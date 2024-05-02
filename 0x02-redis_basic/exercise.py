#!/usr/bin/env python3
"""
This module defines a Cache class that
interfaces with a Redis datastore.
The Cache class provides methods to store data
in Redis using randomly generated keys.
"""

import redis
import uuid
from typing import Callable, Any, Union, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts how many times a method is called,
    using Redis INCR command.

    Args:
    method (Callable): The method to decorate.

    Returns:
    Callable: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Increment the count for the method name in Redis
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to log the history of inputs and
    outputs for a function.

    Args:
    method (Callable): The method to decorate.

    Returns:
    Callable: The wrapped method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Normalize and store inputs
        self._redis.rpush(input_key, str(args))

        # Execute the function and store the output
        result = method(self, *args, **kwargs)
        self._redis.rpush(output_key, str(result))

        return result
    return wrapper


def replay(method: Callable):
    """
    Function to display the history of calls of a
    particular method.

    Args:
    method (Callable): The method to replay the call
    history for.
    """
    instance = method.__self__
    method_name = method.__qualname__
    input_key = f"{method_name}:inputs"
    output_key = f"{method_name}:outputs"

    inputs = instance._redis.lrange(input_key, 0, -1)
    outputs = instance._redis.lrange(output_key, 0, -1)

    print(f"{method_name} was called {len(inputs)} times:")
    for input_str, output_str in zip(inputs, outputs):
        print(f"{method_name}(*{input_str.decode()}) -> {output_str.decode()}")


class Cache:
    """
    A Cache class that allows storing and retrieving
    data from a Redis datastore using unique keys.
    """

    def __init__(self):
        """
        Initializes a new Cache instance, setting up a
        Redis client and flushing any existing data.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores the data in Redis under a randomly generated key.

        Args:
        data (Union[str, bytes, int, float]): data to store.

        Returns:
        str: The key under which the data is stored.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieves data from Redis for the given key and
        optionally applies a conversion function.

        Args:
        key (str): The key whose data is to be retrieved.
        fn (Callable[[bytes], Any], optional): A function to convert
        the data from bytes to a desired format.

        Returns:
        Any: The retrieved data, optionally converted using fn.
        If the key does not exist, returns None.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieves a string from Redis for the given key.

        Args:
        key (str): The key whose string data is to be retrieved.

        Returns:
        Optional[str]: The string data, if the key exists.
        Otherwise, None.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieves an integer from Redis for the given key.

        Args:
        key (str): The key whose integer data is to be retrieved.

        Returns:
        Optional[int]: The integer data, if the key exists and
        the data can be converted to an integer. Otherwise, None.
        """
        return self.get(key, int)

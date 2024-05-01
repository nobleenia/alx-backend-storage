# 0x02. Redis basic

0. exercise.py:
- A Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.

- A store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.

- Type-annotate store correctly. Remember that data can be a str, bytes, int or float.

- A get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.

- get_str and get_int that will automatically parametrize Cache.get with the correct conversion function.

- Implement a system to count how many times methods of the Cache class are called.

- A call_history decorator to store the history of inputs and outputs for a particular function.

- A replay function to display the history of calls of a particular function.

1. web.py: A get_page function (prototype: def get_page(url: str) -> str:). The core of the function is very simple. It uses the requests module to obtain the HTML content of a particular URL and returns it.
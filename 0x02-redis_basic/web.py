#!/usr/bin/env python3
"""
This module implements functionality to fetch
web pages and cache their contents using Redis.
It includes decorators for counting URL access
frequencies and caching responses.
"""

import requests
import redis
from functools import wraps


# Establish a connection to the Redis server
r = redis.Redis(decode_responses=True)  # Use decode_responses to handle string decoding automatically


def count_url_access(func):
    """
    Decorator to count the number of times a URL has been accessed.
    """
    @wraps(func)
    def wrapper(url):
        count_key = f"count:{url}"
        r.incr(count_key)
        return func(url)
    return wrapper


def cache_response(func):
    """
    Decorator to cache the response of a URL for 10 seconds.
    """
    @wraps(func)
    def wrapper(url):
        cache_key = f"cache:{url}"
        cached_data = r.get(cache_key)
        if cached_data:
            return cached_data  # Return decoded data directly from Redis
        # If no cache, fetch data, cache it, and return
        result = func(url)
        # Ensure the result is stored as a string,
        # Redis cannot store complex objects directly
        if isinstance(result, (bytes, bytearray)):
            result = result.decode('utf-8')
        r.setex(cache_key, 10, result)
        return result
    return wrapper


@count_url_access
@cache_response
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL,
    caches it for 10 seconds, and counts the access.

    Args:
    url (str): The URL to fetch.

    Returns:
    str: HTML content of the URL.
    """
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/3000/url/http://www.google.com"
    print(get_page(url))  # First call, should be slow and cached
    print(get_page(url))  # Second call, should be fast due to cache

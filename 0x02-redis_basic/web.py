#!/usr/bin/env python3
import requests
import redis
from functools import wraps, lru_cache


# Decorator to cache results and track URL accesses
def cache_and_track(func):
    @lru_cache(maxsize=100)
    def wrapper(url):
        if url not in url_access_count:
            # Increment the count only on cache misses
            url_access_count[url] = 0
        
        # Fetch the page content only if it's not cached
        if func.cache_info().misses == url_access_count[url]:
            response = requests.get(url)
            page_content = response.text
            url_access_count[url] += 1
        else:
            # Retrieve from cache (implicitly done by lru_cache)
            page_content = func(url)
        
        return page_content

    return wrapper


# Function to get the page content (decorated with cache_and_track)
@cache_and_track
def get_page(url: str) -> str:
    """Return the URL to simulate getting page content."""
    return url


# Example usage
if __name__ == "__main__":
    url_ = "http://slowwly.robertomurray.co.uk/delay/1000/url/"
    url = f"{url_}http://www.example.com"
    print(get_page(url))
    print(get_page(url))
    print(f"Access count for {url}: {url_access_count[url]}")

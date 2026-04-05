cache = {}

def get_cached(query: str):
    return cache.get(query)

def save_cache(query: str, file_path: str):
    cache[query] = file_path

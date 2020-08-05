
class CacheManager:

    img_cache = {}

    def get_cached_image(key):
        # check if there's a registered cache record
        if key in CacheManager.img_cache:
            return CacheManager.img_cache[key]
        # return none otherwise
        return None
    
    def add_cache_record(key, value):
        CacheManager.img_cache[key] = value
from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import caches, cache

def set_data_to_redis(request):
    value_redis={"0":"test1","1":"test2","2":"test3","3":"test4"}
    cache.set("key_name", value_redis, timeout=None)
    return HttpResponse('Redis cache set successfully.')

def get_data_from_redis(request):
    test = cache.get("key_name")
    print(test)
    if test is None:
        return HttpResponse('Redis cache is empty.')
    else:
        return HttpResponse('Redis cache fetch successfully.')

def delete_redis_data(request):
    cache.delete_pattern("key_name")
    return HttpResponse('Redis cache deleted successfully.')

# Create your views here.

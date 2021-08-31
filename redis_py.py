import redis

r = redis.Redis()

print(r.mset({"Croatia": "Zagreb", "Bahamas": "Nassau"}))


print(r.get("Bahamas"))

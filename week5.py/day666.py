
import urllib.request
import json
# Make a request with a custom header

req = urllib.request.Request(
    "http://httpbin.org/headers",
    headers = {"X-Custom-Headers": "OwaaOlangClass"}
)
with urllib.request.urlopen(req) as r:
    data = json.loads(r.read())
    print(data["headers"])
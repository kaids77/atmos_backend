import urllib.request, json
req = urllib.request.Request(
    'http://127.0.0.1:8000/api/auth/signin', 
    method='POST', 
    headers={
        'Content-Type': 'application/json',
        'Origin': 'http://localhost:49811'
    }, 
    data=b'{"email":"admin@atmos.com","password":"admin"}'
)
try:
    with urllib.request.urlopen(req) as response:
        print(response.status, response.read())
except Exception as e:
    import traceback
    print(getattr(e, 'code', str(e)))
    print(e.read() if hasattr(e, 'read') else str(e))

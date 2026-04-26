import requests

print("=" * 60)
print("TESTING BACKEND-FRONTEND CONNECTION")
print("=" * 60)

# Test 1: Login endpoint
print("\n1. Testing POST /api/token (Login)")
print("-" * 60)
response = requests.post('http://127.0.0.1:8000/api/token', json={
    'username': 'testuser',
    'password': 'testpass123'
})
print(f"Status: {response.status_code}")
if response.status_code == 200:
    data = response.json()
    access_token = data.get('access')
    print(f"✅ Response: {data}")
else:
    print(f"❌ Response: {response.text}")
    access_token = None

# Test 2: User endpoint (if login succeeded)
if access_token:
    print("\n2. Testing GET /api/user (Get Current User)")
    print("-" * 60)
    headers = {'Authorization': f'Bearer {access_token}'}
    user_response = requests.get('http://127.0.0.1:8000/api/user', headers=headers)
    print(f"Status: {user_response.status_code}")
    if user_response.status_code == 200:
        user_data = user_response.json()
        print(f"✅ Response: {user_data}")
    else:
        print(f"❌ Response: {user_response.text}")

# Test 3: CORS headers
print("\n3. Testing CORS (OPTIONS request)")
print("-" * 60)
cors_response = requests.options('http://127.0.0.1:8000/api/token')
print(f"Status: {cors_response.status_code}")
cors_headers = cors_response.headers
if 'Access-Control-Allow-Origin' in cors_headers:
    print(f"✅ CORS Enabled: {cors_headers.get('Access-Control-Allow-Origin')}")
else:
    print(f"❌ CORS Not Found in headers")

print("\n" + "=" * 60)
print("TEST COMPLETE")
print("=" * 60)

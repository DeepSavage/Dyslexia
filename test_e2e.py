#!/usr/bin/env python
"""End-to-end test for the Dyslexia app."""

import sys
import os
os.environ['FLASK_ENV'] = 'testing'

from index import app

print('=' * 70)
print('END-TO-END TEST')
print('=' * 70)

client = app.test_client()

# Test 1: Home page
print('\n1. Testing home page (/)...')
resp = client.get('/')
if resp.status_code == 200:
    print('   PASS: Status 200')
    if b'Welcome to Dyslexia Assist' in resp.data:
        print('   PASS: Page content correct')
    else:
        print('   FAIL: Page content incorrect')
        sys.exit(1)
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

# Test 2: Login page
print('\n2. Testing login page (/login)...')
resp = client.get('/login')
if resp.status_code == 200:
    print('   PASS: Status 200')
    if b'Login' in resp.data:
        print('   PASS: Page content correct')
    else:
        print('   FAIL: Page content incorrect')
        sys.exit(1)
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

# Test 3: Register page
print('\n3. Testing register page (/register)...')
resp = client.get('/register')
if resp.status_code == 200:
    print('   PASS: Status 200')
    if b'Register' in resp.data:
        print('   PASS: Page content correct')
    else:
        print('   FAIL: Page content incorrect')
        sys.exit(1)
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

# Test 4: App page (should redirect to login)
print('\n4. Testing app page (/app) - redirect when not logged in...')
resp = client.get('/app', follow_redirects=False)
if resp.status_code == 302:
    print('   PASS: Redirects to login')
else:
    print(f'   FAIL: Status {resp.status_code} (expected 302)')
    sys.exit(1)

# Test 5: Exercise pages
print('\n5. Testing exercise home (/home)...')
resp = client.get('/home')
if resp.status_code == 200:
    print('   PASS: Status 200')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

print('\n6. Testing context exercise (/context)...')
resp = client.get('/context')
if resp.status_code == 200:
    print('   PASS: Status 200')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

print('\n7. Testing match exercise (/match)...')
resp = client.get('/match')
if resp.status_code == 200:
    print('   PASS: Status 200')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

print('\n8. Testing sort exercise (/sort)...')
resp = client.get('/sort')
if resp.status_code == 200:
    print('   PASS: Status 200')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

# Test 9: Module page
print('\n9. Testing module page (/module)...')
resp = client.get('/module')
if resp.status_code == 200:
    print('   PASS: Status 200')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

# Test 10: History page
print('\n10. Testing history page (/history)...')
resp = client.get('/history')
if resp.status_code == 200:
    print('   PASS: Status 200')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

# Test 11: Login simulation
print('\n11. Testing login simulation...')
resp = client.post('/login', data={
    'username': 'testuser',
    'password': 'testpass'
}, follow_redirects=True)
if resp.status_code == 200:
    print('   PASS: Login succeeded (demo mode)')
else:
    print(f'   FAIL: Status {resp.status_code}')
    sys.exit(1)

print('\n' + '=' * 70)
print('ALL END-TO-END TESTS PASSED!')
print('=' * 70)

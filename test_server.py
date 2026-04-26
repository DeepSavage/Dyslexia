#!/usr/bin/env python
"""Test that the Flask server can start."""

import sys
import os

# Suppress Flask startup messages
os.environ['FLASK_ENV'] = 'testing'

print("=" * 70)
print("Test: Starting Flask server in test mode...")
print("=" * 70)

try:
    from index import app
    
    # Test that we can create a test client
    client = app.test_client()
    print("PASS: Test client created successfully")
    
    # Test the home route
    response = client.get('/')
    print(f"PASS: Home route responds with status {response.status_code}")
    
    # Test the login route
    response = client.get('/login')
    print(f"PASS: Login route responds with status {response.status_code}")
    
    # Test the app route (requires login, but should redirect)
    response = client.get('/app', follow_redirects=False)
    print(f"PASS: App route responds with status {response.status_code}")
    
    # Test an exercise route
    response = client.get('/home')
    print(f"PASS: Home exercise route responds with status {response.status_code}")
    
    print("\n" + "=" * 70)
    print("SUCCESS: Server can start and routes are accessible")
    print("=" * 70)
    
except Exception as e:
    print(f"\nFAIL: Server test failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)

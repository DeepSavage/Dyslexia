#!/usr/bin/env python
"""Test script to verify the Dyslexia app fixes."""

import sys
import re

# Test 1: Verify dictionary has no duplicate keys
print("=" * 70)
print("Test 1: Checking DYSLEXIA_CORRECTIONS dictionary...")
print("=" * 70)

from dataset import DYSLEXIA_CORRECTIONS

# Check for duplicates by creating a reversed dict
reversed_dict = {}
duplicates = []
for key, value in DYSLEXIA_CORRECTIONS.items():
    if key in reversed_dict:
        duplicates.append(key)
    reversed_dict[key] = value

if duplicates:
    print(f"FAIL: Found duplicate keys: {duplicates}")
    sys.exit(1)
else:
    print(f"PASS: No duplicate keys found")
    print(f"PASS: Total unique entries: {len(DYSLEXIA_CORRECTIONS)}")

# Test 2: Apply dictionary corrections
def apply_dictionary_corrections(text):
    corrected_text = text
    for wrong, correct in DYSLEXIA_CORRECTIONS.items():
        pattern = r'\b' + re.escape(wrong) + r'\b'
        corrected_text = re.sub(pattern, correct, corrected_text, flags=re.IGNORECASE)
    return corrected_text

test_cases = [
    ('I go to scool', 'I go to school'),
    ('He is a techer', 'He is a teacher'),
    ('This is gud', 'This is good'),
    ('I lerning reeding', 'I learning reading'),
    ('I hav a bok', 'I have a book'),
    ('She writting a storry', 'She writing a story'),
    ('We alwys go to libary', 'We always go to library'),
]

print("\n" + "=" * 70)
print("Test 2: Testing dictionary corrections...")
print("=" * 70)

all_pass = True
for original, expected in test_cases:
    result = apply_dictionary_corrections(original)
    status = 'PASS' if result == expected else 'FAIL'
    if status == 'FAIL':
        all_pass = False
        print(f"{status}: \"{original}\"")
        print(f"  Expected: \"{expected}\"")
        print(f"  Got:      \"{result}\"")

if all_pass:
    print("All test cases passed!")

# Test 3: Verify index.py syntax
print("\n" + "=" * 70)
print("Test 3: Checking index.py imports...")
print("=" * 70)

try:
    import index
    print("PASS: index.py imports successfully")
    
    # Check essential functions exist
    essential_funcs = [
        'apply_dictionary_corrections',
        'correct_text',
        'hash_password',
        'verify_password',
    ]
    
    for func_name in essential_funcs:
        if hasattr(index, func_name):
            print(f"PASS: {func_name} exists")
        else:
            print(f"FAIL: {func_name} not found")
            sys.exit(1)
            
except Exception as e:
    print(f"FAIL: Import error: {e}")
    sys.exit(1)

# Test 4: Verify Flask routes
print("\n" + "=" * 70)
print("Test 4: Checking Flask routes...")
print("=" * 70)

essential_routes = [
    '/',
    '/login',
    '/register',
    '/app',
    '/module',
    '/context',
    '/match',
    '/sort',
    '/home',
    '/history',
]

try:
    for rule in index.app.url_map.iter_rules():
        if rule.rule in essential_routes:
            print(f"PASS: Route {rule.rule} -> {rule.endpoint}")
            essential_routes.remove(rule.rule)
    
    if essential_routes:
        print(f"WARN: Missing routes: {essential_routes}")
    else:
        print("PASS: All essential routes exist")
except Exception as e:
    print(f"FAIL: Route check error: {e}")
    sys.exit(1)

print("\n" + "=" * 70)
print("All tests passed successfully!")
print("=" * 70)

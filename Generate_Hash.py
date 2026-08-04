# -*- coding: utf-8 -*-
"""
Created on Thu Feb 26 19:28:52 2026

@author: YASHASWI
"""

import hashlib

password = input("Enter password: ")

# Convert password to bytes
password_bytes = password.encode()

# Generate SHA256 hash
hash_object = hashlib.sha256(password_bytes)

# Convert to hexadecimal format
hashed_password = hash_object.hexdigest()

print("SHA256 Hash is:", hashed_password)
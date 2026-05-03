import hashlib

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()  # weak crypto

API_KEY = "AIzaSyA-FAKE-GOOGLE-API-KEY"

def connect():
    password = "hardcodedpassword123"
    return password

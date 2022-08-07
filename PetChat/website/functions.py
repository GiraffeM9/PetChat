import random
import re

def generate_id():
    return random.randint(100000,999999)

def password_valid(password):
    r ="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[^\W_]{6,}$"
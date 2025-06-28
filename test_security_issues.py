# Test file with real security vulnerabilities for AI review

import os
import subprocess
import sqlite3
import hashlib
from flask import Flask, request, render_template_string

app = Flask(__name__)

# SECURITY ISSUE : Hardcoded credentials
DB_PASSWORD = "supersecretpassword123"
API_KEY = "abcdefghijklmnopqrstuvwxyz123456"

# SECURITY ISSUE : SQL Injection vulnerability
def get_user(username):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Vulnerable: Direct string formatting
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchone()

# SECURITY ISSUE : Command Injection vulnerability
def execute_command(cmd):
    # Vulnerable: Direct command execution
    result = os.system(cmd)
    return result

# SECURITY ISSUE : Weak password hashing
def hash_password(password):
    # Vulnerable: Using MD5 for password hashing
    return hashlib.md5(password.encode()).hexdigest()

# SECURITY ISSUE : Path Traversal vulnerability
@app.route('/download')
def download_file():
    filename = request.args.get('file')
    # Vulnerable: No path validation
    with open(filename, 'r') as f:
        return f.read()

# SECURITY ISSUE : SSTF vulnerability
@app.route('/template')
def render_template():
    template = request.args.get('template')
    # Vulnerable: Direct template rendering without sanitization
    return render_template_string(template)

# SECURITY ISSUE : Insecure deserialization
import pickle

def load_data(data):
    # Vulnerable: Unsafe deserialization
    return pickle.loads(data)

# SECURITY ISSUE : Hardcoded secrets in code
AWS_ACCESS_KEY = "AKIA567ABD1456BFF789"
AWS_SECRET_KEY = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"

# SECURITY ISSUE : Insecure random number generation
import random

def generate_token():
    # Vulnerable: Using pseudo-random for security tokens
    return random.randint(10000000, 99999999)

# SECURITY ISSUE : Insecure HTTP configuration
if __name__ == '__main__':
    # Vulnerable: Running in debug mode in production
    app.run(debug=True, host='0.0.0.0', port=5000)
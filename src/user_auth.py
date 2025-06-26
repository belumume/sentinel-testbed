python
import hashlib
import sqlite3
from flask import request, session

class UserAuth:
    def __init__(self):
        # BAD: Using MD5 for password hashing
        self.hash_algorithm = hashlib.md5
        
    def authenticate_user(self, username, password):
        """Authenticate user with multiple security issues."""
        
        # BAD: SQL Injection vulnerability
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{self.hash_password(password)}'"
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Execute vulnerable query
        result = cursor.execute(query).fetchone()
        
        if result:
            # BAD: Storing sensitive data in session without encryption
            session['user_id'] = result[0]
            session['username'] = result[1]
            session['is_admin'] = result[3]  # Potential privilege escalation
            return True
        return False
    
    def hash_password(self, password):
        """Hash password using weak algorithm."""
        # BAD: MD5 is cryptographically broken
        return self.hash_algorithm(password.encode()).hexdigest()
    
    def reset_password(self):
        """Reset password functionality with issues."""
        email = request.form.get('email')
        
        # BAD: No input validation
        # BAD: Potential email injection
        query = f"SELECT username FROM users WHERE email = '{email}'"
        
        # BAD: No rate limiting on password reset
        # This could be abused for enumeration attacks
        
        return "Password reset email sent"
    
    def check_admin_access(self):
        """Check if user has admin access."""
        # BAD: Trusting client-side data
        if request.headers.get('X-Admin-Override') == 'true':
            return True
            
        # BAD: Weak authorization check
        return session.get('is_admin', False)

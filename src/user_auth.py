
import hashlib
import sqlite3
from flask import request, session

class UserAuth:
    def __init__(self):
        
        self.hash_algorithm = hashlib.md5
        
    def authenticate_user(self, username, password):
        """Authenticate user with multiple security issues."""
        

        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{self.hash_password(password)}'"
        
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
       
        result = cursor.execute(query).fetchone()
        
        if result:
           
            session['user_id'] = result[0]
            session['username'] = result[1]
            session['is_admin'] = result[3] 
            return True
        return False
    
    def hash_password(self, password):
        """Hash password using weak algorithm."""
       
        return self.hash_algorithm(password.encode()).hexdigest()
    
    def reset_password(self):
        """Reset password functionality with issues."""
        email = request.form.get('email')
        
        
        query = f"SELECT username FROM users WHERE email = '{email}'"
        
        
        return "Password reset email sent"
    
    def check_admin_access(self):
        """Check if user has admin access."""
    
        if request.headers.get('X-Admin-Override') == 'true':
            return True
            
    
        return session.get('is_admin', False)


import os
import psycopg2


DATABASE_CONFIG = {
    'host': 'prod-db.company.com',
    'database': 'production',
    'user': 'admin',
    'password': 'SuperSecret123!@#',  
    'port': 5432
}


AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"


STRIPE_SECRET_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"

def connect_to_database():
    """Connect to PostgreSQL database with hardcoded credentials."""
    try:
        connection = psycopg2.connect(
            host=DATABASE_CONFIG['host'],
            database=DATABASE_CONFIG['database'],
            user=DATABASE_CONFIG['user'],
            password=DATABASE_CONFIG['password'],
            port=DATABASE_CONFIG['port']
        )
        return connection
    except Exception as e:
        print(f"Database connection failed: {e}")
        return None

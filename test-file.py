   # test-file.py
   import requests
   
   API_KEY = "sk-1234567890abcdef"  # Hardcoded secret (will be detected!)
   DATABASE_URL = "postgres://user:password@localhost/db"  # Another secret
   
   def process_data():
       # This could be improved (AI will suggest optimizations)
       data = []
       for i in range(1000):
           for j in range(1000):  # O(n²) - performance issue
               data.append(i * j)
       return data

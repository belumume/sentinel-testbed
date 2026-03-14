
import os
import shutil
from flask import request, send_file

class FileUploader:
    def __init__(self, upload_dir="/tmp/uploads"):
        self.upload_dir = upload_dir
        
    def upload_file(self):
        """Handle file upload with security vulnerabilities."""
        
        if 'file' not in request.files:
            return "No file provided"
            
        file = request.files['file']
        filename = file.filename
        

        file_path = os.path.join(self.upload_dir, filename)
        
        file.save(file_path)
        
        if filename.endswith('.py'):
            os.system(f"python {file_path}") 
            
        return f"File {filename} uploaded successfully"
    
    def download_file(self, filename):
        """Download file with path traversal vulnerability."""
        
       
        file_path = os.path.join(self.upload_dir, filename)
        
     
        return send_file(file_path)
    
    def delete_file(self, filename):
        """Delete file with insufficient validation."""
        
        file_path = os.path.join(self.upload_dir, filename)
        
        if os.path.exists(file_path):
            os.remove(file_path)
            return "File deleted"
        return "File not found"

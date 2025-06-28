# Professional Grade Multi-Tool Scanner Test
# This file contains comprehensive secrets that should be detected
# by multiple professional tools and layers

# AWS Credentials
AWS_ACCESS_KEY = "AKIA567ABD1456BFF789"
AWS_SECRET_KEY = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"

# GitHub Tokens
GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz123456"
GITHUB_OPAT_TOKEN = "gho_abcdefghijklmnopqrstuvwxyz123456"

# API Keys
OPENAI_API_KEY = "sk-abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnop"
STRIPE_API_KEY = "sk_test_51abcdefghijklmnopqrstuvwxyz1234567890"
SLACK_BOT_TOKEN = "xoxb-1234567890-1234567890-1234567890-abcdefghijklmnopqrstuvwxyz"

# Database Credentials
MONGO_URI = "mongodb://user:password@cluster0.abcdef.mongodb.net/database"
POSTGRES_URI = "postgres://user:password@host:5432/db"
MYSQL_URI = "mysql://user:password@host:3306/database"
REDIS_URI = "redis://:password@host:6379/0"

# JWT Tokens
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJub25lYWJsZS5pby5pbmRleCIsImF1ZCI6IjEyMzQ1Njc4OTAiLCJleHAiOjE2MzQ1Njc4OTB9.abcdefghijklmnopqrstuvwxyz1234567890"

# Private Keys
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyz\n-----END RSA PRIVATE KEY-----"
SSH_PRIVATE_KEY = "-----BEGIN OPENSSH PRIVATE KEY-----\nb3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABFwAAAAB3NnNzaC1yc2EAAAABAwEAAQAAAQEA01234567890abcdefghijklmnopqrstuvwxyz\n-----END OPENSSH PRIVATE KEY-----"

# Additional High-Entropy Secrets
API_SECRET = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ENCRYPTION_KEY = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRS"

# Cloud Credentials
AZURE_CLIENT_SECRET = "abcdefghijklmnopqrstuvwxyz1234567890"
GCP_SERVICE_ACCOUNT_KEY = "{\"type\":\"service_account\",\"project_id\":\"test-project\",\"private_key_id\":\"abcdefghijklmnopqrstuvwxyz1234567890\"}"

# This file should trigger:
# - TruffleHog ML detection
# - GitLeaks pattern matching
# - Semgrep semantic analysis
# - Entropy analysis
# - Semantic context analysis
# - Intelligent fusion and deduplication
# - Professional verification and scoring
# Test file for professional multi-tool scanners

# Real secrets that should be detected by multiple tools
AWS_ACCESS_KEY = "AK1234567890ABCDEF"
AWS_SECRET_KEY = "1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5"
GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz123456"
OPENAI_KEY = "sk-abcdefghijklmnopqrstuvwxyz1234567890abcdefghijklmnop"
STRIPE_KEY = "sk_test_51abcdefghijklmnopqrstuvwxyz1234567890"
SLACK_TOKEN = "xoxb-1234567890-1234567890-1234567890-abcdefghijklmnopqrstuvwxyz"
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJub25lYWJsZS5pby5pbmRleCIsImF1ZCI6IjEyMzQ1Njc4OTAiLCJleHAiOjE2MzQ1Njc4OTB9.abcdefghijklmnopqrstuvwxyz1234567890"
MONGO_URI = "mongodb://user:password@cluster0.abcdef.mongodb.net/database"
POSTGRES_URI = "postgres://user:password@host:5432/db"
PRIVATE_KEY = "-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEA1234567890abcdefghijklmnopqrstuvwxyz\n-----END RSA PRIVATE KEY-----"

# This file should trigger multiple secret detection tools
# and demonstrate intelligent deduplication

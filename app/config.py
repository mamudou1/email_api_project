"""
Configuration module for email API project.
Loads environment variables for SMTP and IMAP settings.
"""

import os                                   # Import os module to access environment variables
from dotenv import load_dotenv               # Import load_dotenv to load variables from .env file

# Load environment variables from .env file
load_dotenv()                              

# SMTP configuration
EMAIL_HOST = os.getenv("EMAIL_HOST")                   
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))         
EMAIL_USER = os.getenv("EMAIL_USER")                   
EMAIL_PASS = os.getenv("EMAIL_PASS")                   

# IMAP configuration
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com")   
IMAP_PORT = int(os.getenv("IMAP_PORT", 993))               

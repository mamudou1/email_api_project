import os                                   # Import os module to access environment variables
from dotenv import load_dotenv               # Import load_dotenv to load variables from .env file

load_dotenv()                               # Load environment variables from .env file

EMAIL_HOST = os.getenv("EMAIL_HOST")        # Get SMTP server address from environment
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587)) # Get SMTP port, default to 587 if not set
EMAIL_USER = os.getenv("EMAIL_USER")        # Get email username from environment
EMAIL_PASS = os.getenv("EMAIL_PASS")        # Get email password from environment
IMAP_SERVER = os.getenv("IMAP_SERVER", "imap.gmail.com") # Get IMAP server, default to Gmail IMAP
IMAP_PORT = int(os.getenv("IMAP_PORT", 993)) # Get IMAP port, default to 993

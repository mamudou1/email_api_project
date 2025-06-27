from fastapi import FastAPI, HTTPException           # Import FastAPI framework and HTTPException for error handling
from pydantic import BaseModel                       # Import BaseModel for request data validation
from app.email_utils import send_email, fetch_emails # Import utility functions for sending and fetching emails

app = FastAPI()                                      # Create a FastAPI application instance

class EmailRequest(BaseModel):                       # Define a Pydantic model for email request validation
    to: str                                          # Recipient email address
    subject: str                                     # Email subject
    body: str                                        # Email body content

@app.post("/send")                                   
def send_email_endpoint(email: EmailRequest):
    """
    Endpoint to send an email.
    Receives email details in the request body and sends the email using the send_email utility.
    Returns a success message or raises an HTTP 500 error on failure.
    """
    try:
        result = send_email(email.to, email.subject, email.body)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/inbox")
def inbox():
    """
    Endpoint to fetch emails from the inbox.
    Returns a list of recent emails using the fetch_emails utility.
    Raises an HTTP 500 error on failure.
    """
    try:
        return fetch_emails()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

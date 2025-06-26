from fastapi import FastAPI, HTTPException           # Import FastAPI framework and HTTPException for error handling
from pydantic import BaseModel                       # Import BaseModel for request data validation
from app.email_utils import send_email, fetch_emails # Import utility functions for sending and fetching emails

app = FastAPI()                                      # Create a FastAPI application instance

class EmailRequest(BaseModel):                       # Define a Pydantic model for email request validation
    to: str                                          # Recipient email address
    subject: str                                     # Email subject
    body: str                                        # Email body content

@app.post("/send")                                   # Define POST endpoint at /send for sending emails
def send_email_endpoint(email: EmailRequest):        # Renamed function to avoid shadowing
    try:
        result = send_email(email.to, email.subject, email.body) # Call utility to send email
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) # Return HTTP 500 error with exception details

@app.get("/inbox")                                   # Define GET endpoint at /inbox for fetching emails
def inbox():                                         # Function to handle fetching emails
    try:
        return fetch_emails()                        # Call utility to fetch emails and return them
    except Exception as e:                           # Catch any exceptions
        raise HTTPException(status_code=500, detail=str(e)) # Return HTTP 500 error

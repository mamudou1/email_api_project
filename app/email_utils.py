import smtplib                           # Import smtplib for sending emails via SMTP
import imaplib                           # Import imaplib for receiving emails via IMAP
import email                             # Import email module for parsing email messages
from email.mime.text import MIMEText      # Import MIMEText for creating plain text email parts
from email.mime.multipart import MIMEMultipart # Import MIMEMultipart for creating multipart email messages
from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASS, IMAP_SERVER, IMAP_PORT # Import email config

def send_email(to_email: str, subject: str, body: str): # Define function to send an email
    msg = MIMEMultipart()                # Create a multipart email message object
    msg["From"] = EMAIL_USER             # Set sender email address
    msg["To"] = to_email                 # Set recipient email address
    msg["Subject"] = subject             # Set email subject

    msg.attach(MIMEText(body, "plain"))  # Attach the email body as plain text

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server: # Connect to SMTP server
        server.starttls()                # Start TLS encryption for security
        server.login(EMAIL_USER, EMAIL_PASS) # Log in to the SMTP server
        server.sendmail(EMAIL_USER, to_email, msg.as_string()) # Send the email
        return {"status": "Email sent successfully"} # Return success status

def fetch_emails(limit=5):               # Define function to fetch emails, default limit is 5
    with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) as mail: # Connect to IMAP server using SSL
        mail.login(EMAIL_USER, EMAIL_PASS) # Log in to the IMAP server
        mail.select("inbox")             # Select the inbox folder

        result, data = mail.search(None, "ALL") # Search for all emails in the inbox
        mail_ids = data[0].split()[-limit:]     # Get the latest 'limit' email IDs

        emails = []                      # Initialize list to store fetched emails
        for num in reversed(mail_ids):   # Iterate over email IDs in reverse order (latest first)
            result, msg_data = mail.fetch(num, "(RFC822)") # Fetch the full email message
            raw_email = msg_data[0][1]   # Get the raw email bytes
            msg = email.message_from_bytes(raw_email) # Parse raw email into message object

            subject = msg.get("subject", "")     # Use get to avoid None
            from_ = msg.get("from", "")          # Use get to avoid None
            body = ""                            # Initialize body variable

            if msg.is_multipart():               # Check if the email has multiple parts
                for part in msg.walk():          # Iterate through each part of the email
                    if part.get_content_type() == "text/plain": # Look for plain text part
                        try:
                            body = part.get_payload(decode=True).decode('utf-8', errors='replace') # Robust decode
                        except Exception:
                            body = ""
                        break
            else:
                try:
                    body = msg.get_payload(decode=True).decode('utf-8', errors='replace') # Robust decode
                except Exception:
                    body = ""

            emails.append({                      # Append the extracted email data to the list
                "from": from_,                   # Sender's email address
                "subject": subject,              # Email subject
                "body": body                     # Email body content
            })

        return emails                    # Return the list of fetched emails

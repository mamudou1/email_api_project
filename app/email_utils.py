import smtplib
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import EMAIL_HOST, EMAIL_PORT, EMAIL_USER, EMAIL_PASS, IMAP_SERVER, IMAP_PORT

def send_email(to_email: str, subject: str, body: str):
    """
    Sends an email to the specified recipient using SMTP.
    """
    msg = MIMEMultipart()
    msg["From"] = EMAIL_USER
    msg["To"] = to_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, to_email, msg.as_string())
        return {"status": "Email sent successfully"}

def fetch_emails(limit=5):
    """
    Fetches the latest emails from the inbox using IMAP.
    Returns a list of dictionaries containing 'from', 'subject', and 'body' for each email.
    """
    with imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) as mail:
        mail.login(EMAIL_USER, EMAIL_PASS)
        mail.select("inbox")

        result, data = mail.search(None, "ALL")
        mail_ids = data[0].split()[-limit:]

        emails = []
        for num in reversed(mail_ids):
            result, msg_data = mail.fetch(num, "(RFC822)")
            raw_email = msg_data[0][1]
            msg = email.message_from_bytes(raw_email)

            subject = msg.get("subject", "")
            from_ = msg.get("from", "")
            body = ""

            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        try:
                            body = part.get_payload(decode=True).decode('utf-8', errors='replace')
                        except Exception:
                            body = ""
                        break
            else:
                try:
                    body = msg.get_payload(decode=True).decode('utf-8', errors='replace')
                except Exception:
                    body = ""

            emails.append({
                "from": from_,
                "subject": subject,
                "body": body
            })

        return emails
    

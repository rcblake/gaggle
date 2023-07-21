import sendgrid
import os

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get("SENDGRID_API_KEY"))

data = {
    "personalizations": [
        {
            "to": [{"email": "test@example.com"}],
            "subject": "Sending with SendGrid is Fun",
        }
    ],
    "from": {"email": "test@gaggle.dev"},
    "content": [
        {"type": "text/plain", "value": "and easy to do anywhere, even with Python"}
    ],
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)

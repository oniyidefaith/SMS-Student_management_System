import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from django.conf import settings

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')


def send_email(subject, message, recipient):
    """
    Send an email using SendGrid.
    :param subject: The subject of the email.
    :param message: The content of the email.
    :param recipient: The recipient of the email.
    """

    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)

    from_email = Email(os.environ.get('DEFAULT_FROM_EMAIL'))
    to_email = To(recipient)
    content = Content("text/plain", message)
    mail = Mail(from_email, to_email, subject, content)

    response = sg.client.mail.send.post(request_body=mail.get())

    if response.status_code not in [200, 201]:
        raise Exception("Failed to send email. Status code: %s, Body: %s" % (response.status_code, response.body))

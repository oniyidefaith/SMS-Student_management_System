from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, To, From, Cc, Bcc, Content
import os


class Util:
    @staticmethod
    def send_email(content, subject, to_email):
        message = Mail(
            from_email=From(os.environ.get('EMAIL_HOST_USER')),
            to_emails=To(to_email),
            subject=subject,
            html_content=Content("text/html", content)
        )

        try:
            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            response = sg.send(message)

            if response.status_code == 202:
                print("Email sent successfully!")
            else:
                print("Failed to send email:", response.status_code)
            return response
        except Exception as e:
            print(e)

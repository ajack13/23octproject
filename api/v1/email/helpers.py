from django.core.mail import EmailMessage
from django.conf import settings
from api.models import Email
from datetime import datetime
import csv

import logging
logger = logging.getLogger('interview')

def send_email(data):
    email = EmailMessage(
        subject=data['subject'],
        body=data['body'],
        from_email=settings.EMAIL_HOST_USER,
        to=data['to'],
        bcc=data['bcc'],
        cc=data['cc'],
    )
    email.send()
    logger.info("Email Sent")
    return


def import_email_csv(csv_path):
    with open(csv_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        email_entries = {
            'bcc': [],
            'cc': [],
            'to': []
        }
        for row in csv_reader:
            if line_count == 0:
                # header row
                line_count += 1
            else:
                email_entries['to'].append(row[0])
                email_entries['cc'].append(row[1])
                email_entries['bcc'].append(row[2])
                line_count += 1
        return email_entries


def email_report():
    emails = Email.objects.filter(datetime=datetime.today())
    emails = Email.objects.all()
    total_emails = emails.count()
    body = "Hi \n\n"
    body += "Total emails sent : " + str(total_emails) + "\n"
    subject = "Email stats"
    for email in emails:
        body += str(email.datetime)
        body += "\n"

    data = {"to": [settings.EMAIL_HOST_USER], "subject": subject, "body": body, "cc": [], "bcc":[]}
    send_email(data)
    logger.info("Bulk Email Sent")
    return

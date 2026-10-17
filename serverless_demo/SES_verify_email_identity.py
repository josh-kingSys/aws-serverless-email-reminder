# to verify email in which apps in aws can use to send emails

import boto3

SES = boto3.client("ses")

emails = ["joshuaagbeniyi2+sender@gmail.com", "joshuaagbeniyi2+customer@gmail.com"]

for email in emails:
    response = SES.verify_email_identity(
    EmailAddress=email
    )

print(response)

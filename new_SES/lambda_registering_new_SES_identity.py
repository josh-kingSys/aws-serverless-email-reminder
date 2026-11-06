# lambda to verify new email identity
import boto3, json

SES = boto3.client("ses")

def lambda_handler(event, context):
    # Print event data(python obj) to logs as json string.. 
    print("Received event: " + json.dumps(event))


    data = json.loads(events['body'])
    email = data['email']
    

    response = SES.verify_email_identity(
    EmailAddress=email
    )

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': json.dumps({
            'message': 'Email received',
            'email': email
        })
    }
import boto3

lambda_client = boto3.client("lambda")

with open('python.zip', 'rb') as byte:
    zip_byte = byte.read()

response = lambda_client.create_function(
    FunctionName="email_reminder_lambda",
    Runtime="python3.15",
    Role="arn:aws:iam::810498828759:role/LambdaRoleCat",
    Code={
     "ZipFile" : zip_byte
    },
    Handler='lambda_python.handler'
)
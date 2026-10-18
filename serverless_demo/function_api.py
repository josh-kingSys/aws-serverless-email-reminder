import boto3

lambda_client = boto3.client("lambda")

with open("function.zip", "rb") as file:
    binary_file = file.read()

response = lambda_client.create_function(
    FunctionName="api_function",
    Runtime="python3.15",
    Role="arn:aws:iam::810498828759:role/LambdaRoleCat",
    Handler="api_python_lambda.handler",
    Code={
        'ZipFile' : binary_file
    }
)
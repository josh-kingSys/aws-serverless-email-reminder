import boto3

api = boto3.client("apigateway")

response = api.create_rest_api(
    name="reminder_app",
    endpointConfiguration={
        'types' : ['REGIONAL']
    }

)
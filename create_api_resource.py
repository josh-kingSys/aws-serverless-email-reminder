import boto3

api = boto3.client('apigateway')

response = api.create_resource(
    restApiId='9t2qor65n6',
    parentId='m4phx7h60e',
    pathPart='verify-identity'
)
import boto3

api = boto3.client('apigateway')

response = api.create_resource(
    restApiId="1sz9iafm08",
    parentId="skitli2prh",
    pathPart="reminder_resource"
)
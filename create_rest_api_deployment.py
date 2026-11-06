import boto3

api = boto3.client('apigateway', region_name='us-east-1')

api.create_deployment(
    restApiId='9t2qor65n6',
    stageName='run'
)
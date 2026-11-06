import boto3

api = boto3.client('apigateway')

response = api.put_method(
    restApiId='9t2qor65n6',
    resourceId='7110pj',
    httpMethod='POST',
    authorizationType='none',
    operationName='Verify User\'s Email'
)
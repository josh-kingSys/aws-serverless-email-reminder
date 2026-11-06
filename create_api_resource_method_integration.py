import boto3

api = boto3.client('apigateway', region_name='us-east-1')

lambda_arn = 'arn:aws:lambda:us-east-1:810498828759:function:VerifyIdentity'

response = api.put_integration(
    restApiId='9t2qor65n6',
    resourceId='7110pj',
    httpMethod='POST',
    type='AWS_PROXY',
    integrationHttpMethod='POST',
    uri=(
        'arn:aws:apigateway:us-east-1:lambda:path/'
        f'2015-03-31/functions/{lambda_arn}/invocations'
    )
)
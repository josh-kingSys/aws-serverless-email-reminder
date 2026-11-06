import boto3

api = boto3.client("apigateway", region_name="us-east-1")

REST_API_ID = "9t2qor65n6"
RESOURCE_ID = "7110pj"


ALLOWED_ORIGIN = "http://localhost:8000"


#Create an OPTIONS method on Verify-Identity resource
api.put_method(
    restApiId=REST_API_ID,
    resourceId=RESOURCE_ID,
    httpMethod="OPTIONS",
    authorizationType="NONE",
    apiKeyRequired=False
)


#Put a Mock Integration
api.put_integration(
    restApiId=REST_API_ID,
    resourceId=RESOURCE_ID,
    httpMethod="OPTIONS",
    type="MOCK",
    passthroughBehavior="NEVER",
    requestTemplates={
        "application/json": '{"statusCode": 200}'
    }
)


#Declare the response headers this method can return.
api.put_method_response(
    restApiId=REST_API_ID,
    resourceId=RESOURCE_ID,
    httpMethod="OPTIONS",
    statusCode="200",
    responseParameters={
        "method.response.header.Access-Control-Allow-Origin": False,
        "method.response.header.Access-Control-Allow-Methods": False,
        "method.response.header.Access-Control-Allow-Headers": False
    }
)


#Set the actual values of those response headers.
api.put_integration_response(
    restApiId=REST_API_ID,
    resourceId=RESOURCE_ID,
    httpMethod="OPTIONS",
    statusCode="200",
    responseParameters={
        "method.response.header.Access-Control-Allow-Origin":
            f"'{ALLOWED_ORIGIN}'",

        "method.response.header.Access-Control-Allow-Methods":
            "'POST,OPTIONS'",

        "method.response.header.Access-Control-Allow-Headers":
            "'Content-Type'"
    },
    responseTemplates={
        "application/json": ""
    }
)

print("OPTIONS configured.")
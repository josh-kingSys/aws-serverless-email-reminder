import boto3

ssm = boto3.client('ssm', region_name='us-east-1')

ssm.put_parameter(
    Name='/A4L/Wordpress/DBUser',
    Tier='Standard',
    Type='String',
    DataType='text',
    Value='a4lwordpressuser',
    Overwrite=True
)

ssm.put_parameter(
    Name='/A4L/Wordpress/DBName',
    Tier='Standard',
    Type='String',
    DataType='text',
    Value='a4lwordpressdb',
    Overwrite=True
)

ssm.put_parameter(
    Name='/A4L/Wordpress/DBEndpoint',
    Tier='Standard',
    Type='String',
    DataType='text',
    Value='localhost',
    Overwrite=True
)

ssm.put_parameter(
    Name='/A4L/Wordpress/DBPassword',
    Tier='Standard',
    Type='SecureString',
    KeyId='alias/aws/ssm',
    Value='4n1m4l54L1f3',
    Overwrite=True
)

ssm.put_parameter(
    Name='/A4L/Wordpress/DBRootPassword',
    Tier='Standard',
    Type='SecureString',
    KeyId='alias/aws/ssm',
    Value='4n1m4l54L1f3',
    Overwrite=True
)
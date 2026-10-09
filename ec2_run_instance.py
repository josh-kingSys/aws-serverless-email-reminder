import boto3

# Create EC2 and SSM client connections
ec2 = boto3.client('ec2', region_name='us-east-1')
ssm = boto3.client('ssm', region_name='us-east-1')

ami_id = ssm.get_parameter(
    Name='/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-6.1-x86_64'
)['Parameter']['Value']

response = ec2.run_instances(
    MinCount=1,
    MaxCount=1,

    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Wordpress-Manual'
                }
            ]
        }
    ],

    ImageId=ami_id,
    InstanceType='t3.micro',

    NetworkInterfaces=[
        {
            'DeviceIndex': 0,
            'SubnetId': 'subnet-03a91319b66864aae',
            'Groups': [
                'sg-03024359d759d42b6'
            ],
            'AssociatePublicIpAddress': True,
            'Ipv6AddressCount': 1
        }
    ],

    IamInstanceProfile={
        'Arn': 'arn:aws:iam::810498828759:instance-profile/A4LVPC-WordpressInstanceProfile-3PQr7QWnvMV0'
    }
)

print(response)
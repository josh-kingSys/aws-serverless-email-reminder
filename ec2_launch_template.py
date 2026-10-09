import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

ec2.run_instances(
    LaunchTemplate={
        'LaunchTemplateId': "lt-07d7a518798bce671"
    },
    SubnetId='subnet-03a91319b66864aae',
    MaxCount=1,
    MinCount=1
)
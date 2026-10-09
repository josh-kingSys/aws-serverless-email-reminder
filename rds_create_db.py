import boto3

rds = boto3.client('rds', region_name='us-east-1')

response = rds.create_db_instance(
    DBInstanceIdentifier='a4lWordPress',
    DBInstanceClass='db.t3.micro',
    Engine='mysql',
    MasterUsername='a4lwordpressuser',
    MasterUserPassword='4n1m4l54L1f3',
    VpcSecurityGroupIds=['sg-0d2f5c967e8a8c40e'],
    DBSubnetGroupName='wordpressrdssubnetgroup',
    MultiAZ=False,
    PubliclyAccessible=False,
    AvailabilityZone='us-east-1a',
    DBName='a4lwordpressdb',
    AllocatedStorage=20
)

print(response)
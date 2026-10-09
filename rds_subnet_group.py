import boto3

rds = boto3.client('rds', region_name='us-east-1')

response = rds.create_db_subnet_group(
    DBSubnetGroupName='WordPressRDSSubNetGroup',
    DBSubnetGroupDescription='WordPress RDS Subnet Group',
    SubnetIds=[
        'subnet-060aec805dcba0758',
        'subnet-0a1936d228c001243',
        'subnet-0ed071579fc39aab1'
    ]
)

print(response)
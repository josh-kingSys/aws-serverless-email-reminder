import boto3

rds = boto3.client('rds', region_name='us-east-1')

endpoint = rds.describe_db_instances(DBInstanceIdentifier='a4lWordPress')['DBInstances'][0]['Endpoint']
print(endpoint)
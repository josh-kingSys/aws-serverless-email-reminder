import boto3
import json

s3 = boto3.client("s3", region_name="us-east-1")

bucket_name = "reminder-static-site1357999"

response = s3.list_buckets(Prefix=bucket_name)


bucket_exists = False

for bucket in response["Buckets"]:
    if bucket["Name"] == bucket_name:
        bucket_exists = True
        break

if not bucket_exists:
    s3.create_bucket(Bucket=bucket_name)

s3.put_public_access_block(
    Bucket=bucket_name,
    PublicAccessBlockConfiguration={
        "BlockPublicAcls": False,
        "IgnorePublicAcls": False,
        "BlockPublicPolicy": False,
        "RestrictPublicBuckets": False
    }
)

policy = {
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "PublicRead",
            "Effect": "Allow",
            "Principal": "*",
            "Action": ["s3:GetObject"],
            "Resource": [f"arn:aws:s3:::{bucket_name}/*"]
        }
    ]
}

s3.put_bucket_policy(
    Bucket=bucket_name,
    Policy=json.dumps(policy)
)

s3.put_bucket_website(
    Bucket=bucket_name,
    WebsiteConfiguration={
        "ErrorDocument": {"Key": "index.html"},
        "IndexDocument": {"Suffix": "index.html"}
    }
)

print(f"http://{bucket_name}.s3-website-us-east-1.amazonaws.com")
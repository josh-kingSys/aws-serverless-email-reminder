import boto3
import json

iam = boto3.client("iam")

role = iam.create_role(
    RoleName="LambdaRoleCat",
    AssumeRolePolicyDocument=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": {"Service": "lambda.amazonaws.com"},
            "Action": "sts:AssumeRole"
        }
        ]
    }
    )
)

put_policy = iam.put_role_policy(
    RoleName="LambdaRoleCat",
    PolicyName="cloudwatchlogs",
    PolicyDocument=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                "Effect": "Allow",
                "Action": ["logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutLogEvents"],
                "Resource": "arn:aws:logs:*:*:*"
                }
            ]

        }
    )
)
import boto3
import json

iam = boto3.client("iam")

try: 
    iam.get_role(
    RoleName="StateMachineRole"
    )


except iam.exceptions.NoSuchEntityException:
    role = iam.create_role(
        RoleName="StateMachineRole",
        AssumeRolePolicyDocument=json.dumps({
            "Version": "2012-10-17",
            "Statement": [{
                "Effect": "Allow",
                "Principal": {"Service": "states.amazonaws.com"},
                "Action": "sts:AssumeRole"
            }
            ]
        }
        )
    )

put_policy = iam.put_role_policy(
    RoleName="StateMachineRole",
    PolicyName="cloudwatchlogs",
    PolicyDocument=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                "Effect": "Allow",
                "Action": ["logs:CreateLogGroup",
                            "logs:CreateLogStream",
                            "logs:PutLogEvents",
                            "logs:CreateLogDelivery",
                            "logs:GetLogDelivery",
                            "logs:UpdateLogDelivery",
                            "logs:DeleteLogDelivery",
                            "logs:ListLogDeliveries",
                            "logs:PutResourcePolicy",
                            "logs:DescribeResourcePolicies",
                            "logs:DescribeLogGroups"
                            ],
                "Resource": "arn:aws:logs:*:*:*"
                }
            ]

        }
    )
)

put_policy = iam.put_role_policy(
    RoleName="StateMachineRole",
    PolicyName="invokelambdasandsendSNS",
    PolicyDocument=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                "Effect": "Allow",
                "Action": [
                    "lambda:InvokeFunction",
                    "sns:*"
                    ],
                "Resource": "*"
                }
            ]

        }
    )
)
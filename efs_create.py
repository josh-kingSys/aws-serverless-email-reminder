import boto3

efs = boto3.client('efs', region_name='us-east-1')


subnet_ids = [
    'subnet-001482733274af991',
    'subnet-06d476180cc06b11f',
    'subnet-088da90230878bacc'
]

for subnet_id in subnet_ids:
    efs.create_mount_target(
        FileSystemId="fs-02ffc1d0ec0e71d54",
        SubnetId=subnet_id,
        SecurityGroups=[
            'sg-0a476d2b2aec0e44b'
        ]
    )

efs.put_lifecycle_configuration(
    FileSystemId="fs-02ffc1d0ec0e71d54",
    LifecyclePolicies=[
        {
            'TransitionToIA': 'AFTER_30_DAYS'
        },
        {
            'TransitionToPrimaryStorageClass': 'AFTER_1_ACCESS'
        }
    ]
)

print("Mount targets and lifecycle policy created.")
import boto3, json

step_function = boto3.client('stepfunctions')

response = step_function.create_state_machine(
    name="EmailReminder",
    definition="""
            {
        "Comment": "Email Reminder.",
        "StartAt": "Timer",
        "States": {
            "Timer": {
            "Type": "Wait",
            "SecondsPath": "$.waitSeconds",
            "Next": "Email"
            },
            "Email": {
            "Type" : "Task",
            "Resource": "arn:aws:states:::lambda:invoke",
            "Parameters": {
                "FunctionName": "arn:aws:lambda:us-east-1:810498828759:function:email_reminder_lambda",
                "Payload": {
                "Input.$": "$"
                }
            },
            "Next": "NextState"
            },
            "NextState": {
            "Type": "Pass",
            "End": true
            }
        }
        }
""",
    roleArn="arn:aws:iam::810498828759:role/StateMachineRole",
    type='STANDARD',
    loggingConfiguration={
        "level" : "ALL",
        "includeExecutionData" : True,
        "destinations" : [
            {
                "cloudWatchLogsLogGroup" : {
                    "logGroupArn" : "arn:aws:logs:us-east-1:810498828759:log-group:stepfunction-loggroup:*"
                }
            }
        ]
    }

)
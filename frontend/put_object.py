import boto3

s3 = boto3.client("s3")

files = {
    "index.html": "text/html",
    "main.css": "text/css",
    "serverless.js": "application/javascript"
}

for filename, content_type in files.items():
    with open(filename, "rb") as file_body:
        s3.put_object(
            Bucket="reminder-static-site1357999",
            Key=filename,
            Body=file_body,
            ContentType=content_type
        )
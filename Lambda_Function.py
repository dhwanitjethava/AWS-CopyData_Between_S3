import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    # 1. IAM User for trigger the Lambda Function
    file_name = event['Records'][0]['s3']['object']['key'];
    service_name='s3'
    region_name='ap-south-1'
    aws_access_key_id='AKIAS63ZKOQK6LSG2G7T'
    aws_secret_access_key='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'
    
    # 2. Get data from S3 (Specified region)
    s3 = boto3.resource(
        service_name = service_name,
        region_name = region_name,
        aws_access_key_id = aws_access_key_id,
        aws_secret_access_key = aws_secret_access_key
        )
    
    # 3. Copy data to another S3 bucket
    copy_source = {
        'Bucket': 'learning-source-bucket',
        'Key': file_name
    }
    
    # 4. For specifying file_name and modification for destination bucket
    s3.meta.client.copy(copy_source,'learning-destination-bucket',file_name)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

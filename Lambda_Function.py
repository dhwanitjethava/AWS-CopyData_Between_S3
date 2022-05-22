import sys
import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # TODO implement
    
    #1 - Print Source bucket name
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    print(source_bucket)

    #2 - Print .json filename
    json_file = event['Records'][0]['s3']['object']['key']
    print(json_file)

    #3 - Print file objects(metadata) of json_file
    json_file_obj = s3_client.get_object(Bucket=source_bucket, Key=json_file)
    print(json_file_obj)

    #4 - Print the file content
    data = json_file_obj['Body'].read().decode('utf-8')
    print(data)
    
    #5. Print Destination bucket name
    destination_bucket = '<Enter name of the destination bucket>'
    print(destination_bucket)
    
    #6. Copy data from Source Bucket
    copy_source = {'Bucket':source_bucket, 'Key':json_file}
   
    #7. Copy to Destination Bucket
    try:
        response = s3_client.copy_object(Bucket = destination_bucket, Key = json_file, CopySource = copy_source)
    except:
        print("ERROR: Could not copy data in Destination Bucket")
    
    #8 - Delete file after move data from Source Bucket
    print("Deleting the file from S3 bucket")
    try:
        response = s3_client.delete_object(Bucket=source_bucket, Key=json_file)
    except:
        print("ERROR: Deletion is not successful!")
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

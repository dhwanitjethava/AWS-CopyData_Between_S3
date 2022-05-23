# AWS : Copy/Move Data Between S3 Buckets
#### Services used :
    AWS S3, Amazon CloudWatch, AWS Lambda, Amazon IAM

### Dataflow Diagram:
<img width="1342" alt="AWS_CopyData_Between_S3" src="C:\Users\Ashok Jethava\Desktop\GitHub Repository\AWS_CopyData_Between_S3\AWS_CopyData_Between_S3.jpg">

### AWS S3 Buckets configuration:
Our goal is to MOVE or COPY data between S3 buckets. First of all we need to create two buckets.
One bucket is source bucket and one bucket is destination bucket. Both buckets should have the same region.

    1. Source bucket
    2. Destination bucket

### IAM Role for Lambda Function:
Create a IAM role for Lambda function that allows you to perform actions while lambda function triggers.
Assign full access of Amazon S3 and Amazon CloudWatch (for monitoring and logs) to role for Lambda function.
IAM Role for Lambda function has the following policies:

    1. AmazonS3FullAccess
    2. CloudWatchFullAccess

### Lambda Function:
Create a Lambda function and attach IAM role for Lambda function that created above.

    Runtime - Python 3.9
    Role - Use existing role (Role for Lambda function that created before)

#### Add Lambda function trigger
    Select S3 trigger
    Select S3 Bucket that is Source bucket
    Event type - PUT
    Suffix: .json

Now, write lambda function in the code section in Python language.
Please refer to lambda_function.py for more information.

### Verify Lambda function:
Let's verify the lambda function that will trigger whenever .json file uploaded to our Source bucket.
Once the lambda function is called, following parameters execute accordingly Lambda function.

- Print the Source bucket name
- Print JSON file name
- Print Metadata of that JSON file
- Print the JSON file contents
- Print Destination bucket name
- Copy that JSON file to the Destination bucket
- Delete that JSON file from the Source bucket

### Monitoring Lambda Function through CloudWatch:
We can monitor Lambda function through CloudWatch monitoring service. There are logs in CloudWatch that created every time whenever the Lambda function triggers. It shows the results of the Lambda function and prints error messages to the log. With the help of CloudWatch, we can optimize the Lambda function and time complexity of the Lambda function.

# AWS Lambda Function: Stop Instances on Weekends

This repository contains a Python AWS Lambda function that stops running EC2 instances on weekends. The function is triggered by a CloudWatch Events schedule and uses the Boto3 library to interact with the AWS EC2 service.

## Prerequisites
- An AWS account with necessary IAM permissions to create and manage Lambda functions, CloudWatch Events, and EC2 instances.
- Python 3.9 or later installed on your local machine.
- AWS CLI configured with valid credentials.

## Setup Instructions
1. Clone the repository or download the source code.
2. Navigate to the project directory.

## Deployment Steps
1. Ensure that you have the AWS CLI configured with the necessary credentials and permissions.
2. Open the AWS Lambda console and create a new function.
3. Set the runtime to Python 3.9.
4. Choose an execution role with the required permissions.
5. Set the "Handler" field to `stop_instances_on_weekends`.
6. Copy and paste the code from the `lambda_function.py` file into the Lambda function code editor.
7. Set the desired timeout duration for the Lambda function.
8. Save the Lambda function.

## CloudWatch Events Configuration
1. Open the AWS CloudWatch console.
2. Create a new rule with a schedule expression that triggers on weekends (e.g., `cron(0 0 ? * SAT-SUN *)` for midnight UTC on Saturdays and Sundays).
3. Add the Lambda function as a target for the CloudWatch Events rule.
4. Save the rule.

## Testing
You can test the Lambda function by manually invoking it from the AWS Lambda console or waiting for the scheduled CloudWatch Events trigger.



import boto3
import datetime

def stop_instances_on_weekends(event, context):
    ec2 = boto3.client('ec2')
    
    today = datetime.datetime.now()
    if today.weekday() in [5, 6]:  # Saturday or Sunday
        response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                ec2.stop_instances(InstanceIds=[instance_id])
        
        print('Instances stopped successfully on weekends.')
    else:
        print('No instances to stop.')

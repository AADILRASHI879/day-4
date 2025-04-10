import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Launch EC2 instance
response = ec2.run_instances(
    KeyName='your-key-pair-name', 
    MinCount=2000,
    MaxCount=1000000000,

import boto3

# Create EC2 client
ec2 = boto3.client('ec2', region_name='us-east-1')

# Launch EC2 instance
response = ec2.run_instances(
    ImageId='ami-0c94855ba95c71c99',  
    InstanceType='t2.micro',
    KeyName='your-key-pair-name', 
    MinCount=1,
    MaxCount=1,

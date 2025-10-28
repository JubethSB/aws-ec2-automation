import boto3

# Create EC2 client
ec2 = boto3.client('ec2')

# Launch a new EC2 instance
response = ec2.run_instances(
    ImageId='ami-0c02fb55956c7d316',  # Example Amazon Linux AMI ID (region-dependent)
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1
)

print("✅ EC2 instance launched successfully!")
print("Instance ID:", response['Instances'][0]['InstanceId'])

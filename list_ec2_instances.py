import boto3

# Initialize a session using your AWS credentials
ec2 = boto3.resource('ec2')

# Create a filter to get all instances
filters = []

# Filter instances based on their state (running, stopped, etc.)
instances = ec2.instances.filter(Filters=filters)

# Loop through the instances and print details
for instance in instances:
    print(f"Instance ID: {instance.id}, "
          f"Instance Type: {instance.instance_type}, "
          f"Public IP: {instance.public_ip_address}, "
          f"State: {instance.state['Name']}")

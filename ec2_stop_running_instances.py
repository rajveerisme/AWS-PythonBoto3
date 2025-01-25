import boto3

# Initialize a session using your AWS credentials
ec2 = boto3.resource('ec2')

# Create a filter for instances in the 'running' state
filters = [
    {
        'Name': 'instance-state-name',
        'Values': ['running']
    }
]

# Filter the instances based on the filters above
instances = ec2.instances.filter(Filters=filters)

# Loop through the instances and stop them
for instance in instances:
    print(f"Stopping Instance ID: {instance.id}")
    instance.stop()
    instance.wait_until_stopped()  # Wait until the instance is in the 'stopped' state
    print(f"Instance {instance.id} is now stopped.")


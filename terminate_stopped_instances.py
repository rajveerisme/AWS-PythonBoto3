import boto3

# Initialize a session using your AWS credentials
ec2 = boto3.resource('ec2')

# Create a filter for instances in the 'stopped' state
filters = [
    {
        'Name': 'instance-state-name',
        'Values': ['stopped']
    }
]

# Filter the instances based on the filters above
instances = ec2.instances.filter(Filters=filters)

# Loop through the instances and terminate them
for instance in instances:
    print(f"Terminating Instance ID: {instance.id}")
    instance.terminate()
    instance.wait_until_terminated()  # Wait until the instance is fully terminated
    print(f"Instance {instance.id} has been terminated.")


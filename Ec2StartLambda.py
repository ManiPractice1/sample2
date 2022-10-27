import boto3
region = 'us-east-1'
instances = ['i-0455fffccb6e65cab']
ec2 boto3.client('ec2', region_name=region)


def lambda_handler(event, context):
     ec2.start_instances(Instance Ids=instances)
     print("started your instances:" + str(instances))

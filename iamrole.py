import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    
    ec2 = boto3.client('ec2',region_name='ap-south-1')

    ec2_descinst = ec2.describe_instances()
    #print(instances.InstanceId)

    for reservation in ec2_descinst['Reservations']:
        #print (reservation)
        for instance in reservation['Instances']:
            print(instance['InstanceId'])
            response = ec2.associate_iam_instance_profile(
            IamInstanceProfile={
                'Name': 'CWAgentRole',
                
            },
            InstanceId=instance['InstanceId']
            #InstanceId="i-0aabf1368d3acf584"
        )
        print(response)
        #print(instance['InstanceId'])

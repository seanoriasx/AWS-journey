import boto3
import datetime

def lambda_handler(event, context):
    print("Scheduled event received:", event)
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('RefreshLogs')
    table.put_item(Item={
        'RunId': str(datetime.datetime.utcnow()),
        'Status': 'Success'
    })

    return {"message": "Data refresh complete"}

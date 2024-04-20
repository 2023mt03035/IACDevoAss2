import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('StudentDB')

def lambda_handler(event, context):
    body = json.loads(event['body'])
    student_id = body['student_id']
    name = body['name']
    title = body['tital']
    # You can add more attributes as needed

    response = table.put_item(
       Item={
            'student_id': student_id,
            'name': name
            'title': title
            # Add more attributes here
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Student saved successfully!')
    }

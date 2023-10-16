import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookdata')

def lambda_handler(event, context):
    try:
        # Use the scan operation to retrieve all items from the table
        response = table.scan()

        items = response.get('Items', [])

        if items:
            return {
                'statusCode': 200,
                'body': json.dumps(items)
            }   
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('No items found in the table')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error getting items from the table: ' + str(e))
        }

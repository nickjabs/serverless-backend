import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookdata')

def lambda_handler(event, context):
    try:
        # Assuming the request body includes 'BookID' to identify the item to delete
        request_body = json.loads(event['body'])
        book_id = request_body.get('BookID', '')

        if not book_id:
            raise Exception('Bad Request: Missing required data')

        # Check if the item exists before attempting deletion
        response = table.get_item(
            Key={
                'BookID': book_id
            }
        )

        if 'Item' in response:
            # Item exists, so proceed with deletion
            table.delete_item(
                Key={
                    'BookID': book_id
                }
            )

            return {
                'statusCode': 200,
                'body': json.dumps('Item deleted from the table')
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps('Item not found in the table')
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error deleting the item: ' + str(e))
        }

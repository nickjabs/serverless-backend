import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookdata')

def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])

        # Assuming the request body includes 'AuthorName'
        author_name = request_body.get('AuthorName', '')

        if not author_name:
            raise Exception('Bad Request: Missing required data')

        # Generate a unique BookID
        book_id = str(uuid.uuid4())

        item = {
            'AuthorName': author_name,
            'BookID': book_id
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps({'BookID': book_id, 'message': 'Item added to the table'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error adding the item: ' + str(e))
        }

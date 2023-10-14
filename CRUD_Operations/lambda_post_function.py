import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('bookdata')

def lambda_handler(event, context):
    try:
        request_body = json.loads(event['body'])

        # Assuming the request body includes 'BookID' and 'AuthorName'
        book_id = request_body.get('BookID', '')
        author_name = request_body.get('AuthorName', '')

        if not book_id or not author_name:
            raise Exception('Bad Request: Missing required data')

        item = {
            'AuthorName': author_name,
            'BookID': book_id
        }

        table.put_item(Item=item)

        return {
            'statusCode': 201,
            'body': json.dumps('Item added to the table')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error adding the item: ' + str(e))
        }

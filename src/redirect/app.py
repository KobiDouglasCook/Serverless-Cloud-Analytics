import json
import boto3
from datetime import datetime

# dynamodb = boto3.resource('dynamodb')
# table = dynamodb.Table("UrlTable")  

eventbridge = boto3.client('events')

def lambda_handler(event, context):
    short_code = event.get("pathParameters", {}).get("shortCode")

    if not short_code:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'shortCode is required'})
        }
    
    # Lookup the short code in DynamoDB
    #response = table.get_item(Key={'shortCode': short_code})
    #item = response.get('Item')

    # Simulate a found item for testing purposes
    item = {
        "longUrl": "https://www.fuegodomain.com",
        "shortCode": short_code
    }

    if not item:
        return {
            'statusCode': 404,
            'body': json.dumps({'error': 'Short URL not found'})
        }
    
    long_url = item['longUrl']

    # Record the redirect event in EventBridge for analytics
    # eventbridge.put_events(
    #     Entries=[
    #         {
    #             'Source': 'urlshortener.analytics',
    #             'DetailType': 'RedirectEvent',
    #             'Detail': json.dumps({
    #                 'shortCode': short_code,
    #                 'timestamp': datetime.utcnow().isoformat()
    #             })
    #         }
    #     ]
    # )

    # Return a 301 redirect response
    return {
        "statusCode": 301,
        "headers": {
            "Location": long_url
        },
        "body": ""
    }
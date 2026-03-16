import os
import json
import boto3
import string
import random 
from datetime import datetime, timedelta

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("UrlTable")

def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(length))
    return short_code

def lambda_handler(event, context):
    body = json.loads(event.get('body', '{}'))
    long_url = body.get('longUrl')

    if not long_url:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'longUrl is required'})
        }
    
    # Generate a unique short code
    short_code = generate_short_code()

    # TTL: expire after 30 days
    ttl_days = 30
    ttl_timestamp = int((datetime.utcnow() + timedelta(days=ttl_days)).timestamp())

    item = {
        'shortCode': short_code,
        'longUrl': long_url,
        'createdAt': datetime.utcnow().isoformat(),
        'ttl': ttl_timestamp,
        "clickCount": 0
    }

    table.put_item(Item=item)

    return { 
        "statusCode": 200,
        "body": json.dumps({
            "shortCode": short_code,
            "shortUrl": f"https://fuegodomain.com/{short_code}",
            "expiresAt": ttl_timestamp
        })
    }
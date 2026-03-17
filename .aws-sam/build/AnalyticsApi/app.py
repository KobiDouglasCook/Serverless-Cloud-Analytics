import json
import boto3
from boto3.dynamodb.conditions import Key
from decimal import Decimal

def convert_decimals(obj):
    if isinstance(obj, list):
        return [convert_decimals(i) for i in obj]
    if isinstance(obj, dict):
        return {k: convert_decimals(v) for k, v in obj.items()}
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    return obj


dynamodb = boto3.resource('dynamodb')
url_table = dynamodb.Table("UrlTable")
events_table = dynamodb.Table("AnalyticsEvent")

def lambda_handler(event, context):
    # Extract shortCode from path parameters
    short_code = event.get("pathParameters", {}).get("shortCode")

    # Validate input
    if not short_code:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "shortCode is required"})
        }

    # Fetch URL metadata
    url_item = url_table.get_item(Key={"shortCode": short_code}).get("Item")

    if not url_item:
        return {
            "statusCode": 404,
            "body": json.dumps({"error": "Short URL not found"})
        }

    # Fetch analytics events
    response = events_table.query(
        KeyConditionExpression=Key("shortCode").eq(short_code)
    )

    events = response.get("Items", [])

    result = {
        "shortCode": short_code,
        "longUrl": url_item["longUrl"],
        "createdAt": url_item["createdAt"],
        "clickCount": url_item.get("clickCount", 0),
        "events": events
    }

    clean = convert_decimals(result)

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(clean)
    }
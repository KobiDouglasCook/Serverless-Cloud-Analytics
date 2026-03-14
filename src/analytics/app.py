import json
import boto3
from datetime import datetime

dynamodb = boto3.resource("dynamodb")
events_table = dynamodb.Table("AnalyticsEvents")

def lambda_handler(event, context):
    # EventBridge sends events in an array under "Records" or directly as "detail"

    # Extract the event detail safely
    detail = event.get("detail", {})

    short_code = detail.get("shortCode")
    timestamp = detail.get("timestamp", datetime.utcnow().isoformat())

    if not short_code:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "shortCode missing in analytics event"})
        }

    # Write the analytics event to DynamoDB
    events_table.put_item(
        Item={
            "shortCode": short_code,
            "timestamp": timestamp,
            "userAgent": detail.get("userAgent"),
            "ip": detail.get("ip"),
            "country": detail.get("country")
        }
    )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Analytics event processed",
            "shortCode": short_code,
            "timestamp": timestamp
        })
    }

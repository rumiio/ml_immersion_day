import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client = boto3.client('rekognition')
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': 'aiml-rumi',
                'Name': 'ML Immersion Day/birthday_party1.jpeg'
            }
        })
    
    response_str = json.dumps(response)
    response_json = json.loads(response_str)
    
    for item in response_json['Labels']:
        if item['Confidence'] >= 80:
            print(item['Name'] + ': Confidence level is ' + str("{0:.1f}%".format(item['Confidence'])))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

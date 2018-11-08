import json
import boto3

def lambda_handler(event, context):
    # create a client object
    client = boto3.client('rekognition')
    
    # replace <YOUR_BUCKET_NAME> with your bucket name and <YOUR_IMAGE_NAME>' with the name of your image
    response = client.detect_labels(
        Image={
            'S3Object': {
                'Bucket': '<YOUR_BUCKET_NAME>',
                'Name': '<YOUR_IMAGE_NAME>'
            }
        })
    
    # conver the response dictionary object to JSON
    response_str = json.dumps(response)
    response_json = json.loads(response_str)
    
    # iterate through the JSON to extract what you want to see
    for item in response_json['Labels']:
        if item['Confidence'] >= 80:
            print(item['Name'] + ': Confidence level is ' + str("{0:.1f}%".format(item['Confidence'])))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

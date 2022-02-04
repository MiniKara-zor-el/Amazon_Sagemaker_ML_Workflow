#classification

import json
import base64
import boto3

# Fill this in with the name of your deployed model
ENDPOINT = 'image-classification-2022-02-03-12-04-46-415'
runtime = boto3.client('runtime.sagemaker')

def lambda_handler(event, context):
    print(event)
    # Decode the image data
    image = base64.b64decode(event['body']['image_data'])
    print(image)
    
    response = runtime.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType='image/png',
        Body=image)

    print(response)
    
    result = json.loads(response['Body'].read().decode('utf-8'))
    
    event["body"]["inferences"] = result
    print('Event BODY IS:', event['body'])
    
    
    return {
          "statusCode": 200,
          "body": event['body']
    }
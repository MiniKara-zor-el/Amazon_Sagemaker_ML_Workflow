#Test Event

{
  "image_data": "image_data",
  "s3_key": "test/bicycle_s_000776.png",
  "s3_bucket": "sagemaker-us-east-1-967897925194"
}

#serial_input 

import json
import boto3
import base64

s3 = boto3.client('s3')
BUCKET_NAME = 'sagemaker-us-east-1-967897925194'
PREFIX = 'test'
def lambda_handler(event, context):
    """A function to serialize target data from S3"""

    # Get the s3 address from the Step Function event input
    key = event['s3_key']
    #bucket = event['s3_bucket']
    bucket = BUCKET_NAME
    

    # Download the data from s3 to /tmp/image.png
    s3.download_file(bucket, key, '/tmp/image.png')

    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }




#Test_event for classification

{
  "body": {
    "image_data": "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",
    "s3_key": "test/bicycle_s_000776.png",
    "s3_bucket": "sagemaker-us-east-1-967897925194",
    "inferences": []
  }
}


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
    # inferences = result
    # event["inferences"] = inferences
    
    return {
          "statusCode": 200,
          "body": event['body']
    }


#test_event for coonfidence inference 

{
  "body": {
    "image_data": "iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAACiZJREFUWIVFl0mPXEd2hb+YX76XY2XNLJFqSs12i7Io2g3YgH+BNwb8L214azTgpQFvjAZahtGyZYlUkayBJVZWTu/lmyPCiyzYi7u5izgn7niu+Md/+KfoEkeSJGiliRGk1ABUVc3D8oE0yziYHpAkjtV6xWJxT5omSClJs5SmaYgxcnR0RN97/vn3/8Ll+/e8+vZbXv/lXxBiRAqFNpq2afHeo7SmLEr0cDjBWotzDiklAoEQEqk167zmD//xXwQEf/bFrzk7PUYbhdIpu6rj6HCCFBJrJQezA1zi6PqOb199w9nZKUo7rt7dUjUt0+mE0WjIIE2RQqOUQqsOHQJ4H2jbbg8sBVIIRIAffnzDn354w/zwmM3qOySB0WiIc5bZwZTZdEbiLANjiBF2RUUInrPTY6azKVXVs1hsePvTJRHPdDrm5cuXTCcTRAQlFTrGQIyRGCNCRAQgBAgROTiY4vuWj7dX+LplV2x5cn7GaDRkNpuglCTGAES8949vgACUEAwSS5YlzCYjtvmaYZpglMT3HVJEYujRQkYQ4dH26BEQ9Hz5qwtOD0f86fvvccrxu9ev+Pb1K/q+4/z8DGMEXV8TYv9Ihv1nQo8g0jY1bbfj6bNTpDxjMh6jVKRpCmIwNHWDvr29QgiJ1hql5J4EEaM1AsE3Xz3n+dMT0mTMi1+/4OjokG2+ZTTKUEZS7Fq22/X/gYfgiT6AEPTe0zYVERiNRqzWC4QQzGYHSAXGKrQxDiHAWYdUCgEEwFqDlJKvXv45xli2D1vqVc5D48nrilD2WGNofYcWCthHLqDoRY8AJPCwKRhNxmhlSJyg6zuUUkihEHj0bHoAgDEGYwxSKUKMjxFRdN4jpeTN9z/xn//27xwfn1IJGNgBVkm6uG+p4WhENhoSRKDsKtqyoliuub39yF/9zV9zfHJOLVuUMjib4L0nhIgGgRB78z7Q9T0hRoQQxBgpdyVKSbSCxGlevfqamCW4QYoWkqZtsYkjAMpoooCi3hGbDl/WtHVDtS1w2rKrG5IkQUpN1+2J68ek0/eBPF8TYkAqBTHirCP0PYtfFlRVwfnpMW1bMj2dYbMUoy2irBiOR0itiTGCkozlDNUFVOdZLx5Ybzas12vWRc75+fljrQRiiOg8L5BSIqXk6uqaqq4xTmON5eLsHKsM1x+uiKHh6OiAX+4+kp0fEb0BKVnnaza7nPnRIdpofACtFU4buqrh4eGBqqpYLlfcLZccHh4TIvSdR2mFXq83dG1L23Zc39xSNRXaaqpix/3HO6bDMcUm5+kXFwyjYnG/oqka3HhCDAHnHGVVsVotyUYjkkECvafxPQ+f7tHG0Jc7Fg9L8qLgzZu3CCHQWnN4OEdXZc3NzQ3z+ZxnTz8nyoB2mny5ZrNc8T///QMucTz77XOyZARIVg9rDk7O8N5jtGY0zGh9z3azxvcZwyTl3dtLfN3y9PNnvPnXSzptmB0eQRQ0TUPpK3a7En19/YHpbMqLF1+ilCLf5bRdg55MGLqEzXKJ0Ip3l+85+eY1yTAjv18Su57wODm1Mdgkoa4q6nzH4vqO9+/fc3p6wofLt9R5QZpmXJx9zXg2pe17urYnz3Ok0pIvvniOMpKIp+9bVsslzhgS57h49pRXv3tNU9a8u7lmMBqy22zpmhqIxLifnlIphoMMFWDx6RPpKOPuYcFoNGaUpISqZjiwaC2wiWWQDTg9PUU+eXJOkjjapqEoCuq6RmuFtZau7zg5OWEymfDZZxfc3N4SBIQYKMuSAPgYIIKMELqe+7tfGI/H1HVN13V89fVLpvMDogCtNUKw7wAiSknkcDjEe89qtWK1XJFlQ4bZkDzPaZuWLMvo2o7pZMpwNGRbFAit2G63hBgeCUREiNzd3KKkRFtLXhTM53M+Le4ZjEe0fUdd1wQfiDEghSQCUkrJZrOh73tmBzOSxGGMYbvZMpvNcIkDQCnFweEhTejxMbBarQjeI6NA+MCHy3dUVcXFs6es8w1HJyc8ubhAaIXJBnTBs9vtCDEQwn77+r5HhhCQUjKfz8myDCEERVFQ7ArSNMUYQ5qlOOdIs4wgIlFKdmVJWzfoKPh0c8fN+yvOL54QtKJqW56cnzMej5keHHDxq2cMx2O22+3/b0wgxoAGcM4RY6RtWz7df+K77/5IXzYcHx6hNxahFVYZcAZlDF4rYoxU+Y7NbsHHm1uOT0/QznL96Y6u77HO0TQNQgom8wO+/M0L1sslXdcRpQIiIQZ0U9YYpfFi77i+vuLnny+xQvHx7g6bpgQBThs8kcUvC3zZYBLL25/fsdvkHB3NGM8nFGVBvt4iBcS+o+06hDFEaZkfnbF8WHF7+5GDo0NiCPRdi377009YZxBKgAwURY41hq6qWdwvkNbQRU/oAr7tqXclwyxDOstyvUUqyaZruLr/SGh77u8WSCN59+ZHJAJhEpqgMVLSdZ6rd+/I8w3WGbRRiL//27+LRVWAiEQRODl9QjYYcfnjjxghCHi6GGh7iUIxHY0xzvLZ58/4/MvnLDdbdlVDkjiuL99wd/OB0XhC6BpEDIBG2RRnLX1bUbc1PnpcYnCDIVqpgNHQPgqF9eoBIzSp1bRljtOQOkuhJEpaksSgtKJpSu7urlhtd6zXLfP5EVorpOrp+wYjJaHrGCQWrTy+3iJ8j4k9iVE4owh9j27qgulkTL4rGY3HJIOMTx/vaauS1GiU9MTQkzjHdDql3Bb0PeRbKOsVZe25v69RSEQsSKzEackwG0PwyBjp2xqlIEpJFA7jLD5EsmyADt7Ttx2T0ZiqbjmYn/Cb3x5x/fNb8uUD0UeQkGaa9WpBXezQ1hKkZzweMtCazEWK9S1GtgytxQePIBKlJkkSzHBIkef4GJBSERFoo8nSIToG2GwKRlEzGk1YLFYM0o7BcEqMCrTEpY4Yasr8jiQxWGdJBg6rNH3TMTAtzhlEH7FC0xCom5okm6KSIfPZhHRcsM1zqrphkA5JBkPKYosmSqQQlLsKhCIbjwm+R2nFYDRCGk0XOsp8xyBxJNahtEKISFvX+zxbSZJomp2nKmtMklBWFQGDMY7NtmAynRCVJWy3aGPYbjfs8i06cSnaGlzqCALK3QYBJM4RfKTvQUrBJMsQcYBSihDCXrqJiEkMgUjXQZCWJvTQB3zTstze0lUl3WRKsctBCtq6YltXaK0wwqMHgxRlFVILBJHEGZzeS3IQGGNwziKip+ta2rYFPFoZlADfd8QAg0GGlBqJJHQNTksGbkjEU2yW9FtI0hSr9OPNwb4WQvSEzhMfNZrRBqJACkmSJDjnUErSd+1+jMa4Pyy1IfQdUirSQYLRlq7zpNaAijjnMM4hhKIoK7ySJFlG9JG26gg+MkgSdNs2CMl+N2sFIaCtxBqLNQYpBG3T0rY1MYJzA2IE73tAMkgSlJD0TUvXNFgpcC5Bqb1E7/oWqyU6S0EpqroieI/RjhgE/wv+32s8qHrTdAAAAABJRU5ErkJggg==",
    "s3_key": "test/bicycle_s_000776.png",
    "s3_bucket": "sagemaker-us-east-1-967897925194",
    "inferences": [
      0.9622887969017029,
      0.03771118074655533
    ]
  }
}


#confidence inference 

import json
THRESHOLD = .7

def lambda_handler(event, context):
    print(event)
    # Grab the inferences from the event
    inferences = event['body']['inferences']
    print('inferences:', inferences)
    #print(event['inferences'])
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = (max(inferences) > THRESHOLD)
    print('whether meets threshold:', meets_threshold)
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        pass
    else:
        raise("THRESHOLD_CONFIDENCE_NOT_MET")
    

    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
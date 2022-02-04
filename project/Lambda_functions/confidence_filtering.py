#confidence_filtering

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
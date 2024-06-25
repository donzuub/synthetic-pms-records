import json

def transform_query_result(record):
    result, = record  # Unpack the single column result
    
    # Print the raw result and its type
    print(f"Raw result: {result}")
    print(f"Type of result: {type(result)}")
    
    # Assuming result is already a dictionary
    if isinstance(result, dict):
        return result
    else:
        try:
            # If result is a JSON string, parse it
            return json.loads(result)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None

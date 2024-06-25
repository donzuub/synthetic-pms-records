from datetime import datetime

def transform_data(input_data):
    current_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + "Z"
    
    subscriber = input_data.get("subscriber", {})
    dependent = input_data.get("dependent")
    payer = input_data.get("payer", {})
    appointment = input_data.get("appointment", {})
    
    patient_data = {
        "subscriberFirstName": subscriber.get("firstName", ""),
        "subscriberLastName": subscriber.get("lastName", ""),
        "birthdate": subscriber.get("dateOfBirth", "").split("T")[0] if subscriber.get("dateOfBirth") else "",
        "groupId": subscriber.get("groupId", ""),
        "coverage": {
            "primary": {
                "payerName": payer.get("name", ""),
                "policyNumber": subscriber.get("id", ""),
                "groupNumber": subscriber.get("groupId", "")
            }
        },
        "appointments": [
            {
                "dateTime": current_date,
                "type": "Routine Checkup",
                "status": "Scheduled"
            }
        ]
    }

    if input_data.get("secondary"):
        patient_data["coverage"]["secondary"] = {
            "payerName": payer.get("name", ""),
            "policyNumber": subscriber.get("id", ""),
            "groupNumber": subscriber.get("groupId", "")
        }
    
    if dependent:
        patient_data["dependents"] = [
            {
                "firstName": dependent.get("firstName", ""),
                "lastName": dependent.get("lastName", ""),
                "birthdate": dependent.get("dateOfBirth", "").split("T")[0] if dependent.get("dateOfBirth") else ""
            }
        ]

    return patient_data

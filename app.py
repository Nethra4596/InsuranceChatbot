def lambda_handler(event, context):
    print("Lex event:", event)

    intent_name = event.get("sessionState", {}).get("intent", {}).get("name")

    if intent_name == "HelloIntent":
        return {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": "HelloIntent",
                    "state": "Fulfilled"
                }
            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Hello! This is a response from Lambda."
                }
            ]
        }

    return {
        "sessionState": {
            "dialogAction": {
                "type": "Close"
            },
            "intent": {
                "name": intent_name or "UnknownIntent",
                "state": "Fulfilled"
            }
        },
        "messages": [
            {
                "contentType": "PlainText",
                "content": "I didn't quite get that."
            }
        ]
    }

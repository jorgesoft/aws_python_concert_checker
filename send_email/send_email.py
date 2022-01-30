import boto3

def send_email(type, link):
    ses_client = boto3.client("ses", region_name="us-west-2")
    CHARSET = "UTF-8"

    answer = ""
    content = link
    if type == "error":
        answer = "ERROR EN PROGRAMA"
    elif type == "ya":
        answer = "Tickets ya!"

    response = ses_client.send_email(
        Destination={
            "ToAddresses": [
                "jorgecarrilloit@gmail.com",
            ],
        },
        Message={
            "Body": {
                "Text": {
                    "Charset": CHARSET,
                    "Data": content,
                }
            },
            "Subject": {
                "Charset": CHARSET,
                "Data": answer,
            },
        },
        Source="jorgecarrilloit@gmail.com",
    )
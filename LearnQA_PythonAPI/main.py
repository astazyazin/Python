from json.decoder import JSONDecodeError
import requests

mail = "tonystark.inablr@mailinator.com"
passw = "11111aA@"
flow = "USER_PASSWORD_AUTH"
clID = "alji7d2mkv4l6eut22e251i0l"
response = requests.post("https://cognito-idp.us-east-2.amazonaws.com/",
                         data={"AuthParameters": {"USERNAME": mail, "PASSWORD": passw},
                               "AuthFlow": flow, "ClientId": clID},
                         headers={'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
                                  'Content-Type': 'application/x-amz-json'
                                                  '-1.1'})
# print(response.text)
try:
    parsed_response_text = response.json()
    print(parsed_response_text)
except JSONDecodeError:
    print("Response isn't JSON format")

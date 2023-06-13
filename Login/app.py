import json

def lambda_handler(event, context):
   password=json.loads(event["body"])['Password']
   if password =='Whatever':
      return 'true'
   else:
      return 'false'
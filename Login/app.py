import json

def lambda_handler(event, context):
   password=json.loads(event["body"])['Password']
   if password =='whatever':
      return 'true'
   else:
      return 'false'
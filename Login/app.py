import json

def lambda_handler(event, context):
   password=json.loads(event["body"])['Password']
   if password =='whatever':
      return {'statuscode':200,
      'headers':{'Content-Type':'application/json'},'body':'true'}
   else:
      return {'statuscode':200,
      'headers':{'Content-Type':'application/json'},'body':'false'}
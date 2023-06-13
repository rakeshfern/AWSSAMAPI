import json

def lambda_handler(event, context):
   message={'message':'Execution started successfully!'}
   password=json.loads(event["body"])['Password']
   if password =='whatever':
      return {'statuscode':200,
      'headers':{'Content-Type':'application/json'},'body':json.dumps(message)}
   else:
      return {'statuscode':200,
      'headers':{'Content-Type':'application/json'},'body':json.dumps(message)}
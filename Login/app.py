import json

def lambda_handler(event, context):
   message={'message':'Execution started successfully!'}
   password=json.loads(event["body"])['Password']
   if password =='whatever':
      return {'statusCode':200,
      'headers':{'Content-Type':'application/json'},'body':"true"}
   else:
      return {'statusCode':200,
      'headers':{'Content-Type':'application/json'},'body':"false"}
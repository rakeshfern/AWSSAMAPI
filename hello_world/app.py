from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            # "location": ip.text.replace("\n", "")
        }),
    }


if __name__ == '__main__':
    app.run()
     

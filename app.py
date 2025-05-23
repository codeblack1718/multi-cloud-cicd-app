from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from CI/CD pipeline!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

# test: docker push to ACR
# Trigger AWS GitHub Actions
# trigger multi-cloud deploy

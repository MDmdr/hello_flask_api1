from flask import Flask
app = Flask(__name__)

import requests

# -------------------------------------

@app.route('/')
def home():   
   text = "hello API 1!" + '<br><br> <a href="/api">Click</a>'
   return text# "hello API 1!"

@app.route('/api')
def api1():
    # r =requests.get('https://example.com')
    r =requests.get('https://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline')
    if r.status_code == 200:
        print("ok api")
        # return "ok api"

        return r.text

    return "fail api"
# -------------------------------------

if __name__ == "__main__":
   app.run(debug=True, port=8067, host='0.0.0.0')
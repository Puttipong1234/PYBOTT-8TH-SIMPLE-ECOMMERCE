from flask import Flask , request

app = Flask(__name__)

@app.route("/internet_banking",methods= ['POST'])
def get_promptpay_data():
    res = request.get_json()
    user_charge_id = res["data"]["id"]
    status = res["data"]["status"]
    
    print(user_charge_id)
    print(status)
    # update firebase database
    
    return "200"

if __name__ == '__main__':
    app.run(port=8080,debug=True)
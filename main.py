from flask import Flask, jsonify, render_template, request
from models.utils import HousePrice


app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("We are in House price prediction")
    return render_template("index.html")


@app.route('/predict_charges',methods =["POST","GET"])
def get_house_price():
    if request.method == "GET":
        print("we are in GET method")
        #data = request.form 
        #print("Data::",data)
    
        #size=eval(data["size"])
        #bath=eval(data["bath"])
        #balcony=eval(data["balcony"])
        #area_type=(data["area_type"])
        #location=(data["location"])

        size = eval(request.args.get("size"))
        bath = eval(request.args.get("bath"))
        balcony = eval(request.args.get("balcony"))
        area_type = (request.args.get("area_type"))
        location = (request.args.get("location"))
        
        
    
        med_ins= HousePrice(size,bath,balcony,area_type,location)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)
       # return jsonify({"Result" :f"Predicted House Price in Bengaluru  {charges}/- Rs. Only"})

    else:
        print("we are in POST method")

        size = eval(request.form.get("size"))
        bath = eval(request.form.get("bath"))
        balcony = eval(request.form.get("balcony"))
        area_type = (request.form.get("area_type"))
        location = (request.form.get("location"))

        
    
        med_ins= HousePrice(size,bath,balcony,area_type,location)
        charges = med_ins.get_predicted_price()
        return render_template("index.html",prediction=charges)
        
if __name__=="__main__":
 app.run(host='0.0.0.0' , port= 2002, debug=True)
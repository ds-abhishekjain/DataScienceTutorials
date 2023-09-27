from flask import Flask,render_template,jsonify
from flask import request

app = Flask(__name__)

# GET : Through URL we are sending the data
# POST : THrough body we are sending the data

@app.route("/",methods = ['GET','POST'])
def home_page():
    return render_template("index.html")

@app.route("/math",methods = ['POST'])
def math_operation():
    if (request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2']) 

        if (ops == 'add'):
            r = num1+num2
            result = 'the sum of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        

        if (ops == 'subtract'):
            r = num1-num2
            result = 'the diff of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        

        if (ops == 'multiply'):
            r = num1*num2
            result = 'the product of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        

        if (ops == 'divide'):
            r = num1/num2
            result = 'the division of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        
        return render_template('result.html',result = result)  

# For API testing we use POSTMAN App across industry, lets see an example
@app.route("/postman_data",methods = ['POST'])
def math_operation2():
    if (request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2']) 

        if (ops == 'add'):
            r = num1+num2
            result = 'the sum of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        

        if (ops == 'subtract'):
            r = num1-num2
            result = 'the diff of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        

        if (ops == 'multiply'):
            r = num1*num2
            result = 'the product of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        

        if (ops == 'divide'):
            r = num1/num2
            result = 'the division of '+str(num1)+ 'and' +str(num2)+ 'is' +str(r)
        
        return jsonify(result) 

#@app.route("/") # we can acess this func on browser using the adress below on which server is running
#def hello_world():
 #   return "<h1>Hello, World<h1>"

@app.route("/helloworld2") # this is known as app routing , we can access this by adding /helloworld2 to ip adress
def hello_world2():
    return "<h1>Hello, World2<h1>"

@app.route("/helloworld3")
def hello_world3():
    return "<h1>Hello, World3<h1>"

@app.route("/test")
def test():
    return "this is a test message"

@app.route("/test2")
def test2():
    data = request.args.get('x')
    return "this is a data input from my URL {}".format(data)

if __name__ == "__main__":
    app.run(host = "0.0.0.0",port=8080)

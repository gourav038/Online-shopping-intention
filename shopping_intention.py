from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
scaler=pickle.load(open('C:/Users/gkg32/OneDrive/Desktop/GOURAV_MAJOR_PROJECT/pickle/scaler.pkl','rb'))
rfc=pickle.load(open('C:/Users/gkg32/OneDrive/Desktop/GOURAV_MAJOR_PROJECT/pickle/rfc.pkl','rb'))

app = Flask(__name__)

@app.route("/")
def fun():
    return render_template('shopping.html')

@app.route('/shopping',methods=['POST'])
def fun1():
    if request.method=='POST':
        admin_page_duration=float(request.form['admin_page_duration'])
        num_of_info_pages=float(request.form['num_of_info_pages'])
        num_of_product_pages=float(request.form['num_of_product_pages'])
        product_page_duration=int(request.form['product_page_duration'])
        total_duration=float(request.form['total_duration'])
        ExitRates=float(request.form['ExitRates'])
        PageValues=float(request.form['PageValues'])
        Month=float(request.form['Month'])
        Region=float(request.form['Region'])
        user_type=int(request.form['user_type'])
        Weekend=int(request.form['Weekend'])
        scaled=scaler.transform([[admin_page_duration,num_of_info_pages,num_of_product_pages,product_page_duration,total_duration,ExitRates,PageValues,Month,Region,user_type,Weekend]])
        output=rfc.predict(scaled)
        if output[0]==1:
            x='Purchased'
            return render_template('result.html',result=x)
        else:
            x='Not Purchased'
            return render_template('result.html',result=x)    


if __name__=="__main__":
    app.run(host="0.0.0.0")

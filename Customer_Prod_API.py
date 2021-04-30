from flask import Flask, jsonify, request 
import os
import os.path
import json
import sys
import pandas as pd
import numpy as np
#pytesseract.pytesseract.tesseract_cmd="D:\\Program Files\\Tesseract-OCR\\tesseract.exe"
 
app = Flask(__name__) 
app.config["DEBUG"]=True 

@app.route('/sampleapi/<string:typeofscript>', methods = ['GET','POST']) 
def disp(typeofscript):
    ## AADAR CARD FACE RECOGNITION
    if typeofscript=='printcust':
        user_id = request.args.get('mock_user_id')
        user_id=int(user_id)
        data=pd.read_csv('customerdata.csv')
        print(data.columns)
        data['CUSTOMER_ID']=data['CUSTOMER_ID'].astype('int')
        customer_df=data.loc[data['CUSTOMER_ID'] == user_id].groupby(['CUSTOMER_ID','PRODUCT_NAME']).size().reset_index(name='COUNT')
        #customer_df.to_json()
        return jsonify(customer_df.to_json())
if __name__ == '__main__': 

    app.run(debug = True,use_reloader=False,threaded=True)

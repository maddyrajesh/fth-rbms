from flask import Flask
from flask import jsonify
import pandas as pd
category = pd.read_csv('category.csv',low_memory=False)
frequent_freq = pd.read_csv('frequent_freq.csv',low_memory=False)


app = Flask(__name__)
@app.route('/')
def Most_Bought():
    output = frequent_freq['Unnamed: 0'].tolist()[:10]
    return jsonify({"Most_Bought_Items": output})

app.run(threaded=True)

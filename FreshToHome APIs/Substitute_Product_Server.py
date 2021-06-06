from flask import Flask
from flask import jsonify
import pandas as pd
category = pd.read_csv('category.csv',low_memory=False)
frequent_freq = pd.read_csv('frequent_freq.csv',low_memory=False)

def compliment_items(Query):
    output = frequent_freq.sort_values(by=[Query],ascending=False)[['Unnamed: 0',Query]]
    output.rename(columns = {'Unnamed: 0':'PRODUCT_NAME', Query: 'Purchase History'}, inplace = True)
    output.reset_index(drop=True)
    output = output.loc[output['Purchase History'] > 0]
    query_db = pd.merge(output, category, how="inner", on=["PRODUCT_NAME"])
    Query_Category = query_db.loc[query_db['PRODUCT_NAME'] == Query]['CATEGORY'][0]
    query_db = query_db[1:]
    Same_Category = query_db.loc[query_db['CATEGORY'] == Query_Category]
    Same_Category_List = Same_Category['PRODUCT_NAME'][:10].tolist()
    return(Same_Category_List)


app = Flask(__name__)
@app.route('/<string:Query>/')
def substitute_item(Query):
    if compliment_items(compliment_items(Query)[0])[0] != Query:
        return jsonify({"Substitute_Item": compliment_items(compliment_items(Query)[0])[0]})
    else:
        return jsonify({"Substitute_Item": compliment_items(compliment_items(Query)[0])[1]})
app.run(threaded=True)


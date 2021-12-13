from flask import Flask
from flask import url_for
from flask import render_template
import pandas as pd
from sodapy import Socrata


client = Socrata("www.datos.gov.co", None)
results = client.get("sdvb-4x4j", limit=2000)
df = pd.DataFrame.from_records(results)

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

def html_table():
    return render_template('index.html')    

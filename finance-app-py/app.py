# app.py
from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_stock_data():
    # Ler os dados do arquivo CSV
    data = pd.read_csv('data/stock.csv')

    # Convertemos os dados em um formato adequado para enviar para o JavaScript
    labels = data['Data'].tolist()
    values = data['PrecoFechamento'].tolist()
    
    return {
        'labels': labels,
        'values': values
    }

if __name__ == '__main__':
    app.run(debug=True)

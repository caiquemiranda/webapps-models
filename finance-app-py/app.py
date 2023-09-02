# app.py
from flask import Flask, render_template
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_stock_data():
    # Obtenha os dados da ação da Petrobras
    petrobras = yf.Ticker('PETR4.SA')
    data = petrobras.history(period='1y')
    
    # Convertemos os dados em um formato adequado para enviar para o JavaScript
    labels = data.index.strftime('%Y-%m-%d').tolist()
    values = data['Close'].tolist()
    
    return {
        'labels': labels,
        'values': values
    }

if __name__ == '__main__':
    app.run(debug=True)
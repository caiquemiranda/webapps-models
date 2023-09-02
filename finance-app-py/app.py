from flask import Flask, render_template, Response
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    # Obtenha os dados da ação da Petrobras
    petrobras = yf.Ticker('PETR4.SA')
    data = petrobras.history(period='1y')
    
    # Crie um gráfico de linha com matplotlib
    plt.figure(figsize=(8, 4))
    plt.plot(data.index, data['Close'], label='Preço de Fechamento (R$)', color='blue')
    plt.xlabel('Data')
    plt.ylabel('Preço de Fechamento (R$)')
    plt.title('Gráfico de Ações da Petrobras')
    plt.legend()
    
    # Salve o gráfico em um objeto BytesIO
    img_stream = BytesIO()
    plt.savefig(img_stream, format='png')
    img_stream.seek(0)
    
    # Converta a imagem em base64
    img_base64 = base64.b64encode(img_stream.read()).decode('utf-8')
    
    return render_template('index.html', img_base64=img_base64)

if __name__ == '__main__':
    app.run(debug=True)

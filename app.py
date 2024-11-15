from flask import Flask, render_template, request, redirect, url_for, jsonify
import yfinance as yf

app = Flask(__name__)

# In-memory storage for user portfolio (could use a database for persistence)
portfolio = {}

@app.route('/')
def index():
    return render_template('index.html', portfolio=portfolio)

@app.route('/add_stock', methods=['POST'])
def add_stock():
    ticker = request.form.get('ticker').upper()
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")

    if not data.empty:
        # Save stock information in portfolio
        portfolio[ticker] = {
            'name': stock.info['shortName'],
            'price': round(data['Close'][0], 2),
            'change': round((data['Close'][0] - data['Open'][0]), 2)
        }
    return redirect(url_for('index'))

@app.route('/remove_stock/<ticker>', methods=['POST'])
def remove_stock(ticker):
    portfolio.pop(ticker, None)
    return redirect(url_for('index'))

@app.route('/refresh_data')
def refresh_data():
    # Refresh data for all stocks in the portfolio
    for ticker in portfolio:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        if not data.empty:
            portfolio[ticker]['price'] = round(data['Close'][0], 2)
            portfolio[ticker]['change'] = round((data['Close'][0] - data['Open'][0]), 2)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

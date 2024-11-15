# stock-portfolio-tracker

# Author  - Azhan Khan
#Link- http://127.0.0.1:5501/template/index.html

Stock Portfolio Tracker
A web-based application that allows users to monitor their stock investments, add and remove stocks, view current performance, and track value changes over time. This project fetches real-time stock data from financial APIs to provide up-to-date information on stocks in the user's portfolio.

##Project Description
The Stock Portfolio Tracker helps users keep track of their stock investments in real time. Users can:

Add stocks by their ticker symbol to get current data on each stock.
View individual stock prices and daily price changes.
Get an overview of their portfolio’s total value and performance.
Refresh stock data to get the latest prices.
Remove stocks from their portfolio.


##Features
Add Stocks: Enter a stock ticker symbol to add it to your portfolio.
Real-Time Stock Prices: Displays up-to-date stock prices and daily change metrics using a financial API.
Portfolio Overview: Displays each stock's name, ticker symbol, price, and daily price change in a table format.
Remove Stocks: Option to remove stocks from the portfolio.
Refresh Data: Update all stock prices with the latest available data.


##Technologies Used
Front-End:

HTML: Structure of the application.
CSS: Styling for layout and visuals.
JavaScript: For front-end interactivity and dynamic updates.
Back-End:

Python (Flask): To create a lightweight server for handling API requests and rendering the UI.
APIs:

Yahoo Finance (via yfinance): Fetches real-time stock data.

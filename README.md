# Quickyearning_Backend_Django
<br>

### Packages Required
Run these in command prompt of project directory:<br>
`pip install django`<br>
`pip install djangorestframework`<br>
`pip install django-cors-headers`<br>
`pip install yfinance`<br>
<br>

### How to start Server
To start the django server, run this command in terminal of the django_backend directory:<br>
`python manage.py runserver`<br>
<br>

### Documentation to fetch api

- Balance Sheet<br>
api will include yearly and quaterly data
Link: `server_link/api/get_balance_sheet/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_balance_sheet/RELIANCE.NS`<br>

- Cash Flow<br>
api will include yearly and quaterly data
Link: `server_link/api/get_cash_flow/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_get_flow/RELIANCE.NS`<br>

- Income Statement<br>
api will include yearly and quaterly data
Link: `server_link/api/get_income_statement/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_income_statement/RELIANCE.NS`<br>

- Historical Data<br>
Link: `server_link/api/get_historical_data/<ticker_symbol>/?interval=<interval>&period=<interval>`<br>
Example: `http://127.0.0.1:8000/api/get_historical_data/RELIANCE.NS/?interval=1d&period=1mo`<br>
Please Note: Only following combinations work:<br>
<table>
    <thead>
        <tr>
            <th>Period</th>
            <th>Interval</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>1d</td>
            <td>1m, 5m, 15m, 30m, 1d</td>
        </tr>
        <tr>
            <td>1mo</td>
            <td>5m, 15m, 30m, 1d, 1mo</td>
        </tr>
    </tbody>
</table><br>

- Sector and Industry Information<br>
Link: `server_link/api/get_sector_and_industry/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_sector_and_industry/RELIANCE.NS`<br>

- Calendar information<br>
Link: `link/api/get_calendar/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_calendar/RELIANCE.NS`<br>

- News information<br>
Link: `link/api/get_news/<ticker_symbol>`<br>
Example: `http://127.0.0.1:8000/api/get_news/RELIANCE.NS`<br>

- Stock Statistics
This API will give the statistics of any ticker symbol and the desired number of quarters. By default the data is displayed for 7 quarters if not provided. Including the current date and the previous n quarters is displayed. It gives information such as Market_Cap, Enterprise_Value, Trailing_PE, Price_to_Sales, Price_to_Book, Enterprise_Value_to_Revenue, Enterprise_Value_to_EBITDA, Forward_PE, PEG_Ratio.
Link: `server_link/api/get_stock_stats/<ticker_symbol>/<num_of_quarters>`
Example: `http://127.0.0.1:8000/api/get_stock_stats/RELIANCE.NS/7/`<br>

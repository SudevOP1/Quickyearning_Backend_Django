import yfinance as yf
import pandas as pd
import json
from datetime import datetime, date

# Helper Functions

def convert_timestamp_to_string(timestamp):
    return timestamp.strftime("%Y-%m-%d %H:%M:%S") if isinstance(timestamp, (datetime, pd.Timestamp)) else str(timestamp)

class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

# Main Functions

def get_balance_sheet_as_json(ticker_symbol):
    bs = yf.Ticker(ticker_symbol).balance_sheet
    bs_json_cleaned = {
        str(key): {
            sub_key: (None if pd.isna(sub_value) or sub_value in [float('inf'), float('-inf')] else sub_value)
            for sub_key, sub_value in value.items()
        }
        for key, value in bs.to_dict().items()
    }
    return bs_json_cleaned

def get_cash_flow_as_json(ticker_symbol, **kwargs):
    cf = yf.Ticker(ticker_symbol).cashflow
    cf_json_cleaned = {
        str(key): {
            sub_key: (None if pd.isna(sub_value) or sub_value in [float('inf'), float('-inf')] else sub_value)
            for sub_key, sub_value in value.items()
        }
        for key, value in cf.to_dict().items()
    }
    return cf_json_cleaned

def get_historical_data_as_json(ticker_symbol, **kwargs):
    historical_data = yf.Ticker(ticker_symbol).history(**kwargs)
    # handle pandas dataframe
    if isinstance(historical_data, pd.DataFrame):
        historical_data = historical_data.reset_index()
        for col in historical_data.columns:
            if pd.api.types.is_datetime64_any_dtype(historical_data[col]):
                historical_data[col] = historical_data[col].apply(convert_timestamp_to_string)
        # Convert DataFrame to list of dictionaries
        historical_data = historical_data.to_dict(orient="records")
    return json.loads(json.dumps(historical_data))

def get_sector_and_industry_as_json(ticker_symbol, **kwargs):
    info = yf.Ticker(ticker_symbol).info
    result = {
        "sector": info.get("sector", "N/A"),
        "industry": info.get("industry", "N/A")
    }
    return result

def get_cal_as_json(ticker_symbol, **kwargs):
    cal = yf.Ticker(ticker_symbol).calendar
    if cal is None:
        return json.dumps({"error": "No calendar data available"})
    return json.loads(json.dumps(cal, cls=DateEncoder))

def get_news_as_json(ticker_symbol):
    news = yf.Ticker(ticker_symbol).news
    if news is None:
        return json.dumps({"error": "No calendar data available"})
    return json.loads(json.dumps(news, cls=DateEncoder))



def get_company_profile(ticker_symbol):
    """
    Fetch and display the profile of a company, including its basic details.
    
    Parameters:
        ticker_symbol (str): The ticker symbol of the company.
    """
    ticker = yf.Ticker(ticker_symbol)
    info = ticker.info  # Fetch metadata and profile details
    return info

def get_analysis_data_as_json(ticker_symbol):
    result = {}
    try:
        # Fetch ticker object
        data = yf.Ticker(ticker_symbol)

        # Access analysis-related attributes
        analysis_data = {
            "earnings_estimate": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.earnings_estimate.to_dict().items()}
                if data.earnings_estimate is not None
                else "No earnings estimate data available"
            ),
            "revenue_estimate": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.revenue_estimate.to_dict().items()}
                if data.revenue_estimate is not None
                else "No revenue estimate data available"
            ),
            "earnings_history": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.earnings_history.to_dict().items()}
                if data.earnings_history is not None
                else "No earnings history data available"
            ),
            "eps_trend": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.eps_trend.to_dict().items()}
                if data.eps_trend is not None
                else "No EPS trend data available"
            ),
            "eps_revisions": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.eps_revisions.to_dict().items()}
                if data.eps_revisions is not None
                else "No EPS revisions data available"
            ),
            "growth_estimates": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.growth_estimates.to_dict().items()}
                if data.growth_estimates is not None
                else "No growth estimate data available"
            ),
            "recommendations": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.recommendations.to_dict().items()}
                if data.recommendations is not None
                else "No recommendations data available"
            ),
            "recommendations_summary": (    
                {str(key): convert_timestamp_to_string(value) for key, value in data.recommendations_summary.to_dict().items()}
                if data.recommendations_summary is not None
                else "No recommendations summary data available"
            ),
            "upgrades_downgrades": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.upgrades_downgrades.to_dict().items()}
                if data.upgrades_downgrades is not None
                else "No upgrades/downgrades data available"
            ),
            "sustainability": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.sustainability.to_dict().items()}
                if data.sustainability is not None
                else "No sustainability data available"
            ),
            "analyst_price_targets": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.analyst_price_targets.items()}
                if data.analyst_price_targets is not None
                else "No analyst price targets data available"
            ),
            "insider-purchases": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.insider_purchases.to_dict().items()}
                if data.insider_purchases is not None
                else "No insider purchases data available"
            ),
            "insider_transactions": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.insider_transactions.to_dict().items()}
                if data.insider_transactions is not None
                else "No insider transactions data available"
            ),
            "insider_roster_holders": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.insider_roster_holders.to_dict().items()}
                if data.insider_roster_holders is not None
                else "No insider roast holders data available"
            ),
            "major_holders": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.major_holders.to_dict().items()}
                if data.major_holders is not None
                else "No major holders data available"
            ),
            "institutional_holders": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.institutional_holders.to_dict().items()}
                if data.institutional_holders is not None
                else "No institutional holders data available"
            ),
            "mutualfund_holders": (
                {str(key): convert_timestamp_to_string(value) for key, value in data.mutualfund_holders.to_dict().items()}
                if data.mutualfund_holders is not None
                else "No mutual fund holders data available"
            ),
        }

        # Serialize the result to JSON format using DateEncoder for date handling
        result[ticker_symbol] = json.loads(json.dumps(analysis_data, cls=DateEncoder))

    except Exception as e:
        result[ticker_symbol] = {"error": str(e)}

    return result


# Example usage
if __name__ == "__main__":

    single_ticker = "AAPL"

    # Balance sheet for a single ticker
    # print("Balance Sheet for Single Ticker:")
    # print(get_balance_sheet_as_json(single_ticker))

    # # Cash flow for a single ticker
    # print("\nCash Flow for Single Ticker:")
    # print(get_cash_flow_as_json(single_ticker))

    # # Historical data for single ticker
    # print("\nHistorical Data for Single Ticker:")
    # print(get_historical_data(single_ticker))

    # # Historical data for single ticker with parameters
    # print("\nHistorical Data for Single Ticker:")
    # print(get_historical_data_as_json(single_ticker, interval="1h", period="1mo"))

    # # Sector / Industry information for single ticker
    # print("\nSector and Industry Data for Single Ticker:")
    # print(get_sector_and_industry_as_json(single_ticker))

    # # Calendar information for single ticker
    # print("\nCalendar Information for Single Ticker:")
    # print(get_calendar_as_json(single_ticker))

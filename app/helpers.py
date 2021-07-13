import os
import requests

def check_registration_valid(username, password, confirmation='none'):

  if not username and not password:
    return 'Ooops please enter a username and password'
  if not username:
    return 'Oops missing a username - please try again'
  if not password:
    return 'Oops missing a password - please try again'
  if not len(password) >= 8:
    return 'Please ensure your password is at least 8 characters long'
  if confirmation == 'none':
    pass
  if not confirmation and not confirmation == 'none':
    return 'Oops missing password confirmation - please try again'
  if not confirmation == 'none':
    if not password == confirmation:
      return 'Oops your confirmation password does not match - please try again'

def formatDollar(value):
  return f"${value:,.2f}"

def formatPercentage(value):
  return f"{value:,.2f}%"

def getLogo(symbol):
  try:
    api_key_test = os.environ.get('API_KEY_TEST')
    # url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
    url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/logo/?token={api_key_test}'

    response = requests.get(url)
  except requests.RequestException:
        return None

  #parse data
  try:
    img_url = response.json()
    return img_url
  except (KeyError, TypeError, ValueError):
        return None


def getListMostActive():
  # cloud.iexapis.com ~ MOST ACTIVE ~
    # Contact API and convert into python dictionary
    try:
        api_key_test = os.environ.get('API_KEY_TEST')
        # url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
        url = f'https://sandbox.iexapis.com/stable/stock/market/list/mostactive/?token={api_key_test}'
        response = requests.get(url)
        # response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        list = response.json()
        data = []

        for item in range(len(list)):
          data.append({
            "name": list[item]["companyName"],
            "symbol": list[item]["symbol"],
            # "img_url": getLogo(list[item]["symbol"]),
            "price": list[item]["latestPrice"],
            "changePercentage": (list[item]["changePercent"] * 100),
            "changePrice": list[item]["change"],
          })
        
        return data
    except (KeyError, TypeError, ValueError):
        return None

def getListGainers():
  # cloud.iexapis.com ~ MOST ACTIVE ~
    # Contact API and convert into python dictionary
    try:
        api_key_test = os.environ.get('API_KEY_TEST')
        # url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
        url = f'https://sandbox.iexapis.com/stable/stock/market/list/gainers/?token={api_key_test}'
        response = requests.get(url)
        # response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        list = response.json()
        data = []

        for item in range(len(list)):
          data.append({
            "name": list[item]["companyName"],
            "symbol": list[item]["symbol"],
            # "img_url": getLogo(list[item]["symbol"]),
            "price": list[item]["latestPrice"],
            "changePercentage": (list[item]["changePercent"] * 100),
            "changePrice": list[item]["change"],
          })
        
        return data
    except (KeyError, TypeError, ValueError):
        return None

def getListLosers():
  # cloud.iexapis.com ~ MOST ACTIVE ~
    # Contact API and convert into python dictionary
    # "img_url": getLogo(list[item]["symbol"]),
    try:
        api_key_test = os.environ.get('API_KEY_TEST')
        # url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
        url = f'https://sandbox.iexapis.com/stable/stock/market/list/losers/?token={api_key_test}'
        response = requests.get(url)
        # response.raise_for_status()
    except requests.RequestException:
        return None

    # Parse response
    try:
        list = response.json()
        data = []

        for item in range(len(list)):
          data.append({
            "name": list[item]["companyName"],
            "symbol": list[item]["symbol"],
            "price": list[item]["latestPrice"],
            "changePercentage": (list[item]["changePercent"] * 100),
            "changePrice": list[item]["change"],
            "marketCap":list[item][""]
          })
        
        return data
    except (KeyError, TypeError, ValueError):
        return None

def getCryto(symbol):
  try:
    # api_key_test: os.environ.get('API_KEY_TEST')
    url = f'https://sandbox.iexapis.com/stable/crypto/{symbol}/price/?token={os.environ.get("API_KEY_TEST")}'

    response = requests.get(url)
  except requests.RequestException:
    return None
  
  #parse data
  try:
    return response.json()
  except(KeyError, TypeError, ValueError):
    return None
    
def getCompanyDetails(symbol):
  # cloud.iexapis.com ~ company details  ~
    # Contact API and convert into python dictionary
    try:
        api_key_test = os.environ.get('API_KEY_TEST')
        # url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
        url = f'https://sandbox.iexapis.com/stable/stock/{symbol}/company/?token={api_key_test}'

        response = requests.get(url)
    except requests.RequestException:
        return None

    # Parse response
    try:
        data = response.json()
        return data
    except (KeyError, TypeError, ValueError):
      return None

def getQuote(symbol):
  # cloud.iexapis.com ~ quote ~
  try: 
    api_key_test = os.environ.get('API_KEY_TEST')
    url = f'https://sandbox.iexapis.com/stable/{symbol}/quote/?token={api_key_test}'

    response = requests.get(url)
  except requests.RequestException:
    return None
  
  # parse response
  try:
    data = response.json()
    return {
      "symbol": data["symbol"],
      "exchange": data["primaryExchange"],
      "latestPrice": data["latestPrice"],
      "latestTime": data["latestTime"],
      "openPrice":data["open"],
      "closePrice": data["previousClose"],
      "marketCap": data["marketCap"],
      "week52High": data["week52High"],
      "week52Low": data["week52Low"]
    }
  except(KeyError, TypeError, ValueError):
    return None
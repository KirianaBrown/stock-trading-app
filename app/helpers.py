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

def getLogo(symbol):
  try:
    api_key_test = os.environ.get('API_KEY_TEST')
    # url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
    url = f'https://sandbox.iexapis.com/stable/stock/market/list/mostactive/?token={api_key_test}'
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
            "img_url": getLogo(list[item]["symbol"]),
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
            "img_url": getLogo(list[item]["symbol"]),
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
            "img_url": getLogo(list[item]["symbol"]),
            "price": list[item]["latestPrice"],
            "changePercentage": (list[item]["changePercent"] * 100),
            "changePrice": list[item]["change"],
          })
        
        return data
    except (KeyError, TypeError, ValueError):
        return None
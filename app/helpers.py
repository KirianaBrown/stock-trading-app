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


def getTop10():
  # cloud.iexapis.com
    # Contact API and convert into python dictionary
    try:
        api_key= os.environ.get('API_KEY')
        url = f'https://cloud.iexapis.com/stable/stock/market/list/mostactive/?token={api_key}'
        response = requests.get(url)
        response.raise_for_staus()
    except requests.RequestException:
        return None

    # Parse response
    try:
        list = response.json()
        return {
            "name": list["companyName"],
            "price": float(list["latestPrice"]),
            "symbol": list["symbol"],
            "changePercentage": float(list['changePercent']),
            "changeValue": float(list['change'])
        }
    except (KeyError, TypeError, ValueError):
        return None
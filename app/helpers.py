def check_registration_valid(username, password, confirmation):

  if not username and not password:
    return 'Ooops please enter a username and password'
  if not username:
    return 'Oops missing a username - please try again'
  if not password:
    return 'Oops missing a password - please try again'
  if not len(password) >= 8:
    return 'Please ensure your password is at least 8 characters long'
  if not password == confirmation:
    return 'Oops your confirmation password does not match - please try again'


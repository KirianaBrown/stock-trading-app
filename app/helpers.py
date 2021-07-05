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


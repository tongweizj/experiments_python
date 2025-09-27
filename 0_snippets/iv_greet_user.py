import json

def get_stored_username():
  """如果已经存储用户名，就读取它"""
  filename = 'username.json'
  try:
    with open(filename) as f:
      username = json.load(f)
  except FileNotFoundError:
    return None
  else:
    return username

def get_new_username():
  """提示用户输入用户名"""
  username =  input("what is your name?")
  filename = "username.json"
  with open(filename,'w') as f:
    json.dump(username, f)
  
  return username

def greet_user():
  """问候用户，并指出其姓名"""
  username = get_stored_username()
  if username:
    print(f"Welcome back, {username}")
  else:
    username = get_new_username()
    print(f"We'll remember you whe you come back, {username}")

greet_user()

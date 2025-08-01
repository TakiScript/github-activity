import requests
import json

url: str = "https://api.github.com/users/TakiMoretti/events/public"

response = requests.get(url)
first_five: dict = response.json()[0:5]

pretty: str = json.dumps(first_five, indent=4)

events: dict = first_five

for event in events:
  
  type: str = event["type"]
  print("Event type is: {}".format(type))


"""
def validate_input(user_input):
  try:
    if " " in user_input.strip():
      return True
    else:
      return False
  except:
    print("Invalid input.")


def main():
  while True: 
    user_input: str = input("github-activity > ")
    
    print(f'You said: {user_input}')
    print(f"{validate_input(user_input)}")
    
if __name__ == "__main__":
  main()
"""

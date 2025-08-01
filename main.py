import requests
import json

base_url: str = "https://api.github.com/users/{username}/events/public"

def fetch_data(username: str):
  final_url: str = base_url.format(username=username)
  response = requests.get(final_url)
  first_five: list = response.json()[0:5]
  
  pretty: str = json.dumps(first_five, indent=4)
  
  events: list = first_five
  
  for event in events:
     type: str = event.get("type", "N/A")
    
     if type == "PushEvent":
       print(f"-  A commit has been pushed to a repository.")
     elif type == "CreateEvent":
       print(f"-  A branch or tag has been created.")
     elif type == "ForkEvent":
       print(f"-  A repository has been forked.")
     elif type == "WatchEvent":
       print(f"-  A user has starred a repository.")
     elif type == "PullRequestEvent":
       print(f"-  A pull request has been opened, closed, or merged.")
     elif type == "IssuesEvent":
       print(f"-  An issue has been opened, closed, or reopened.")
     elif type == "IssueCommentEvent":
       print(f"-  A comment has been added to an issue or pull request.")
     else:
       print(f"Unknown type: {type}")
  
def validate_input(user_input):
  try:
    if " " in user_input.strip():
      return False
    else:
      return True
  except:
    print("Invalid input.")


def main():
  while True: 
    user_input: str = input("github-activity > ")
    
    print(f'You said: {user_input}')
    
    validate_input(user_input)
    
    username: str = user_input.strip()
    
    fetch_data(username)
    
if __name__ == "__main__":
  main()

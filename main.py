import json
import requests

BASE_URL: str = "https://api.github.com/users/{username}/events/public"
AMOUNT_TO_GET: int = 10

def fetch_data(username: str):
  final_url: str = BASE_URL.format(username=username)
  response = requests.get(final_url)
  first_few: list = response.json()[0:AMOUNT_TO_GET]
  
  pretty: str = json.dumps(first_few, indent=4)
  
  events: list = first_few
  
  for event in events:
     event_type: str = event.get("type", "Not found")
     repo_name: str = event.get("repo").get("name")
     action_type: str = event.get("payload").get("action")
     ref: str = event.get("payload").get("ref")
     ref_type: str = event.get("payload").get("ref_type")
    
     if event_type == "PushEvent":
       print(f"-  A commit has been pushed to {repo_name}")
     
     elif event_type == "CreateEvent":
       if ref_type == "repository":
         print(f"-  Created a repo {repo_name}")
       
       elif ref_type == "branch":
         print(f"-  A branch named {ref} created at {repo_name}")
     
     elif event_type == "ForkEvent":
       print(f"-  Forked a repo {repo_name}")
     
     elif event_type == "WatchEvent":
       print(f"-  Starred a repository {repo_name}")
     
     elif event_type == "PullRequestEvent":
       print(f"-  {action_type.capitalize()} a pull request at {repo_name}")
     
     elif event_type == "IssuesEvent":
       print(f"-  An issue has been opened, closed, or reopened at {repo_name}")
     
     elif event_type == "IssueCommentEvent":
       print(f"-  A comment was added at {repo_name}")
     
     elif event_type == "ReleaseEvent":
       print(f"-  {action_type.capitalize()} a release at {repo_name}")
       
     elif event_type == "DeleteEvent":
       print(f"-  A {ref_type} named {ref} was deleted at {repo_name}")
       
     else:
       print(f"Unknown type: {event_type}")
  
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
    validate_input(user_input)
    username: str = user_input.strip()
    
    fetch_data(username)
    
if __name__ == "__main__":
  main()

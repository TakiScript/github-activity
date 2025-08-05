import requests
import json

base_url: str = "https://api.github.com/users/{username}/events/public"

def fetch_data(username: str):
  final_url: str = base_url.format(username=username)
  response = requests.get(final_url)
  first_few: list = response.json()[0:5]
  
  pretty: str = json.dumps(first_few, indent=4)
  
  events: list = first_few
  
  for event in events:
     event_type: str = event.get("type", "N/A")
    
     if event_type == "PushEvent":
       repo_name: str = event.get("repo").get("name")
       print(f"-  A commit has been pushed to {repo_name}")
     
     elif event_type == "CreateEvent":
       if event.get('payload')["ref_type"] == "repository":
         print(f"-  Created a repo {event.get('repo').get('name')}")
       
       elif event.get('payload')["ref_type"] == "branch":
         print(f"-  Created a branch {event.get('payload').get('ref')} at {event.get('repo').get('name')}")
     
     elif event_type == "ForkEvent":
       print(f"-  A repository has been forked.")
     
     elif event_type == "WatchEvent":
       print(f"-  Starred a repository {event.get('repo').get('name')}")
     
     elif event_type == "PullRequestEvent":
       print(f"-  A pull request has been opened, closed, or merged.")
     
     elif event_type == "IssuesEvent":
       print(f"-  An issue has been opened, closed, or reopened.")
     
     elif event_type == "IssueCommentEvent":
       print(f"-  A comment has been added to an issue or pull request.")
     
     elif event_type == "ReleaseEvent":
       repo_name: str = event.get("repo").get("name")
       release_type: str = event.get("payload").get("action")
       print(f"-  {release_type.capitalize()} a release at {repo_name}")
     
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

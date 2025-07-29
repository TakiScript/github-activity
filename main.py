def validate_input(user_input):
  try:
    if " " in user_input:
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

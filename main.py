import requests
import json
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

url = "https://emkc.org/api/v2/piston/execute"

def run_code(source_code, language, version):
    payload = {
        "language": language,
        "version": version,
        "files": [
            {
                "content": source_code
            }
        ],
        "args": [],
        "stdin": "",
        "log": 0
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Request failed with status code {response.status_code}"}

def get_user_choice():
    print(Fore.CYAN + "Choose a language to run your code:")
    print(Fore.GREEN + "1. Python 3.10.0")
    print(Fore.YELLOW + "2. Dart 2.19.6")

    choice = input(Fore.CYAN + "Enter 1 for Python or 2 for Dart: ")
    if choice == "1":
        return "python", "3.10.0"
    elif choice == "2":
        return "dart", "2.19.6"
    else:
        print(Fore.RED + "Invalid choice. Defaulting to Python.")
        return "python", "3.10.0"

language, version = get_user_choice()

print(Fore.CYAN + f"\nYou chose {language.capitalize()} version {version}.")
print(Fore.CYAN + "Enter your code (press Enter twice to run):\n")

user_code = []
while True:
    line = input()
    if line == "":
        break
    user_code.append(line)

source_code = "\n".join(user_code)

response = run_code(source_code, language, version)

if 'run' in response:
    output = response['run']['output']
    if output:
        print(Fore.GREEN + f"\nOutput:\n{output}")
    else:
        print(Fore.YELLOW + "\nNo output.")
else:
    print(Fore.RED + "Error in response:", response)

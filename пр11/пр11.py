import requests
import json
from pprint import pprint

username = "Ansible"
url = f"https://api.github.com/users/{username}"
# делаем запрос и возвращаем json
user_data1 = requests.get(url).json()

print(user_data1)
print('-'*25)
s1 = json.dumps(user_data1)
user_data = json.loads(s1)
info = {
        'company'   : (user_data["company"]   ),
        'created_at': (user_data["created_at"]),
        'email'     : (user_data["email"]     ),
        'id'        : (user_data["id"]        ),
        'name'      : (user_data["name"]      ),
        'url'       : (user_data["url"]       )
        }
pprint(info)

with open('Json.txt', 'w') as file_json:
  json.dump(info,file_json)

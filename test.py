import Jamf
import json


USERID=""
PASSWORD=""
COMPANY=""


jamf = Jamf.Computer.Groups(COMPANY)
jamf.login(USERID, PASSWORD)


print("-=" * 40)
print("GET SMART COMPUTER GROUPS")
response = jamf.get()
print(json.dumps(response, indent=4))
print("-=" * 40)
print("CREATE SMART COMPUTER GROUP")
payload = {
    "computer_group": {
        "name": "TEST JAMF SMART GROUP",
        "is_smart": "true",
        "site": {
            "id": "-1",
            "name": "None"
        },
        "criteria": {
            "size": "2",
            "criterion": [
                {
                    "name": "Operating System Version",
                    "priority": "0",
                    "and_or": "and",
                    "search_type": "like",
                    "value": "10.14",
                    "opening_paren": "false",
                    "closing_paren": "false"
                },
                {
                    "name": "Operating System Version",
                    "priority": "1",
                    "and_or": "and",
                    "search_type": "is not",
                    "value": "10.14.3",
                    "opening_paren": "false",
                    "closing_paren": "false"
                }
            ]
        }
    }
}
response = jamf.post(payload)
print("Create Smart Compuiter Group id [{}]".format(response["computer_group"]["id"]))
print("-=" * 40)
print("UPDATE SMART COMPUTER GROUP")
payload["computer_group"]["name"] = "TEST JAMF SMART COMPUTER GROUP"
response = jamf.put(name="TEST JAMF SMART GROUP", payload=payload)
response = jamf.get(id=response["computer_group"]["id"])
print(json.dumps(response, indent=4))
print("Update Smart Compuiter Group id [{}]".format(response["computer_group"]["id"]))
print("-=" * 40)
print("DELETE SMART COMPUTER GROUP")
response = jamf.delete(name="TEST JAMF SMART COMPUTER GROUP")
print("Delete Smart Compuiter Group id [{}]".format(response["computer_group"]["id"]))

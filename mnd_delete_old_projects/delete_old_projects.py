import requests
import json
import pytz
import dateparser
from datetime import datetime

def main():
    #Declare API information
    api_request = {
        "requestType": "getAllProducts",
        "userKey": "",
        "orgToken": ""
    }

    request_suffix = "/api/v1.3"
    request_headers = {"Content-Type": "application/json"}

    environment = input("Environment URL the Organization is in: ")
    api_request["orgToken"] = input("API Key of the Organization: ")
    api_request["userKey"] = input("Organization Administrator User Key: ")
    days = int(input("Minimum age of the projects to be deleted (in days): "))

    #Get the products in the organization
    products_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))

    products_json = json.loads(products_str.content)
    product_list = []
    print("Getting Products")
    for product in products_json['products']:
        product_list.append({"productName": product['productName'], "productToken": product['productToken']})

    print(f"Number of Products: {len(product_list)}")
        

    del api_request['orgToken']

    print()
    #Get the projects in the organization
    api_request["requestType"] = "getAllProjects"

    print("Getting Projects")
    for product in product_list:
        api_request["productToken"] = product["productToken"]
        projects_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
        projects_json = json.loads(projects_str.content)
        product["projects"] = projects_json["projects"]
        print(f"{product['productName']} - Number of Projects: {len(product['projects'])}")
        
        
    print("\nGetting Creation Dates")
    #Get project vitals for every project
    del api_request["productToken"]
    api_request["requestType"] = "getProjectVitals"
    for product in product_list:
        for project in product["projects"]:
            api_request["projectToken"] = project["projectToken"]
            
            project_vitals_str = requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
            project_vitals_obj = json.loads(project_vitals_str.content)
            project["creationDate"] = project_vitals_obj["projectVitals"][0]["creationDate"]


    print("\nDeleting projects based off of creation date.")
    api_request["requestType"] = "deleteProject"
    utc_tz = pytz.timezone('UTC')
    now = datetime.now(utc_tz)
    for product in product_list:
        api_request["productToken"] = product["productToken"]
        
        for project in product["projects"]:
            creation_date = dateparser.parse(project["creationDate"])
            if (now - creation_date).days >= days:
                api_request["projectToken"] = project["projectToken"]
                requests.post(f"{environment}{request_suffix}", headers=request_headers, data=json.dumps(api_request))
                print(f"Deleted project: {project['projectName']}")

if __name__ == "__main__":
    main()
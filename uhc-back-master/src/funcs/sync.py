import requests
import json

url = "https://api.excelhire.com/api/open-link-careerportal/get_careerportal_jobs"

payload = json.dumps({
  "organization_id": "6830c7659de9160fef969b86",
  "cp_token": "U2FsdGVkX19cctRQsv6CdzEM759t2bMUIZDY4bohEZsUATYIwjvVJB%2BKqQ4O%2Fgnz",
  "include_candidate_pay_rate": True
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

jobs = response.json().get("data", []).get("jobs", [])

ids = [job["_id"] for job in jobs]

jds = []
for job in jobs:
    url = "https://api.excelhire.com/api/open-link-job/get_open_job_details"

    payload = json.dumps({
    "job_id": f"{job["_id"]}",
    "organization_id": "6830c7659de9160fef969b86",
    "cp_token": "U2FsdGVkX19cctRQsv6CdzEM759t2bMUIZDY4bohEZsUATYIwjvVJB%2BKqQ4O%2Fgnz"
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    job_details = response.json().get("data", {})
    job_details["candidate_pay_rate"] = job.get("candidate_pay_rate", None)
    job_details["candidate_pay_rate_currency"] = job.get("candidate_pay_rate_currency", None)
    job_details["employment_type"] = job.get("employment_type", None)
    if job_details:
        jds.append(job_details)

# insert all jds into mongodb 

import pymongo
client = pymongo.MongoClient("mongodb+srv://admin:admin123@uhc.sip2665.mongodb.net/?retryWrites=true&w=majority&appName=uhc")
db = client["uhc"]
collection = db["jobs"]

# Clear the collection before inserting new jobs
collection.delete_many({})
# Insert the new job details
if jds:
    # Ensure that jds is not empty before inserting
    print(f"Inserting {len(jds)} job documents into the collection.")
else:
    print("No job documents to insert.")

collection.insert_many(jds)
print("Jobs inserted successfully.")
import pymongo
import pymongo.errors
import sys


try:
    client = pymongo.MongoClient("mongodb+srv://admin:admin123@uhc.sip2665.mongodb.net/?retryWrites=true&w=majority&appName=uhc")
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB: {e}")
    client = None

try:
    db = client["uhc"]
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not access database: {e}")
    db = None
    sys.exit()
    

def get_collection(collection_name):
    """
    Returns the specified collection from the database.
    """
    if db is not None and collection_name in db.list_collection_names():
        return db[collection_name]
    else:
        print("No database available.")
        return None
    
def close_client():
    """
    Closes the MongoDB client connection.
    """
    if client:
        client.close()
    else:
        print("No MongoDB client to close.")

def get_all_documents(collection_name):
    """
    Returns all documents from the specified collection.
    """
    if collection_name is not None:
        return list(collection_name.find())
    else:
        print("No collection available.")
        return []

def get_jobs(keywords="", location=""):
    """
    Retrieves all job documents from the 'jobs' collection.
    """
    collection = get_collection("jobs")  # Change to your collection name
    
    if collection is not None:
        documents = get_all_documents(collection)

        if keywords == "" and location == "":
            return documents
        
    # Filter jobs based on keywords if provided
        filtered_jobs_keywords = []
        filtered_jobs_location = []
        filtered_jobs = []
        keywords = keywords.lower().split()
        location = location.lower()
        for job in documents:
            job_title = job.get("job_title", "").lower()
            job_city = job.get("city", "").lower()
            job_state = job.get("state", "").lower()

            for keyword in keywords:
                if keyword in job_title:
                        filtered_jobs_keywords.append(job)
                        break
            if location:
                if location in job_city or location in job_state:
                    filtered_jobs_location.append(job)

        if filtered_jobs_keywords and filtered_jobs_location:
            filtered_jobs = [job for job in filtered_jobs_keywords if job in filtered_jobs_location]
        elif filtered_jobs_keywords:
            filtered_jobs = filtered_jobs_keywords
        elif filtered_jobs_location:
            filtered_jobs = filtered_jobs_location
        else:
            filtered_jobs = []

        return filtered_jobs


def get_job_by_id(job_code):
    """
    Retrieves a job document by its ID from the 'jobs' collection.
    """
    collection = get_collection("jobs")  # Change to your collection name
    
    if collection is not None:
        job = collection.find_one({"job_code": job_code})
        return job
    else:
        return None

if __name__ == "__main__":
    jobs = get_jobs()
    if jobs:
        print("Retrieved jobs:")
        for job in jobs:
            print(job['job_code'])

    print("MongoDB client connection closed.")
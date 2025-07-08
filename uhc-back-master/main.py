from flask import Flask, request, jsonify

app = Flask(__name__)

# route to get a list of 20 jobs
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    # Simulate fetching data
    jobs = {
        "message": "Hello, World!",
        "status": "success"
    }
    return jsonify(jobs)

# route to get a specific job by ID
@app.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    # Simulate fetching a specific job
    job = {
        "id": job_id,
        "title": f"Job {job_id}",
        "description": f"Description for job {job_id}"
    }
    return jsonify(job)

# route to send job application data 
@app.route('/api/jobs/<int:job_id>/apply', methods=['POST'])
def apply_job(job_id):
    data = request.json
    # Simulate saving the application data
    application = {
        "job_id": job_id,
        "applicant_name": data.get("name"),
        "applicant_email": data.get("email"),
        "status": "Application submitted"
    }
    return jsonify(application), 201
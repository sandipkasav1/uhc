from flask import Blueprint, request

bp = Blueprint("api", __name__)

@bp.route("/status")
def status():
    return {"status": "ok"}, 200

@bp.route("/post_job", methods=["POST"])
def post_job():
    # Placeholder for job posting logic
    return {"message": "Job posted successfully"}, 201

@bp.route("/get_trending_jobs", methods=["GET"])
def get_trending_jobs():
    # Placeholder for retrieving jobs logic
    return {"jobs": []}, 200

@bp.route("/get_job/<int:job_id>", methods=["GET"])
def get_job(job_id):
    # Placeholder for retrieving a specific job by ID
    return {"job_id": job_id, "title": "Sample Job"}, 200

@bp.route("/search_jobs", methods=["GET"])
def search_jobs():
    # Placeholder for searching jobs logic
    query = " ".join(request.args.getlist('query'))
    return {"jobs": [], "query": query}, 200
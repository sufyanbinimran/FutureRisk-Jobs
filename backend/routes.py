from flask import Blueprint, request, jsonify
from models import Job, db
from sqlalchemy import desc

api = Blueprint("api", __name__)

@api.route("/jobs", methods=["GET"])
def get_jobs():
    query = Job.query

    # Filters
    job_type = request.args.get("job_type")
    location = request.args.get("location")
    tag = request.args.get("tag")
    sort = request.args.get("sort")

    if job_type:
        query = query.filter_by(job_type=job_type)
    if location:
        query = query.filter_by(location=location)
    if tag:
        query = query.filter(Job.tags.like(f"%{tag}%"))

    if sort == "posting_date_desc":
        query = query.order_by(desc(Job.posting_date))
    elif sort == "posting_date_asc":
        query = query.order_by(Job.posting_date)

    jobs = query.all()
    return jsonify([job_to_dict(job) for job in jobs])

@api.route("/jobs/<int:id>", methods=["GET"])
def get_job(id):
    job = Job.query.get(id)
    if job:
        return jsonify(job_to_dict(job))
    return jsonify({"error": "Job not found"}), 404

@api.route("/jobs", methods=["POST"])
def create_job():
    data = request.json
    required = ["title", "company", "location", "posting_date", "job_type"]
    if not all(field in data and data[field] for field in required):
        return jsonify({"error": "Missing required fields"}), 400

    job = Job(**data)
    db.session.add(job)
    db.session.commit()
    return jsonify(job_to_dict(job)), 201

@api.route("/jobs/<int:id>", methods=["PUT", "PATCH"])
def update_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    data = request.json
    for field in ["title", "company", "location", "posting_date", "job_type", "tags"]:
        if field in data:
            setattr(job, field, data[field])

    db.session.commit()
    return jsonify(job_to_dict(job))

@api.route("/jobs/<int:id>", methods=["DELETE"])
def delete_job(id):
    job = Job.query.get(id)
    if not job:
        return jsonify({"error": "Job not found"}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({"message": "Job deleted"}), 200

def job_to_dict(job):
    return {
        "id": job.id,
        "title": job.title,
        "company": job.company,
        "location": job.location,
        "posting_date": job.posting_date,
        "job_type": job.job_type,
        "tags": job.tags,
    }

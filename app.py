
from flask import Flask, render_template, jsonify, request, send_file
from werkzeug.utils import secure_filename
import csv
from datetime import date
from pathlib import Path
import tempfile
import os
import pandas as pd
from utils.csv_validator import validate_csv
from services.s3_service import upload_file_to_s3

app = Flask(__name__)

BASE_DIR = Path(__file__).parent
CSV_FILE = BASE_DIR / "data.csv"
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json(silent=True) or {}
    count = data.get("count", 3)

    if not isinstance(count, int) or isinstance(count, bool) or not 1 <= count <= 1000:
        return jsonify({"error": "Enter a number from 1 to 1000"}), 400

    with CSV_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Value", "Date"])

        for i in range(1, count + 1):
            writer.writerow([i, f"Sample {i}", i * 100, date.today()])

    return jsonify({
        "message": f"Generated {count} records",
        "count": count
    })


@app.route("/api/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")

    if not uploaded_file or not uploaded_file.filename:
        return jsonify({"error": "Please select a CSV file."}), 400

    if not uploaded_file.filename.lower().endswith(".csv"):
        return jsonify({"error": "Only CSV files are allowed."}), 400

    safe_name = secure_filename(uploaded_file.filename)

    if not safe_name:
        return jsonify({"error": "Invalid filename."}), 400

    temp_path = None

    try:
        with tempfile.NamedTemporaryFile(
            mode="wb", suffix=".csv", delete=False, dir=BASE_DIR
        ) as temp_file:
            temp_path = Path(temp_file.name)
            uploaded_file.save(temp_file)

        result = validate_csv(temp_path)

        if not result["valid"]:
            return jsonify({"error": "; ".join(result["errors"])}), 400

        # Keep a local copy for the dashboard
        temp_path.replace(CSV_FILE)
        temp_path = None

        # Upload to S3 only when a bucket is configured
        if os.getenv("AWS_S3_BUCKET"):
            s3_result = upload_file_to_s3(CSV_FILE, safe_name)

            if not s3_result["success"]:
                return jsonify({
                    "message": "CSV loaded locally, but S3 upload failed.",
                    "warning": s3_result["message"],
                    "rows": result["rows"],
                    "columns": result["columns"]
                }), 200

            return jsonify({
                "message": "CSV validated and uploaded to AWS S3 successfully.",
                "rows": result["rows"],
                "columns": result["columns"]
            })

        return jsonify({
            "message": "CSV validated and loaded locally. AWS S3 is not configured yet.",
            "rows": result["rows"],
            "columns": result["columns"]
        })

    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)
@app.route("/api/clean/missing", methods=["POST"])
def clean_missing():
    data = request.get_json(silent=True) or {}
    fill_value = data.get("fill_value", "Unknown")

    if not isinstance(fill_value, str):
        return jsonify({"error": "Fill value must be text."}), 400

    if not CSV_FILE.exists():
        return jsonify({"error": "No CSV file available."}), 404

    try:
        df = pd.read_csv(CSV_FILE, keep_default_na=False)
        missing_before = int((df == "").sum().sum())
        df = df.replace(r"^\s*$", fill_value, regex=True)
        df.to_csv(CSV_FILE, index=False)

        return jsonify({
            "message": f"Filled {missing_before} missing cells.",
            "cleaned": missing_before
        })
    except Exception as error:
        return jsonify({"error": str(error)}), 400
@app.route("/api/clean/duplicates", methods=["POST"])
def remove_duplicates():
    if not CSV_FILE.exists():
        return jsonify({"error": "No CSV file available."}), 404

    try:
        df = pd.read_csv(CSV_FILE)
        before = len(df)
        df = df.drop_duplicates()
        removed = before - len(df)
        df.to_csv(CSV_FILE, index=False)

        return jsonify({
            "message": f"{removed} duplicate rows removed.",
            "removed": removed,
            "remaining": len(df)
        })
    except Exception as error:
        return jsonify({"error": str(error)}), 400
@app.route("/api/data")
def get_data():
    if not CSV_FILE.exists():
        return jsonify([])

    with CSV_FILE.open("r", newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))

    return jsonify(rows)


@app.route("/api/download")
def download():
    if not CSV_FILE.exists():
        return jsonify({"error": "Generate or upload a CSV first."}), 404

    return send_file(CSV_FILE, as_attachment=True)


@app.errorhandler(413)
def file_too_large(error):
    return jsonify({"error": "File exceeds the 10 MB limit."}), 413


if __name__ == "__main__":
    app.run(debug=True)

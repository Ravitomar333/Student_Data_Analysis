from flask import Flask, render_template, request, send_file, redirect, url_for
import os
from analysis import analyze

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
DOWNLOAD_FOLDER = "downloads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

analysis_result = None


# -----------------------------
# Home Page (Upload CSV)
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():
    global analysis_result

    # Clear previous analysis every time user comes to home
    analysis_result = None

    # Delete uploaded CSV files
    if os.path.exists(UPLOAD_FOLDER):
        for file in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, file)
            if os.path.isfile(file_path):
                os.remove(file_path)

    if request.method == "POST":

        file = request.files.get("csv_file")

        if file and file.filename != "":

            filepath = os.path.join(
                app.config["UPLOAD_FOLDER"],
                file.filename
            )

            file.save(filepath)

            analysis_result = analyze(filepath)

            return redirect(url_for("dashboard"))

    return render_template("index.html")


# -----------------------------
# Dashboard
# -----------------------------
@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    global analysis_result

    if analysis_result is None:
        return redirect(url_for("home"))

    search_result = None

    if request.method == "POST":

        name = request.form.get("search_name", "").strip().lower()

        for student in analysis_result["students"]:
            if student["Student Name"].strip().lower() == name:
                search_result = student
                break

    return render_template(
        "dashboard.html",
        summary=analysis_result["summary"],
        students=analysis_result["students"],
        charts=analysis_result["charts"],
        search_result=search_result
    )


# -----------------------------
# Download Report
# -----------------------------
@app.route("/download")
def download():
    report_path = os.path.join(DOWNLOAD_FOLDER, "student_result.csv")

    if not os.path.exists(report_path):
        return "No report available yet.", 404

    return send_file(
        report_path,
        as_attachment=True,
        download_name="student_result.csv"
    )


# -----------------------------
# New Analysis
# -----------------------------
@app.route("/new-analysis")
def new_analysis():
    global analysis_result

    analysis_result = None

    # Delete result CSV
    report_path = os.path.join(DOWNLOAD_FOLDER, "student_result.csv")
    if os.path.exists(report_path):
        os.remove(report_path)

    # Delete charts
    chart_folder = "static/charts"

    if os.path.exists(chart_folder):
        for file in os.listdir(chart_folder):
            file_path = os.path.join(chart_folder, file)

            if os.path.isfile(file_path):
                os.remove(file_path)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)

application = app
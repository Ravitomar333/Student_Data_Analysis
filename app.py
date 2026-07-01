from flask import Flask, render_template, request, send_file
import os
from analysis import analyze

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Create uploads folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store analysis results
analysis_result = None


@app.route("/", methods=["GET", "POST"])
def index():
    global analysis_result

    search_result = None

    if request.method == "POST":

        # Upload CSV
        if "csv_file" in request.files:
            file = request.files["csv_file"]

            if file.filename != "":
                filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
                file.save(filepath)

                # Run analysis
                analysis_result = analyze(filepath)

        # Search Student
        if request.form.get("search_name") and analysis_result:

            name = request.form.get("search_name").strip().lower()

            # for student in analysis_result["students"]:
            #     if student["Name"].lower() == name:
            #         search_result = student
            #         break
            for student in analysis_result["students"]:
                 if student["Student Name"].strip().lower() == name:
                  search_result = student
                  break

    return render_template(
        "index.html",
        summary=analysis_result["summary"] if analysis_result else None,
        students=analysis_result["students"] if analysis_result else None,
        charts=analysis_result["charts"] if analysis_result else None,
        search_result=search_result
    )
@app.route("/download")
def download():

    return send_file(
        "student_result.csv",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)

# Render-compatible WSGI entry point
application = app
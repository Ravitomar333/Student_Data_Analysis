import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


def analyze(csv_path):

    # Read CSV
    df = pd.read_csv(csv_path)

    # Subjects
    subjects = ["Math", "English", "Science", "SST", "Hindi"]

    # Total & Average
    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = (df["Total"] / len(subjects)).round(2)

    # Grade Function
    def grade(avg):
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"

    df["Grade"] = df["Average"].apply(grade)

    # Create folders for generated files
    chart_folder = "static/charts"
    report_folder = "downloads"
    os.makedirs(chart_folder, exist_ok=True)
    os.makedirs(report_folder, exist_ok=True)

    # Average Marks of Subjects
    subject_avg = df[subjects].mean()

    # Find Topper and Lowest Performer
    topper = df.loc[df["Average"].idxmax()]
    lowest = df.loc[df["Average"].idxmin()]

    

    # ---------------- Bar Chart ----------------

    plt.figure(figsize=(6,4))
    plt.bar(subject_avg.index, subject_avg.values)
    plt.title("Average Marks by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.tight_layout()
    plt.savefig(f"{chart_folder}/bar.png")
    plt.close()

    # ---------------- Line Chart ----------------

    plt.figure(figsize=(6,4))
    plt.plot(subject_avg.index, subject_avg.values, marker="o")
    plt.title("Subject Performance")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"{chart_folder}/line.png")
    plt.close()

    # ---------------- Pie Chart ----------------

    grades = df["Grade"].value_counts()

    plt.figure(figsize=(5,5))
    plt.pie(
        grades,
        labels=grades.index,
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("Grade Distribution")
    plt.tight_layout()
    plt.savefig(f"{chart_folder}/pie.png")
    plt.close()

    # ---------------- Student Average Chart ----------------

    plt.figure(figsize=(10,5))
    plt.bar(df["Student Name"], df["Average"])
    plt.xticks(rotation=45)
    plt.ylabel("Average Marks")
    plt.title("Student Average Marks")
    plt.tight_layout()
    plt.savefig(f"{chart_folder}/average.png")
    plt.close()

    # Save Result CSV
    report_path = os.path.join(report_folder, "student_result.csv")
    df.to_csv(report_path, index=False)

   
    summary = {

    "total_students": len(df),

    "overall_average": round(df["Average"].mean(), 2),

    "highest_average": round(df["Average"].max(), 2),

    "lowest_average": round(df["Average"].min(), 2),

    "topper_name": topper["Student Name"],
    "topper_percentage": round(topper["Average"], 2),

    "lowest_name": lowest["Student Name"],
    "lowest_percentage": round(lowest["Average"], 2)

}

    # Return everything to Flask
    return {
        "summary": summary,

        "students": df.to_dict(orient="records"),

        "charts": {
            "bar": "charts/bar.png",
            "line": "charts/line.png",
            "pie": "charts/pie.png",
            "average": "charts/average.png"
        }
    }


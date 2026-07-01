# Student Data Analysis

A simple Flask web application for analyzing and visualizing student performance data from CSV files. The app lets users upload student records, process the data, and view insightful charts such as average marks, subject-wise performance, and grade distribution.

## Project Overview

This project is designed to help educators and students quickly analyze academic results. It reads student data from CSV files, calculates important metrics, and displays them through a clean web interface.

## Features

- Upload student data in CSV format
- Analyze student marks and results
- Generate visual charts for better understanding
- Display summary statistics such as average marks and pass/fail status
- Built with Flask for a lightweight web experience

## Technologies Used

- Python
- Flask
- Pandas
- Matplotlib / Seaborn
- HTML, CSS, and JavaScript

## Project Structure

- `app.py` - Main Flask application
- `analysis.py` - Data analysis and processing logic
- `templates/` - HTML templates for the web UI
- `static/` - CSS, JavaScript, and chart images
- `uploads/` - Uploaded CSV files
- `students.csv`, `student2.csv`, `student_result.csv` - Sample data files

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/Ravitomar333/Student_Data_Analysis.git
   ```

2. Navigate into the project folder
   ```bash
   cd Student_Data_Analysis
   ```

3. Create and activate a virtual environment
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

4. Install the required packages
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Start the Flask app with:

```bash
python app.py
```

Then open your browser and visit:

```bash
http://127.0.0.1:5000/
```

## Usage

- Upload a CSV file containing student records
- View generated analysis and charts
- Explore the results through the interactive web interface

## License

This project is open-source and available for educational and personal use.

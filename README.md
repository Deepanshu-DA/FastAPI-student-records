# FastAPI Student Records Application

This is a simple FastAPI application for managing student records. It allows you to view, update, and add student records using a RESTful API.

## Features

- **View Student Record**: Retrieve student records by providing the student ID.
- **Update Student Record**: Update student records by providing the student ID and new data.
- **Add New Student**: Add new student records.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/fastapi-student-records.git
2. Install dependencies:
   
   ```bash
   pip install -r requirements.txt
3. Run the application:
   ```bash
   uvicorn main:app --reload

# Usage

1. Access the application at [http://localhost:8000](http://localhost:8000).
2. Use the provided endpoints to interact with the application:
   - `/`: Home page (redirects to the main HTML page).
   - `/post_comment/{student_id}`: View student record by student ID.
   - `/update_comment/{student_id}`: Update student record by student ID.
   - `/add_student`: Add a new student record.

# Project Structure

- `main.py`: Contains the FastAPI application code.
- `data/data.csv`: CSV file containing student records.
- `static/`: Directory containing static files (HTML, CSS, JavaScript).
- `requirements.txt`: List of Python dependencies.

# Contributing

Contributions are welcome! Please feel free to fork the repository, make changes, and submit a pull request.

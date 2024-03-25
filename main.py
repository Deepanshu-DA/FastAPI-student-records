from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import csv
import uvicorn

class CheckAPIPost(BaseModel):
    Name: str
    Course: str
    Gender: str
    Age: int
    Duration: str
    Payment_Mode: str
    Fees: str
    Amount_Paid_or_Remaining: str

app = FastAPI()

valuesToBeStored = {}

def load_data_from_csv():
    with open("data/data.csv", mode='r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student_id = int(row['Student_ID'])
            valuesToBeStored[student_id] = {
                "Student_ID": student_id,
                "Name": row['Name'],
                "Course": row['Course'],
                "Gender": row['Gender'],
                "Age": int(row['Age']),
                "Duration": row['Duration'],
                "Payment_Mode": row['Payment_Mode'],
                "Fees": row['Fees'],
                "Amount_Paid_or_Remaining": row['Amount_Paid_or_Remaining']
            }

load_data_from_csv()

# Serve static files (HTML, CSS, JavaScript) from the 'static' directory
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get('/')
def get_home_page():
    # Redirect to the main HTML page
    return JSONResponse(content={"message": "Redirecting to home page"}, status_code=302, headers={"Location": "/static/home.html"})

@app.get('/post_comment/{student_id}')
def take_comment(student_id: int):
    """
    Takes a Student ID and returns corresponding stored values.
    """
    try:
        data = valuesToBeStored[student_id]
        return data
    except KeyError:
        raise HTTPException(status_code=404, detail="Student not found")

@app.put('/update_comment/{student_id}')
def update_comment(student_id: int, new_data: CheckAPIPost):
    """
    Update the data for a given Student ID.
    """
    if student_id not in valuesToBeStored:
        raise HTTPException(status_code=404, detail="Student not found")
    
    valuesToBeStored[student_id].update(new_data.dict())
    
    return JSONResponse(content={"message": "Data updated successfully"})

@app.post('/add_student')
def add_student(new_student: CheckAPIPost):
    """
    Add a new student to the data.
    """
    new_student_id = max(valuesToBeStored.keys()) + 1 if valuesToBeStored else 1
    valuesToBeStored[new_student_id] = {"Student_ID": new_student_id, **new_student.dict()}
    
    return JSONResponse(content={"message": "New student added successfully", "student_id": new_student_id})

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

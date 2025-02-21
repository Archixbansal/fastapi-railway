from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

# Initialize FastAPI app
app = FastAPI()

# Define the request model
class InputData(BaseModel):
    full_name: str
    dob: str  # Expected format: DDMMYYYY
    email: str
    roll_number: str
    data: List[str]  # Mixed list of numbers and alphabets

# Root endpoint (for testing if API is running)
@app.get("/")
def root():
    return {"message": "FastAPI is working!"}

# POST method for processing input data
@app.post("/bfhl")
def process_data(input_data: InputData) -> Dict:
    try:
        # Generate user ID
        user_id = f"{input_data.full_name.lower().replace(' ', '_')}_{input_data.dob}"

        # Separate numbers and alphabets
        numbers = [x for x in input_data.data if x.isdigit()]
        alphabets = [x for x in input_data.data if x.isalpha()]
        
        # Response structure
        response = {
            "is_success": True,
            "user_id": user_id,
            "email": input_data.email,
            "roll_number": input_data.roll_number,
            "numbers": numbers,
            "alphabets": alphabets
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# GET method for returning operation code
@app.get("/bfhl")
def get_operation_code():
    return {"operation_code": 1}


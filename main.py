from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class InputData(BaseModel):
    full_name: str
    dob: str  # Expected format: DDMMYYYY
    email: str
    roll_number: str
    data: List[str]  # Mixed list of numbers and alphabets

@app.post("/bfhl")
def process_data(input_data: InputData) -> Dict:
    try:
        user_id = f"{input_data.full_name.lower().replace(' ', '_')}_{input_data.dob}"
        numbers = [x for x in input_data.data if x.isdigit()]
        alphabets = [x for x in input_data.data if x.isalpha()]
        
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

@app.get("/bfhl")
def get_operation_code() -> Dict:
    return {"operation_code": 1}

#Install: pip install fastapi
#Install: pip install uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Store BMI data in memory using a dictionary
bmi_data = {}

# Pydantic model for request data
class BMIInput(BaseModel):
    height: float
    weight: float

# Pydantic model for response data
class BMIResponse(BaseModel):
    bmi: float

# Generate a unique key for each BMI calculation
def generate_key():
    return str(len(bmi_data) + 1)

# Endpoint to calculate and store BMI
@app.post("/calculate_bmi/", response_model=BMIResponse)
async def calculate_bmi(bmi_input: BMIInput):
    bmi = bmi_input.weight / (bmi_input.height ** 2)
    key = generate_key()
    bmi_data[key] = bmi
    return {"bmi": bmi}

# Endpoint to retrieve BMI using the unique key
@app.get("/get_bmi/{key}", response_model=BMIResponse)
async def get_bmi(key: str):
    if key in bmi_data:
        return {"bmi": bmi_data[key]}
    else:
        raise HTTPException(status_code=404, detail="Key not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

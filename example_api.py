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

# Endpoint to calculate and store BMI
@app.post("/calculate_bmi/", response_model=BMIResponse)
async def calculate_bmi(bmi_input: BMIInput):
    bmi = bmi_input.weight / (bmi_input.height ** 2)
    return {"bmi": bmi}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

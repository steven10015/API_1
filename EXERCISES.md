## Exercises prior to project.

1. Write an API that computes the average speed. The user must pass the distance in *Miles* and the *Time* taken. Using that the API must return the average speed in miles per hours.
2. Write an API that computes the probability of an income be greater than \$1500. Assume that the population follows a Normal Distribution: N($\mu=1000$,$\sigma=500$ ).
3. Consider this API code:
```
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np

app = FastAPI()

# Pydantic model for request data
class VectorsInput(BaseModel):
    vector1: list
    vector2: list

# Pydantic model for response data
class CorrelationResponse(BaseModel):
    correlation: float

# Endpoint to compute the correlation between two vectors
@app.post("/compute_correlation/", response_model=CorrelationResponse)
async def compute_correlation(vectors_input: VectorsInput):
    vector1 = vectors_input.vector1
    vector2 = vectors_input.vector2

    if len(vector1) != len(vector2):
        raise HTTPException(status_code=400, detail="Vector lengths must be the same")

    correlation = np.corrcoef(vector1, vector2)[0, 1]
    return {"correlation": correlation}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

```
Create a python code that sends these two vectors: `[1, 2, 3, 4, 5]` and `[5, 4, 3, 2, 1]` and computes the correlation.

Obs: You must install:
> pip install fastapi

> pip install uvicorn

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# Store word reversals in memory using a dictionary
word_data = {}

# Pydantic model for request data
class WordInput(BaseModel):
    word: str

# Pydantic model for response data
class WordResponse(BaseModel):
    reversed_word: str
    key: str

# Generate a unique key for each word reversal
def generate_key():
    return str(len(word_data) + 1)

# Endpoint to submit a word and get the reversed word with a key
@app.post("/submit_word/", response_model=WordResponse)
async def submit_word(word_input: WordInput):
    word = word_input.word
    reversed_word = word[::-1]  # Reverse the word
    key = generate_key()
    word_data[key] = reversed_word
    return {"reversed_word": reversed_word, "key": key}

# Endpoint to retrieve a reversed word using the unique key
@app.get("/get_reversed_word/{key}", response_model=WordResponse)
async def get_reversed_word(key: str):
    if key in word_data:
        reversed_word = word_data[key]
        return {"reversed_word": reversed_word, "key": key}
    else:
        raise HTTPException(status_code=404, detail="Key not found")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

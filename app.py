import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException # type: ignore
from pydantic import BaseModel


codesetup_path = Path.home() / "Desktop" / "codesetup"
sys.path.append(str(codesetup_path))

from function import addition

app = FastAPI()


class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/add")
async def add_numbers_endpoint(numbers: Numbers):
    try:
        result = addition(numbers.num1, numbers.num2)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

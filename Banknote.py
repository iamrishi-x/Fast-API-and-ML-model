from pydantic import BaseModel

# Define the parent class
class Bank(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float


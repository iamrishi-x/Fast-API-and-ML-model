import uvicorn
from fastapi import FastAPI
from Banknote import Bank
# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}

# Define a route with a path parameter
@app.get("/{name}")
def read_name(name: str):
    return {"Name is ": name}

# Define a route with a query parameter
@app.post("/predict")
def predict_output(data:Bank):
    output=data.entropy+data.curtosis+data.skewness+data.variance
    return { "Prediction | Addition": f"output - {output}!"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    #uvicorn main:app --reload     uvicorn {filename}:{fastapi_obj_name} --reload



from fastapi import FastAPI

app = FastAPI()

@app.get("/convert")
def convert_temperature(fahrenheit: float):
    """
    Convert temperature from Fahrenheit to Celsius.
    Formula: (F - 32) * 5/9
    """

    if fahrenheit not int:
        raise ValueError("Fahrenheit value must be a number.")

    celsius = (fahrenheit - 32) * 5 / 9
    return {"fahrenheit": fahrenheit, "celsius": celsius}
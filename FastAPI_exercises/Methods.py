from fastapi import FastAPI

app = FastAPI()

@app.get("/products/{product_id}")
def display(product_id: int, include_details: bool=False):
    return {"id": product_id, "details_included": include_details}
# Products API FastAPI

A simple FastAPI application for managing products.

## Getting Started

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- FastAPI
- Uvicorn

You can install the required libraries using pip:

```bash
pip install fastapi[all] uvicorn
```

### Running the App

To run the FastAPI app, navigate to the directory containing your `products_api.py` file and execute:

```bash
uvicorn products_api:app --reload
```

This will start the server on `http://127.0.0.1:8000/`.

## API Documentation

Once the server is running, you can navigate to `http://127.0.0.1:8000/docs` to view the automatic interactive API documentation provided by FastAPI's integration with Swagger UI.

## API Endpoints

- **GET `/items/`**  
  Returns a list of all items.
- **GET `/items/{item_id}`**  
  Retrieves a specific item by its ID. Returns a 404 error if the item does not exist.

- **POST `/items/`**  
  Creates a new item. If an item with the same ID already exists, it returns a 400 error.

- **PUT `/items/{item_id}`**  
  Updates a specific item by its ID. Returns a 404 error if the item does not exist.

- **DELETE `/items/{item_id}`**  
  Deletes a specific item by its ID. Returns a 404 error if the item does not exist.

## Data Model

The API uses the following data model for an item:

```python
class Item(BaseModel):
    id: int
    name: str
    price: float
    url: str
    description: str
```

## Contribution

Feel free to fork the repository, open a pull request, or submit any issues!

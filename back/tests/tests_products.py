from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app, base_url="http://0.0.0.0:8000")


base_url = "/product"
endpoints = {
    "UPLOAD_FILE": base_url + "/file",
    "LIST_PRODUCTS": base_url + "/list",
}

def test_list_products():
    response = client.get(endpoints["LIST_PRODUCTS"])
    print(response.content)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_upload_file():
    files = {'file': ('sales.txt', open("../../sales.txt", 'rb'))}
    response = client.post(endpoints["UPLOAD_FILE"], files=files)
    print(response.content)
    assert response.status_code == 200

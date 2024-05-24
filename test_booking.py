import requests

def test_id_list_return_200():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.status_code == 200

def test_id_list_response_is_greater_then_one():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert len(response.json()) > 1

def test_subject_list_response_item_has_id():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.json()[0]["id"] is not None

def test_subject_list_response_item_has_title():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.json()[0]["title"] is not None

def test_subject_list_response_item_contains_price():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.json()[0]["price"] is not None

def test_subject_list_response_headers_has_content_type():
    response = requests.get("https://restful-booker.herokuapp.com/booking")
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"



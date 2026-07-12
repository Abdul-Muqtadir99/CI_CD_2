def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"

def test_get_weather(web_client):
    response = web_client.get("/weather")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "It's going to be a beautiful day!"
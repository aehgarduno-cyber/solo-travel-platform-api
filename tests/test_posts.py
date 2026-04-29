def test_get_posts(client):
    response = client.get("/posts")
    assert response.status_code == 200

# this is a GET - post test
# will help with the integration of testing
# can confirm flask app starts --> routing is functional --> /posts endpt. is 200 green 


def test_home_route(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Travel Blog API running" in response.data

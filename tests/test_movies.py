from .settings_tests import client

def test_create_movie():
    response = client.post(
        "/filmes/",
        json={
            "title": "The Godfather",
            "director": "Francis Ford Coppola",
            "year": 1972
        }
    )

    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972
    }

def test_get_movies():
    response = client.get("/filmes/")

    assert response.status_code == 200
    assert response.json() == [
        {
            "id": 1,
            "title": "The Godfather",
            "director": "Francis Ford Coppola",
            "year": 1972
        }
    ]

def test_get_movie():
    response = client.get("/filmes/1")

    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "title": "The Godfather",
        "director": "Francis Ford Coppola",
        "year": 1972
    }

def test_update_movie():
    response = client.put(
        "/filmes/1",
        json={
            "title": "The Godfather 2",
            "director": "Francis Ford Coppola",
            "year": 1974
        }
    )

    assert response.status_code == 202
    assert response.json() == {
        "id": 1,
        "title": "The Godfather 2",
        "director": "Francis Ford Coppola",
        "year": 1974
    }

def test_delete_movie():
    response = client.delete("/filmes/1")

    assert response.status_code == 204
    assert response.text == ""
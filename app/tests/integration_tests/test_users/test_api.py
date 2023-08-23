import pytest
from httpx import AsyncClient


@pytest.mark.parametrize("email,password,status_code", [
    ("serg@gmail.com", "serg", 201),
    ("serg@gmail.com", "serg3", 409),
    ("serg1@gmail.com", "serg1", 201),
    ("serg13@gmail.com", "serg1", 422),
])
async def test_register_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/api/v1/auth/register", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code


@pytest.mark.parametrize("email,password,status_code", [
    ("test@test.com", "test", 200),
    ("serg@gmail.com", "serg", 200),
    ("test1@gmail.com", "serg1", 401),
])
async def test_login_user(email, password, status_code, ac: AsyncClient):
    response = await ac.post("/api/v1/auth/login", json={
        "email": email,
        "password": password,
    })

    assert response.status_code == status_code
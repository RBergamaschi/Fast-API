from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_hello_world():
    client = TestClient(app)  # organização

    response = client.get('/')  # ação

    assert (
        response.status_code == HTTPStatus.OK
    )  # assert: é uma especie de garantia que a respostar vai ser == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}

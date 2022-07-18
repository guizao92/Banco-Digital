import json
from django.test import TestCase
from banco_digital.models.cliente import Cliente
from rest_framework import status


class ContaTestCase(TestCase):

    def setUp(self) -> None:
        self.cliente = Cliente()

    def test_conta_post_sucesso(self):
        # dado
        cliente = {
            "url": "http://127.0.0.1:8000/v1/cliente/3/",
            "telefone": "+554575445123",
            "nome": "Guilherme",
            "cpf": "12345678999",
            "email": "teste@gmail.com",
            "endereço": "Rua teste 2"
        }

        # quando
        response = self.client.post('v1/cliente/', cliente, format='json')

        # entao
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

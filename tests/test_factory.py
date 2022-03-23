from unittest import TestCase
from app import create_app


class TestFlaskApp(TestCase):
    def test_create_app_ocorre(self):
        self.assertEqual(hasattr(app.create_app, 'create_app'), True, 'Não ocorre aplicação')

    def test_create_app_ativa(self):
        self.assertEqual(hasattr(app.create_app, '__call__' ), True, 'jsonarray não está ativa')

    def test_create_app_ativa_no_flask_app(self):
        self.assertInstance(app.create_app, Flask, 'jsonarray não faz parte do escopo do projeto Flask')

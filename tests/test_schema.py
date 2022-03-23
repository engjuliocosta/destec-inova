from unittest import TestCase
from app import schema

class TestSchema(TestCase):
    def test_schema_deve_ter_funcao_de_setup(self):
        self.assertEqual(hasattr(schema, 'configure_app'), True, "Schema não está configurado")

    def test_setup_ativo(self):
        self.assertEqual(hasattr(schema.configure_app, '__call__'), True, 'Setup do schema não está ativo')

    def test_setup_se_schema_ativo(self):
        self.assertEqual(hasattr(schema.configure_app.__code__.co_argcount, 1), True, 'configure_app não recebe app')

    def test_schema_deve_ter_ma(self):
        self.assertEqual(hasattr(schema, 'configure_app'), True, "Schema não está configurado")

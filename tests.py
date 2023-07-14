from api import app
import unittest
import json


class TestAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    # Caso de éxito: obtener contactos de una cuenta existente
    def test_get_contactos_success(self):
        response = self.app.get('/billetera/contactos?minumero=21345')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data())
        self.assertEqual(data['usuario_nombre'], 'Arnaldo')

    # Caso de error: obtener contactos de una cuenta no existente
    def test_get_contactos_fail(self):
        response = self.app.get('/billetera/contactos?minumero=10101010101010')
        self.assertEqual(response.status_code, 404)

    # Caso de error: enviar operacion desde una cuenta no existente
    def test_post_mensaje_fail(self):
        response = self.app.get('/billetera/pagar?minumero=10101010101010&numerodestino=21345&valor=10')
        self.assertEqual(response.status_code, 404)

    # Caso de error: obtener operaciones enviadas por una cuenta no existente
    def test_get_enviados_fail(self):
        response = self.app.get('/billetera/enviadas?minumero=10101010101010')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()

from datetime import date


class Operacion:
    def __init__(self, numero_origen, numero_destino, valor):
        self.numero_origen = numero_origen
        self.numero_destino = numero_destino
        self.valor = valor
        self.fecha = date.today()


class Cuenta:
    def __init__(self, numero, nombre, saldo, lista_contactos):
        self.numero = numero
        self.nombre = nombre
        self.saldo = saldo
        self.lista_contactos = lista_contactos
        self.lista_operaciones_recibidas = []
        self.lista_operaciones_enviadas = []

    def recibir_mensaje(self, operacion):
        self.lista_operaciones_recibidas.append(operacion)

    def enviar_mensaje(self, operacion):
        if (operacion.valor <= self.saldo) and (operacion.numero_destino in self.lista_contactos):
            self.lista_operaciones_enviadas.append(operacion)
            return True

        return False

    def get_lista_contactos(self):
        response = {
            "usuario_numero": self.numero,
            "usuario_nombre": self.nombre,
            "contactos": self.lista_contactos
        }

        return response

    def get_operaciones_recibidas(self):
        lista_operaciones_recibidas_tmp = []

        for operacion in self.lista_operaciones_recibidas:
            tmp_operacion = {
                "numero_origen": operacion.numero_origen,
                "numero_destino": operacion.numero_destino,
                "valor": operacion.valor
            }
            lista_operaciones_recibidas_tmp.append(tmp_operacion)

        response = {
            "cuenta_numero": self.numero,
            "cuenta_nombre": self.nombre,
            "cuenta_saldo": self.saldo,
            "operaciones_recibidas": lista_operaciones_recibidas_tmp
        }

        return response

    def get_operaciones_enviadas(self):
        lista_operaciones_enviadas_tmp = []

        for operacion in self.lista_operaciones_enviadas:
            tmp_operacion = {
                "numero_origen": operacion.numero_origen,
                "numero_destino": operacion.numero_destino,
                "valor": operacion.valor
            }
            lista_operaciones_enviadas_tmp.append(tmp_operacion)

        response = {
            "cuenta_numero": self.numero,
            "cuenta_nombre": self.nombre,
            "cuenta_saldo": self.saldo,
            "operaciones_enviadas": lista_operaciones_enviadas_tmp
        }

        return response

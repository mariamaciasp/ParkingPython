import random
class vehiculo_service:

    def calcular_pin(self):
        longitud_pin = 6
        pin = []
        for i in range(longitud_pin):
            pin.append(str(random.randrange(10)))

        pin_final = int("".join(pin))

        return int(pin_final)

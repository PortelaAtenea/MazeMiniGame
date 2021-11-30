from main import Cuarto


class Cuarto1(Cuarto):
    """Creacion del nivel 1"""

    def __init__(self):
        super().__init__()
        # Crear las paredes. (x_pos, y_pos, largo, alto)

        # Esta es la lista de las paredes. Cada una se especifica de la forma [x, y, largo, alto]
        paredes = [[0, 0, 20, 250, BLANCO],
                   [0, 350, 20, 250, BLANCO],
                   [780, 0, 20, 250, BLANCO],
                   [780, 350, 20, 250, BLANCO],
                   [20, 0, 760, 20, BLANCO],
                   [20, 580, 760, 20, BLANCO],
                   [390, 50, 20, 500, AZUL]
                   ]

        # Iteramos a través de la lista. Creamos la pared y la añadimos a la lista.
        for item in paredes:
            pared = Pared(item[0], item[1], item[2], item[3], item[4])
            self.pared_lista.add(pared)

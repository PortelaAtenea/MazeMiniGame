
class Jugador:
    x = 10
    y = 10
    velocidad = 1

    def moveRight(self):
        self.x = self.x + self.velocidad

    def moveLeft(self):
        self.x = self.x - self.velocidad

    def moveUp(self):
        self.y = self.y - self.velocidad

    def moveDown(self):
        self.y = self.y + self.velocidad

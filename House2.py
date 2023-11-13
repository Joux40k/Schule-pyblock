from pyblockworld import World
from Wall import Wall
from Roof import Roof


class House():
    def __init__(self, pos: tuple, bw: World):
        self.wallFront: Wall = Wall
        self.wallLeft: Wall = Wall
        self.wallRight: Wall = Wall
        self.wallBack: Wall = Wall
        self.pos = pos
        self.roof: Roof = Roof
        self.__bw = bw

    def build(self):
        self.wallFront = Wall(self.__bw, self.pos)
        self.wallLeft = Wall(self.__bw, self.pos)
        self.wallLeft.rotated = True
        x, y, z = self.pos
        x += self.wallLeft.width
        z += self.wallLeft.width
        frontWallPos = x, y, z
        self.wallRight = Wall(self.__bw, frontWallPos)
        self.wallFront.build()
        self.wallLeft.build()
        self.wallRight.build()
        x, y, z = self.pos
        y += 6
        roofPos = x, y, z
        self.roof = Roof(self.__bw, roofPos)


def buildHouse(world: World):
    house = House(world.player_position(), world)
    house.build()


world = World()
world.build_key_pressed = buildHouse
world.run()

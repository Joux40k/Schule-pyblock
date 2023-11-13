from pyblockworld import World
from Roof import Roof
from Wall import Wall
from wall_with_window_or_door import WallWithDoor, WallWithWindow



class House():
    def __init__(self, pos: tuple, bw: World):
        self.pos = pos
        self.__bw = bw
        self.wallFront = WallWithDoor(self.__bw, self.pos)
        self.wallLeft = WallWithWindow(self.__bw, self.pos)
        self.wallLeft.rotated = True
        x, y, z = self.pos
        rightWallPosition = x + self.wallFront.width, y, z
        self.wallRight = WallWithWindow(self.__bw, rightWallPosition)
        self.wallRight.rotated = True
        backWallPosition = x, y, z + self.wallRight.width
        self.wallBack = Wall(self.__bw, backWallPosition)
        y += self.wallLeft.height
        roofPos = x, y, z
        self.roof = Roof(self.__bw, roofPos)


    def build(self):
        self.wallFront.build()
        self.wallLeft.build()
        self.wallRight.build()
        self.wallBack.build()
        self.roof.build()


def buildHouse(world: World):
    house = House(world.player_position(), world)
    house.build()


world = World()
world.build_key_pressed = buildHouse
world.run()

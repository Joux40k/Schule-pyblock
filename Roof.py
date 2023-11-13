from pyblockworld import World
import math

class Roof():
    def __init__(self, bw: World, pos: tuple):
        self.width = 6
        self.depth = 6
        self.roof_material_id = "default:brick"
        self.pos = pos
        self.__bw = bw

    def build(self):
        x,y,z = self.pos
        x += 1
        steps = 0
        half = self.width // 2
        while steps <= half:
            self.__bw.setBlocks(math.ceil(x+steps), math.ceil(y), math.ceil(z),
                                math.ceil(x +self.width- steps), math.ceil(y + steps), math.ceil(z + self.depth),
                                self.roof_material_id)
            steps += 1

def buildRoof(world: World):
    roof = Roof(world, world.player_position())
    roof.build()


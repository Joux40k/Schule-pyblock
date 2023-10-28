from pyblockworld import World

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
        while steps < (self.width // 2):
            if steps == 0:
                self.__bw.setBlocks(x, y, z, x + self.width-1, y, z + self.depth-1, self.roof_material_id)
            self.__bw.setBlocks(x+steps,y,z,x+self.width-steps,y+steps,z+self.depth, self.roof_material_id)
            steps += 1

def buildRoof(world: World):
    roof = Roof(world, world.player_position())
    roof.build()

world = World()
world.build_key_pressed = buildRoof
world.run()
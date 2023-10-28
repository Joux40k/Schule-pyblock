from pyblockworld import World
from pyglet.window import key


class ThreeBlocks(World):
    def __init__(self):
        super().__init__()

    def t_key_pressed(self):
        print("t key pressed")
        x,y,z = self.player_position()
        self.setBlock(x + 1, y, z, "default:brick")
        self.setBlock(x + 2, y, z, "default:sand")
        self.setBlock(x + 3, y, z, "default:stone")

    def unknown_key_pressed(self, symbol):
        super().unknown_key_pressed(symbol)
        if symbol == key.T:
            self.t_key_pressed()



world = ThreeBlocks()
world.run()
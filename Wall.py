from pyblockworld import World

class Wall():
    def __init__(self, bw: World, pos: tuple):
        self.width = 6
        self.height = 5
        self.pos = pos
        self.rotated = False

        self.material_id = "default:stone"
        self._bw = bw

    def build(self):
        x, y, z = self.pos
        x += 1
        if self.rotated:
            self._bw.setBlocks(x, -1, z, x, y + self.height, z + self.width, self.material_id)
        else:
            self._bw.setBlocks(x, -1, z, x + self.width, y + self.height, z, self.material_id)
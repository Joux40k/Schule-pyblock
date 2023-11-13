from pyblockworld import World
from Wall import Wall


class WallWithWindow(Wall):
    def __init__(self, bw: World, pos: tuple):
        super().__init__(bw, pos)
        self.window_material_id:str = "air"

    def build(self):
        super().build()
        x, y, z = self.pos
        x += 1
        window_width: int
        window_height: int
        if self.width >= 4:
            window_width = 2
        else:
            window_width = 1
        if self.height >= 4:
            window_height = 2
        else:
            window_height = 1
        window_start_pos = self.width / 2
        if self.rotated:
            self._bw.setBlocks(x, y, z + window_start_pos, x, y + window_height, z + window_width, self.window_material_id)
        else:
            self._bw.setBlocks(x+window_start_pos, y, z, x+window_height, y + window_height, z, self.window_material_id)

def placeTwoWallsWithWindow(world:World):
    wall_with_window = WallWithWindow(world, world.player_position())
    wall_with_window.build()
    wall_with_window_rotated = WallWithWindow(world, world.player_position())
    wall_with_window_rotated.rotated = True
    wall_with_window_rotated.build()

class WallWithDoor(Wall):
    def __init__(self, bw: World, pos: tuple):
        super().__init__(bw, pos)
        self.window_material_id:str = "air"

    def build(self):
        super().build()
        x, y, z = self.pos
        x += 1
        door_position = self.width / 2
        if self.rotated:
            self._bw.setBlocks(x, y-1, z + door_position, x, y+1, z + door_position, self.window_material_id)
        else:
            self._bw.setBlocks(x+door_position, y-1, z, x + door_position, y +1, z, self.window_material_id)

def placeTwoWallsWithDoor(world: World):
    x,y,z = world.player_position()
    x += 10
    wall_location: tuple = x,y,z
    wall_with_door = WallWithDoor(world, wall_location)
    wall_with_door.build()
    wall_with_door_rotated = WallWithDoor(world, wall_location)
    wall_with_door_rotated.rotated = True
    wall_with_door_rotated.build()

def place4Walls(world: World):
    placeTwoWallsWithDoor(world)
    placeTwoWallsWithWindow(world)


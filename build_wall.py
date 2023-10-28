from pyblockworld import World
from Wall import Wall


def placeWall(world: World):
    wall = Wall(world, world.player_position())
    wall.build()
    wallRotated = Wall(world, world.player_position())
    wallRotated.rotated = True
    wallRotated.build()


world = World()
world.build_key_pressed = placeWall
world.run()

from pyblockworld import World
def b_key_pressed(world: World):
    # Neue Blöcke können mit setBlock gesetzt werden.
    # Verfügbare Materialien stehen in World.MATERIALS und umfassen
    # air, default:brick, default:stone, default:sand, default:grass
    print("Block types", World.MATERIALS)
    x, y, z = world.player_position()
    # Einen Block platzieren
    world.setBlock(x, y, z, "default:brick")

    # Mehrere Blöcke auf einmal abseits des Spielers platzieren
    x, y, z = x, y, z + 3
    world.setBlocks(x, y, z, x + 3, y + 3, z + 3, "default:grass")


world = World()
world.build_key_pressed = b_key_pressed
world.run()
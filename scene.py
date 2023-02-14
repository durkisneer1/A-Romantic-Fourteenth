from ursina import *


def load_scene():
    # Sky
    Entity(
        model="sphere",
        texture="assets/sky.png",
        position=(-3.5, 0, 21),
        scale=75,
        color=color.dark_gray,
        double_sided=True,
    )
    Entity(
        model="sphere",
        texture="assets/moon.jpg",
        position=(3.5, 24.5, 42),
        rotation_y=90,
        scale=8,
    )

    # Rooms
    Entity(
        model=f"assets/rooms.obj",
        texture="assets/walls.png",
        collider="mesh",
    )
    Entity(
        model="plane",
        texture="assets/arrow.png",
        rotation=(-90, 0, 90),
        scale=3,
        position=(-13.9, 2, 0),
    )
    Entity(
        model="assets/outer_walls.obj",
        texture="assets/outer_walls.png",
    )

    # Beach
    Entity(
        model="assets/beach.obj",
        texture="assets/sand.png",
        collider="box",
    )
    Entity(
        model="plane",
        visible=False,
        collider="box",
        position=(-14, 2.5, 21),
        rotation_z=90,
        scale=(5, 1, 21),
    )
    Entity(
        model="plane",
        visible=False,
        collider="box",
        position=(7, 2.5, 21),
        rotation_z=90,
        scale=(5, 1, 21),
    )
    Entity(
        model="plane",
        visible=False,
        collider="box",
        position=(-3.5, 2.5, 31.5),
        rotation_z=90,
        rotation_y=90,
        scale=(5, 1, 21),
    )

    # Trees
    Entity(
        model="assets/trees.obj",
        texture="assets/trees.png",
        double_sided=True,
    )


def load_props():
    # Rose Pedals
    Entity(
        model="assets/pedals.obj",
        texture="assets/pedals.png",
    )

    # Candles
    Entity(
        model="assets/candles.obj",
        texture="assets/candles.png",
    )

    # Campfire
    Entity(
        model="assets/campfire.obj",
        texture="assets/campfire.png",
    )

    # Banner
    Entity(
        model="assets/banner.obj",
        texture="assets/banner.png",
        color=rgb(75, 39, 81),
        double_sided=True,
    )
    Entity(
        model="assets/poles.obj",
        color=color.black,
    )

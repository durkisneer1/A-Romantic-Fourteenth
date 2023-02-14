from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController  # NOQA
from direct.filter.CommonFilters import CommonFilters

from scene import load_scene, load_props


def input(key):  # NOQA
    if key == Keys.escape:
        application.quit()


def setup_fps():
    fps_cam = FirstPersonController()
    fps_cam.position = (4, 0, 0)
    fps_cam.rotation_y = -90
    fps_cam.cursor.visible = False

    fps_cam.jump_height = 1.5
    fps_cam.jump_up_duration = 0.5
    fps_cam.fall_after = 0.25


def main():
    app = Ursina(borderless=False, fullscreen=True)
    camera.clip_plane_near = 0.25

    filters = CommonFilters(app.win, app.cam)
    filters.setBloom()
    filters.setBlurSharpen(0.5)

    # EditorCamera()
    setup_fps()

    load_scene()
    load_props()

    while True:
        app.step()


if __name__ == '__main__':
    main()

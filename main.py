import sys
import os
import time
import dxcam
import mouse
import keyboard
import pygetwindow as gw
from pynput.keyboard import Key, Controller
from constants import APPLICATION_TRIGGER, COLOR_TRIGGERS, PIXELS_PER_ITERATION, \
                      NEW_GAME_TRIGGER_POS, APPLICATION_NAME

__author__ = "Ata"

def exit_program():
    """Exit the program."""
    print("Exiting program...")
    os._exit(0)

def get_application_bbox() -> tuple[int]:
    """Bring the game window to the foreground and return its bounding box."""
    windows_list = [window for window in gw.getAllWindows() if APPLICATION_NAME in window.title]

    if not windows_list:
        return None  # Application not found

    app_window = windows_list[0]
    
    # Bring the window to the foreground
    keyboard_controller = Controller()
    keyboard_controller.press(Key.alt)
    app_window.activate()
    keyboard_controller.release(Key.alt)

    return app_window.left, app_window.top, app_window.right, app_window.bottom

def is_game_running(frame, app_bbox) -> bool:
    """Check if the game is running by scanning for specific colors in the timer."""
    if not app_bbox:
        return False

    left, top, right, bottom = app_bbox
    for x_rel, y_rel in APPLICATION_TRIGGER['positions']:
        x = int(x_rel * (right - left)) + left
        y = int(y_rel * (bottom - top)) + top

        try:
            if frame[y][x][:3] == tuple(APPLICATION_TRIGGER['color']):
                return True
        except IndexError:
            print('Operation terminated due to window movement.')
            return False

    return False

def is_object_detected(pixel: tuple[int]) -> bool:
    """Detect the target object by its color."""
    red, green, blue = pixel
    if COLOR_TRIGGERS['red']['min'] <= red <= COLOR_TRIGGERS['red']['max']:
        if COLOR_TRIGGERS['green']['min'] <= green <= COLOR_TRIGGERS['green']['max']:
            if COLOR_TRIGGERS['blue']['min'] <= blue <= COLOR_TRIGGERS['blue']['max']:
                return True
    return False

def wait_for_game_start(camera) -> None:
    """Wait for the game to start by checking the window state."""
    frame = camera.get_latest_frame()
    app_bbox = get_application_bbox()
    while not is_game_running(frame, app_bbox):
        time.sleep(0.2)
        frame = camera.get_latest_frame()
        app_bbox = get_application_bbox()

def main():
    """Main function to run the bot."""
    keyboard.add_hotkey('ctrl+x', exit_program)
    print("Press Ctrl + X to exit the program.")

    game_counter = 0
    total_games = int(sys.argv[1]) if len(sys.argv) > 1 else 1

    camera = dxcam.create()
    camera.start(target_fps=60)

    print('Detecting the game. Please click play...')
    wait_for_game_start(camera)

    # Define bounds for scanning the game window
    x_shift, y_shift_top, y_shift_bottom = 20, 150, 250
    app_bbox = get_application_bbox()
    left, top, right, bottom = app_bbox

    x_range = range(left + x_shift, right - x_shift, PIXELS_PER_ITERATION)
    y_range = range(top + y_shift_top, bottom - y_shift_bottom, PIXELS_PER_ITERATION)

    # Game loop
    while game_counter < total_games:
        game_counter += 1
        print(f"Starting game {game_counter}...")

        frame = camera.get_latest_frame()
        while is_game_running(frame, app_bbox):
            for x in x_range:
                for y in y_range:
                    if is_object_detected(frame[y][x]):
                        mouse.move(x, y, absolute=True)
                        mouse.click(button='left')

            frame = camera.get_latest_frame()

        print(f"Game {game_counter} finished.")

        if game_counter < total_games:
            time.sleep(0.5)
            x_new_game = left + int(NEW_GAME_TRIGGER_POS[0] * (right - left))
            y_new_game = top + int(NEW_GAME_TRIGGER_POS[1] * (bottom - top))
            mouse.move(x_new_game, y_new_game, absolute=True)
            mouse.click(button='left')

            wait_for_game_start(camera)

    del camera

if __name__ == "__main__":
    main()
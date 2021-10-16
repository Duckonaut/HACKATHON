from pynput import keyboard
import win32api

def tonemap(value: int) -> int:
    return int(55 * pow(2, value / 12))

def on_press(key: keyboard.Key):
    if key == keyboard.Key.esc:
        quit()
    else:
        try:
            win32api.Beep(tonemap(ord(key.char) - ord('0')), 200)
        except AttributeError:
            win32api.Beep(tonemap(key.value.vk), 200)
        except TypeError:
            pass


def main():
    with keyboard.Listener(
        on_press=on_press) as listener:
        listener.join()


        
if __name__ == "__main__":
    main()

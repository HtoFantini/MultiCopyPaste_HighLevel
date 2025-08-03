import keyboard
import pyperclip
import time
from collections import deque

from global_vars import MAX_BUFF_SIZE, clipboard_buffer

def get_last_copied(buf: deque):
    if len(buf) > 0:
        return clipboard_buffer[0]
    return None

def copy_callback(buf: deque = clipboard_buffer):
    item = pyperclip.paste()
    # FAZER COM QUE SEJA INSERIDO NA FILA (ITEM,TIPO)
    print("ITEM COPIED: ", item)   
    if item != get_last_copied(buf=buf):
        print("Recent item on clipboard BEFORE:", get_last_copied(buf=buf))
        clipboard_buffer.appendleft(item)
        print("Recent item on clipboard AFTER:", get_last_copied(buf=buf))
        print(clipboard_buffer)
        return item
    else:
        print("Same as last item copied")
        return item


if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+c', copy_callback)
    keyboard.wait()
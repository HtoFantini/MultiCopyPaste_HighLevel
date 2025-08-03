import keyboard

from mt_copy import copy_callback
from mt_paste import paste_callback
from global_vars import MAX_BUFF_SIZE, clipboard_buffer


def main():
    keyboard.add_hotkey('ctrl+c', copy_callback)
    for i in range(MAX_BUFF_SIZE):
        key_seq = f"ctrl+alt+{i+1}"
        print(key_seq)
        keyboard.add_hotkey(key_seq, lambda num=i: paste_callback(num=num,buf=clipboard_buffer))
    keyboard.wait()

if __name__ == "__main__":
    main()




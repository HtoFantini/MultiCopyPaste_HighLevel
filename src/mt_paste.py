import keyboard
import pyperclip
import time
from collections import deque

from global_vars import MAX_BUFF_SIZE, clipboard_buffer
from key_sequences import paste_key_seq

def paste_callback(num: int, buf: deque = clipboard_buffer):
    print(f"\n--- Atalho com o número {num} detectado! ---")

    try:
        item_bkp = pyperclip.paste()
        print("Clipboard original salvo.")
    except pyperclip.PyperclipException:
        item_bkp = ""
    
    try:
        item_to_paste = clipboard_buffer[num-1]
        print(f"Preparando para colar: \"{item_to_paste[:30]}...\"")
        pyperclip.copy(item_to_paste)

    except IndexError as e:
        print("Nada foi copiado para este numero")
        return 
    
    time.sleep(0.1)

    # Simula a ação de "colar" (Ctrl+V).
    keyboard.press_and_release('ctrl+v')
    print("Ação de colar (Ctrl+V) simulada.")
    
    # Restaura o conteúdo original do clipboard.
    time.sleep(0.1)
    pyperclip.copy(item_bkp)
    print("Clipboard original restaurado.")


if __name__ == "__main__":
    for i in range(MAX_BUFF_SIZE):
        atalho = f"ctrl+alt+{i+1}"
        keyboard.add_hotkey(atalho, lambda num=i: paste_callback(num=num,buf=clipboard_buffer))
    keyboard.wait()
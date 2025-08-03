from collections import deque

MAX_BUFF_SIZE = 9

clipboard_buffer = deque(maxlen=MAX_BUFF_SIZE)

# TODO ACREDITO QUE ESSA NAO SEJA A MELHOR FORMA DE COMPARTILHAR UMA FILA
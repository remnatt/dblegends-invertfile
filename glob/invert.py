# remnatt による glob dbl
## interref; 96fcxxi>><zarcF> --debug --depack --releasein Py

def decrypt_file(file_path):
    with open(file_path, 'rb') as file:
        file_bytes = bytearray(file.read())

    for i in range(len(file_bytes)):
        file_bytes[i] = (~file_bytes[i] + 256) & 0xFF

    with open(file_path, 'wb') as file:
        file.write(file_bytes)

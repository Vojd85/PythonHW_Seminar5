# задача 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
from files import *
en_path_vvod = 'encode_vvod.txt'
en_path_vivod = 'encode_vivod.txt'
de_path_vvod = 'decode_vvod.txt'
de_path_vivod = 'decode_vivod.txt'

def encode(string):
    en_string = ''
    count = 1
    for i in range(len(string)):
        if i+1 < len(string) and string[i+1] == string[i]:
            count += 1
        else:
            en_string += str(count) + string[i]
            count = 1
    return en_string

def decode(string):
    de_string = ''
    for i in range(len(string)-1):
        if (string[i]).isdigit():
            de_string += int(string[i]) * string[i+1]
        else:
            continue
    return de_string

en_str = encode(read_file(en_path_vvod))
add_file(en_path_vivod, en_str)

de_str = decode(read_file(de_path_vvod))
add_file(de_path_vivod, de_str)


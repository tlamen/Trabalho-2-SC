
# S_BOX utilizada nas funções de substituição
S_BOX = {
    "0": "63", "1": "7c", "2": "77", "3": "7b", "4": "f2", "5": "6b", "6": "6f", "7": "c5",
    "8": "30", "9": "1", "a": "67", "b": "2b", "c": "fe", "d": "d7", "e": "ab", "f": "76",
    "10": "ca", "11": "82", "12": "c9", "13": "7d", "14": "fa", "15": "59", "16": "47", "17": "f0",
    "18": "ad", "19": "d4", "1a": "a2", "1b": "af", "1c": "9c", "1d": "a4", "1e": "72", "1f": "c0",
    "20": "b7", "21": "fd", "22": "93", "23": "26", "24": "36", "25": "3f", "26": "f7", "27": "cc",
    "28": "34", "29": "a5", "2a": "e5", "2b": "f1", "2c": "71", "2d": "d8", "2e": "31", "2f": "15",
    "30": "4", "31": "c7", "32": "23", "33": "c3", "34": "18", "35": "96", "36": "5", "37": "9a",
    "38": "7", "39": "12", "3a": "80", "3b": "e2", "3c": "eb", "3d": "27", "3e": "b2", "3f": "75",
    "40": "9", "41": "83", "42": "2c", "43": "1a", "44": "1b", "45": "6e", "46": "5a", "47": "a0",
    "48": "52", "49": "3b", "4a": "d6", "4b": "b3", "4c": "29", "4d": "e3", "4e": "2f", "4f": "84",
    "50": "53", "51": "d1", "52": "0", "53": "ed", "54": "20", "55": "fc", "56": "b1", "57": "5b",
    "58": "6a", "59": "cb", "5a": "be", "5b": "39", "5c": "4a", "5d": "4c", "5e": "58", "5f": "cf",
    "60": "d0", "61": "ef", "62": "aa", "63": "fb", "64": "43", "65": "4d", "66": "33", "67": "85",
    "68": "45", "69": "f9", "6a": "2", "6b": "7f", "6c": "50", "6d": "3c", "6e": "9f", "6f": "a8",
    "70": "51", "71": "a3", "72": "40", "73": "8f", "74": "92", "75": "9d", "76": "38", "77": "f5",
    "78": "bc", "79": "b6", "7a": "da", "7b": "21", "7c": "10", "7d": "ff", "7e": "f3", "7f": "d2",
    "80": "cd", "81": "c", "82": "13", "83": "ec", "84": "5f", "85": "97", "86": "44", "87": "17",
    "88": "c4", "89": "a7", "8a": "7e", "8b": "3d", "8c": "64", "8d": "5d", "8e": "19", "8f": "73",
    "90": "60", "91": "81", "92": "4f", "93": "dc", "94": "22", "95": "2a", "96": "90", "97": "88",
    "98": "46", "99": "ee", "9a": "b8", "9b": "14", "9c": "de", "9d": "5e", "9e": "b", "9f": "db",
    "a0": "e0", "a1": "32", "a2": "3a", "a3": "a", "a4": "49", "a5": "6", "a6": "24", "a7": "5c",
    "a8": "c2", "a9": "d3", "aa": "ac", "ab": "62", "ac": "91", "ad": "95", "ae": "e4", "af": "79",
    "b0": "e7", "b1": "c8", "b2": "37", "b3": "6d", "b4": "8d", "b5": "d5", "b6": "4e", "b7": "a9",
    "b8": "6c", "b9": "56", "ba": "f4", "bb": "ea", "bc": "65", "bd": "7a", "be": "ae", "bf": "8",
    "c0": "ba", "c1": "78", "c2": "25", "c3": "2e", "c4": "1c", "c5": "a6", "c6": "b4", "c7": "c6",
    "c8": "e8", "c9": "dd", "ca": "74", "cb": "1f", "cc": "4b", "cd": "bd", "ce": "8b", "cf": "8a",
    "d0": "70", "d1": "3e", "d2": "b5", "d3": "66", "d4": "48", "d5": "3", "d6": "f6", "d7": "e",
    "d8": "61", "d9": "35", "da": "57", "db": "b9", "dc": "86", "dd": "c1", "de": "1d", "df": "9e",
    "e0": "e1", "e1": "f8", "e2": "98", "e3": "11", "e4": "69", "e5": "d9", "e6": "8e", "e7": "94",
    "e8": "9b", "e9": "1e", "ea": "87", "eb": "e9", "ec": "ce", "ed": "55", "ee": "28", "ef": "df",
    "f0": "8c", "f1": "a1", "f2": "89", "f3": "d", "f4": "bf", "f5": "e6", "f6": "42", "f7": "68",
    "f8": "41", "f9": "99", "fa": "2d", "fb": "f", "fc": "b0", "fd": "54", "fe": "bb", "ff": "16"
}

INVERTED_S_BOX = {value: key for key, value in S_BOX.items()}


Rcon = [0x00000000, 0x01000000, 0x02000000,
		0x04000000, 0x08000000, 0x10000000, 
		0x20000000, 0x40000000, 0x80000000, 
		0x1b000000, 0x36000000]

# Função para pegar os estados de entrada de um texto
# Recebe o texto em string
# Devolve um array com as matrizes dos estados de entrada em ordem
def get_bytes(texto):
    matrices = []
    byte_array = bytearray(texto, 'utf-8')
    num_matrices = len(byte_array) // 16

    for i in range(num_matrices):
        matrix = []
        for j in range(4):
            row = []
            for k in range(4):
                row.append(byte_array[i * 16 + j * 4 + k])
            matrix.append(row)
        matrices.append(matrix)

    return matrices

# Função que executa um XOR bit a bit entre 2 matrizes 4x4
# Recebe duas matrizes 4x4
# Retorna uma matriz 4x4
def add_round_key(text_matrix, key_matrix):
    state = []
    for i in range(4):
        row = []
        for j in range(4):
            row.append(text_matrix[i][j] ^ key_matrix[i][j])
        state.append(row)
    return state

def wordXOR(word1, word2):
    new = []
    for i in range(4):
        new.append(int(word1[i]) ^ int(word2[i]))
    return new

def wordHeXOR(word1, int1):
    new_word = []
    bin1 = bin(int1)
    s = ''
    for n in word1:
        s_temp = bin(n)[2:]
        while len(s_temp) != 8:
            s_temp = '0' + s_temp
        s += s_temp
    s = int(s, 2)
    s = bin(s)
    xord = int(s, 2) ^ int(bin1, 2)
    hexed = hex(xord)[2:]
    if len(hexed) != 8:
        hexed = '0' + hexed
    
    for i in range(4):
        temp = hexed[i*2:2+i*2]
        new_word.append(int(temp, 16))
    return new_word

# Função que gera um array com 11 sub-chaves 
# Recebe a chave como string
# Retorna um array com 11 matrizes 4x4 representando as sub-chaves
def key_expansion(key):
    sub_keys = []
    words = []
    init_round_key = get_bytes(key)[0]
    sub_keys.append(init_round_key)
    for i in range(4):
        words.append(init_round_key[i])

    for i in range(4, 44):
        temp = words[i-1]
        word = words[i-4]

        if (i % 4 == 0):
            y = KeySubBytes(RotWord(temp))
            temp = wordHeXOR(y,  Rcon[int(i / 4)])
        words.append(wordXOR(word, temp))
    
    # print("Words array: ", words)

    for i in range(4, len(words), 4):
        sub_keys.append([words[i], words[i+1], words[i+2], words[i+3]])
    return sub_keys

# Função de rotação de palavras
# Recebe uma palavra
# retorna uma nova palavra, com os bytes rotacionados para a esquerda
def RotWord(word):
    return [word[1], word[2], word[3], word[0]]

# Função de substituição de palavra
# Recebe uma palavra
# Retorna uma nova palavra com os valores corresppondentes na S_BOX
def KeySubBytes(word):
    new = []
    for i in range(4):
        new.append(int(S_BOX[hex(int(word[i]))[2:4]], 16))
    return new
        
# Função de substituição de matriz
# Recebe a matriz a ser substituida
# Retorna uma nova matriz com os valores corresppondentes na S_BOX
def InvSubBytes(matrix):
    new = []
    for i in range(4):
        column = []
        for j in range(4):
            column.append(int(INVERTED_S_BOX[hex(matrix[i][j])[2:4]], 16))
        new.append(column)
    return new

# Função de mudança de linhas de matriz
# Recebe uma matriz
# Retorna uma nova matriz, com as linhas permutadas adequadamente segundo o algoritmo 
def ShiftRows(matrix):
    new = []

    new.append([matrix[0][0], matrix[1][1], matrix[2][2], matrix[3][3]])
    new.append([matrix[1][0], matrix[2][1], matrix[3][2], matrix[0][3]])
    new.append([matrix[2][0], matrix[3][1], matrix[0][2], matrix[1][3]])
    new.append([matrix[3][0], matrix[0][1], matrix[1][2], matrix[2][3]])

    return new

# Função de multiplicação no campo de galois - auxiliar para função MixColumns
# Recebe dois números
# Retiorna a multiplicação no campo de galois entre eles
def gmul(a, b):
    if b == 1:
        return a
    tmp = (a << 1) & 0xff
    if b == 2:
        return tmp if a < 128 else tmp ^ 0x1b
    if b == 3:
        return gmul(a, 2) ^ a
def gmul09(a):
    return gmul(gmul(gmul(a, 2), 2), 2) ^ a

def gmul11(a):
    return gmul((gmul(gmul(a, 2), 2) ^ a), 2) ^ a

def gmul13(a):
    return gmul(gmul((gmul(a, 2) ^ a), 2), 2) ^ a

def gmul14(a):
    return gmul((gmul((gmul(a, 2) ^ a), 2) ^ a), 2)
# Função de embaralhamento de colunas
# Recebe uma matriz
# Retorna uma nova matriz, com mudanças realizadas por coluna
def MixColumns(matrix):
    new = [[], [], [], []]
    
    for i in range(4):
        new[i].append(gmul(matrix[i][0], 2) ^ gmul(matrix[i][1], 3) ^ gmul(matrix[i][2], 1) ^ gmul(matrix[i][3], 1))
        new[i].append(gmul(matrix[i][1], 2) ^ gmul(matrix[i][2], 3) ^ gmul(matrix[i][3], 1) ^ gmul(matrix[i][0], 1))
        new[i].append(gmul(matrix[i][2], 2) ^ gmul(matrix[i][3], 3) ^ gmul(matrix[i][0], 1) ^ gmul(matrix[i][1], 1))
        new[i].append(gmul(matrix[i][3], 2) ^ gmul(matrix[i][0], 3) ^ gmul(matrix[i][1], 1) ^ gmul(matrix[i][2], 1))

    return new


# Função de deciframento
# Recebe uma matriz 4x4 do texto base e o conjunto de subchaves a ser utilizada
# retorna uma matriz 4x4 criptografada
def encrypt(text_matrix, keys):
    temp = add_round_key(text_matrix, keys[0])
    for i in range(1, len(keys)):
        # print("ROUND ", i)
        # print("Used subkey: ", keys[i])
        temp = InvSubBytes(temp)
        # print("After SubBytes: ", temp)
        temp = InvShiftRows(temp)
        # print("After ShiftRows: ", temp)
        if i != 10:
            temp = InvMixColumns(temp)
        # print("After MixColumns: ", temp)
        temp = add_round_key(temp, keys[i])
        # print("After addRoundKey: ", temp)
    return temp

# Função de conversão em texto
# Recebe uma lista de matrizes 4x4
# Retorna texto correspondente
def to_text(matrixes):
    s = ""
    for matrix in matrixes:
        for i in range(4):
            for j in range(4):
                s += chr(matrix[i][j])
    return s


text = input("encrypted text: ")

key = input("key: ")
while len(key) != 16:
    key = input("key (128 bits / 16 caracteres): ")

keys = key_expansion(key)
# for key in keys:
#     print("Sub-chave: ", key)

text = get_bytes(text)

results = []
for i in range(len(text)):
    results.append(encrypt(text[i], keys))

# print(keys)
print(results)
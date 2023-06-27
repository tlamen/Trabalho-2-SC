text = input("plain text: ")

S_BOX = {
    "00": "63", "01": "7c", "02": "77", "03": "7b", "04": "f2", "05": "6b", "06": "6f", "07": "c5",
    "08": "30", "09": "01", "0a": "67", "0b": "2b", "0c": "fe", "0d": "d7", "0e": "ab", "0f": "76",
    "10": "ca", "11": "82", "12": "c9", "13": "7d", "14": "fa", "15": "59", "16": "47", "17": "f0",
    "18": "ad", "19": "d4", "1a": "a2", "1b": "af", "1c": "9c", "1d": "a4", "1e": "72", "1f": "c0",
    "20": "b7", "21": "fd", "22": "93", "23": "26", "24": "36", "25": "3f", "26": "f7", "27": "cc",
    "28": "34", "29": "a5", "2a": "e5", "2b": "f1", "2c": "71", "2d": "d8", "2e": "31", "2f": "15",
    "30": "04", "31": "c7", "32": "23", "33": "c3", "34": "18", "35": "96", "36": "05", "37": "9a",
    "38": "07", "39": "12", "3a": "80", "3b": "e2", "3c": "eb", "3d": "27", "3e": "b2", "3f": "75",
    "40": "09", "41": "83", "42": "2c", "43": "1a", "44": "1b", "45": "6e", "46": "5a", "47": "a0",
    "48": "52", "49": "3b", "4a": "d6", "4b": "b3", "4c": "29", "4d": "e3", "4e": "2f", "4f": "84",
    "50": "53", "51": "d1", "52": "00", "53": "ed", "54": "20", "55": "fc", "56": "b1", "57": "5b",
    "58": "6a", "59": "cb", "5a": "be", "5b": "39", "5c": "4a", "5d": "4c", "5e": "58", "5f": "cf",
    "60": "d0", "61": "ef", "62": "aa", "63": "fb", "64": "43", "65": "4d", "66": "33", "67": "85",
    "68": "45", "69": "f9", "6a": "02", "6b": "7f", "6c": "50", "6d": "3c", "6e": "9f", "6f": "a8",
    "70": "51", "71": "a3", "72": "40", "73": "8f", "74": "92", "75": "9d", "76": "38", "77": "f5",
    "78": "bc", "79": "b6", "7a": "da", "7b": "21", "7c": "10", "7d": "ff", "7e": "f3", "7f": "d2",
    "80": "cd", "81": "0c", "82": "13", "83": "ec", "84": "5f", "85": "97", "86": "44", "87": "17",
    "88": "c4", "89": "a7", "8a": "7e", "8b": "3d", "8c": "64", "8d": "5d", "8e": "19", "8f": "73",
    "90": "60", "91": "81", "92": "4f", "93": "dc", "94": "22", "95": "2a", "96": "90", "97": "88",
    "98": "46", "99": "ee", "9a": "b8", "9b": "14", "9c": "de", "9d": "5e", "9e": "0b", "9f": "db",
    "a0": "e0", "a1": "32", "a2": "3a", "a3": "0a", "a4": "49", "a5": "06", "a6": "24", "a7": "5c",
    "a8": "c2", "a9": "d3", "aa": "ac", "ab": "62", "ac": "91", "ad": "95", "ae": "e4", "af": "79",
    "b0": "e7", "b1": "c8", "b2": "37", "b3": "6d", "b4": "8d", "b5": "d5", "b6": "4e", "b7": "a9",
    "b8": "6c", "b9": "56", "ba": "f4", "bb": "ea", "bc": "65", "bd": "7a", "be": "ae", "bf": "08",
    "c0": "ba", "c1": "78", "c2": "25", "c3": "2e", "c4": "1c", "c5": "a6", "c6": "b4", "c7": "c6",
    "c8": "e8", "c9": "dd", "ca": "74", "cb": "1f", "cc": "4b", "cd": "bd", "ce": "8b", "cf": "8a",
    "d0": "70", "d1": "3e", "d2": "b5", "d3": "66", "d4": "48", "d5": "03", "d6": "f6", "d7": "0e",
    "d8": "61", "d9": "35", "da": "57", "db": "b9", "dc": "86", "dd": "c1", "de": "1d", "df": "9e",
    "e0": "e1", "e1": "f8", "e2": "98", "e3": "11", "e4": "69", "e5": "d9", "e6": "8e", "e7": "94",
    "e8": "9b", "e9": "1e", "ea": "87", "eb": "e9", "ec": "ce", "ed": "55", "ee": "28", "ef": "df",
    "f0": "8c", "f1": "a1", "f2": "89", "f3": "0d", "f4": "bf", "f5": "e6", "f6": "42", "f7": "68",
    "f8": "41", "f9": "99", "fa": "2d", "fb": "0f", "fc": "b0", "fd": "54", "fe": "bb", "ff": "16"
}


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

# Função que gera um array com 11 sub-chaves 
# Recebe a chave como string
# Retorna um array com 11 matrizes 4x4 representando as sub-chaves
def key_expansion(key):
    sub_keys = []
    words = []
    init_round_key = get_bytes(key)[0]
    sub_keys.append(init_round_key)
    for i in range(4):
        column = []
        for j in range(4):
            column.append(init_round_key[j][i])
        words.append(column)
    
    for i in range(4, 44):
        temp = words[i-1]
        if (i % 4 == 0):
            temp = SubBytes (RotWord(temp)) ^ Rcon[i/4]
        words.append( words[i-4] ^ temp)

        
# Função de substituição de matriz
# Recebe a matriz a ser substituida
# Retorna uma nova matriz com os valores corresppondentes na S_BOX
def SubBytes(matrix):
    new = []
    for i in range(4):
        column = []
        for j in range(4):
            column.append(S_BOX[hex(matrix[i][j])[2:4]])
        new.append(column)
    return new

# Função de mudança de linhas de matriz
# Recebe uma matriz
# Retorna uma nova matriz, com as linhas permutadas adequadamente segundo o algoritmo 
def ShiftRows(matrix):
    pass

def RotWord():
    pass

def Rcon():
    pass

key = input("key: ")
while len(key) != 16:
    key = input("key: ")



# keys = key_expansion(key)



# Testes pra saber se o add_round_key e get_bytes funcionam
key = get_bytes(key)[0] # Initial round key
text = get_bytes(text)
print(SubBytes(text[0]))


text = input("plain text: ")

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
            temp = SubWord (RotWord(temp)) ^ Rcon[i/4]
        words.append( words[i-4] ^ temp)

        
def SubWord():
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
# key = get_bytes(key)[0] # Initial round key
# text = get_bytes(text)
# print(key)
# print(text[0])
# print(add_round_key(text[0], key))

key_expansion(key)
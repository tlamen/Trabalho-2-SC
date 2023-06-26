text = input("")

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

print(get_bytes(text))


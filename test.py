bytes_data = b'\x01\x02\x03'
exponent = 3
modulus = 5

# Convert bytes_data to an integer
integer_data = int.from_bytes(bytes_data, byteorder='big')

print(integer_data)
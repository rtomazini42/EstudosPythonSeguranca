import hashlib

arquivo1 = 'hashs/A.txt'
arquivo2 = 'hashs/B.txt'

hash1 =  hashlib.new('ripemd160')
hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())


if hash1.digest() != hash2.digest():
    print(f'O arquivo: {arquivo1} é diferente do {arquivo2}')
else:
    print(f'O arquivo: {arquivo1} é igual ao {arquivo2}')

print(hash1.digest())
print(hash2.digest())

import random
import string

tamanho = 32

chars = string.ascii_letters + string.digits + 'çÇãÃ!@#$%¨&*()-+;.,?><[]{}'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))

import os


print("." * 50)
os.system('color 0d')
ip_ou_host = input("Digite o host ou IP para verificar: ")
os.system('ping -n 6 {}'.format(ip_ou_host))
print("-" * 50)

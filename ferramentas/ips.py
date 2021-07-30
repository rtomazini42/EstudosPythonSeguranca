import ipaddress

ip = '192.168.0.1'

iprede = '192.168.0.0/24'

endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(iprede)
#rede = ipaddress.ip_network(iprede, strict = False)

for ip in rede:
    print(ip)

# NMAP Carnivoro
# Autor Sixth Hunter
# 23/07/2020
print("NMAP CARNIVORO")
print("Sixth Hunter")
print("[1] - PORT SCANNER")

import socket
import sys

portas = [80, 443, 21, 22, 23, 25, 3306]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
for porta in portas:
    if sock.connect_ex((sys.argv[1], porta)):
        print("Porta ", porta, "aberta")

print("CONCLUÍDO")
sock.close

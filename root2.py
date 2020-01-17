print("Введите путь до ssh-key")
json_file = str(input())
with open(json_file, "r") as read_file:
    for line in read_file:
            f = open('authorized_keys', 'w')
            f.write(line)


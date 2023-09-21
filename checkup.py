import os, glob


server_dict = {}


def check_folders(folder):
    for name in os.listdir(folder):
        if name.endswith(".log"):
            file = open("".join((folder, "/", name)))
            content = file.read()
            server_list = content.split("\n")
            for server in server_list:
                data = server.split(":")
                if data[0] in server_dict:
                    server_dict[data[0]] = (server_dict[data[0]][0] + int(data[1]), server_dict[data[0]][1] + "+" + data[1])
                else:
                    server_dict[data[0]] = ( int(data[1]), data[1])
            file.close()
        else:
            new_path = "".join((folder, "/", name))
            check_folders(new_path)

if __name__ == "__main__":
    folder_name = "log"
    check_folders(folder_name)
    for key, value in server_dict.items():
        print(key + ": " + str(value[0]) + " (" + value[1] + ")")

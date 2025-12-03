#1
# ip = ["10.0.0.1", "10.0.0.2", "10.0.0.1", "192.168.1.10"]
# print(set(ip))

#2
# words = {"root", "admin", "test"}
# words.add("hacker")
# words.remove("test")
# print(words)

#3
# ports = {21, 22, 23, 25}
# user = int(input("Vvedi port: "))
# if user in ports:
#     print("Port zapreshen")
# else:
#     print(user)

#4
# domen1 = {"mal.com", "bad.net"}
# domen2 = {"bad.net", "xevil.org"}
# print(domen2.difference(domen1))

#5
# white_list = {"alice", "bob", "root"}
# # black_list = {"root", "admin"}
# # print(white_list.intersection(black_list))

#6
# a = {"CVE-1", "CVE-2"}
# b = {"CVE-2", "CVE-3"}
# print(a.union(b))

#7
# admin = {"read", "write", "delete"}
# user = {"read", "download"}
# admin1 = admin.difference(user)
# user1 = user.difference(admin)
# admin1.update(user1)
# print(admin1)

#8
# all_passwords = ["123", "qwerty", "test", "123", "qwerty", "admin"]
# banned = {"test"}
# result = {p for p in all_passwords if p not in banned}
# print(result)

#9
# global_ips = {"10.0.0.1", "10.0.0.2", "192.168.1.1"}
# local_ips  = {"10.0.0.2", "10.0.0.3"}
# result = local_ips & global_ips
# print(result)

#10
# logs = ["scan", "debug_mode", "scan", "connect", "debug_info"]
# result = {cmd for cmd in logs if "debug" not in cmd}
# print(result)
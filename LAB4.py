my_list=["tomer",23,"tomerhakak15@gmail.com","0522503603"]
print("full name: " + my_list[0] + "\nage: " + str(my_list[1]) +"\nemail: " + my_list[2] +"\nphone: " + my_list[3])

ip_list=["10.0.0.1","10.0.0.2"]
print(ip_list)
ip_list.append("10.0.0.3")
ip_list.append("10.0.0.4")
ip_list.append("10.0.0.5")
print(ip_list)
ip_list.pop(2)
print("ip list is: " + str(len(ip_list)) + "\nand the ip list: " + str(ip_list))
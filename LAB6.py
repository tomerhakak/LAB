d='''
menu:
-----
1.Insert Number and ** it by 3
2.Insert 4 Ips to a list and print it
3.Insert 4 Entries to DNS_Dictionary and print it
4.Check if a string is polindrom 
-----
'''
print(d)

a=input("you will tell him to insert 1-4 only!\n")
if(a=="1"):
    print("The number that came out after the calculation is: "  + str((int(input("Enter a number")))**3))
elif(a=="2"):
    list_ip=[]
    list_ip.append(input("Enter new ip: "))
    list_ip.append(input("Enter new ip: "))
    list_ip.append(input("Enter new ip: "))
    list_ip.append(input("Enter new ip: "))
    print("The new list:\n-------\n" + str(list_ip))
elif(a=="3"):
    dns_dict={}  
    dns_dict.update({input("Enter a url: "): input("Enter ip ")}) 
    dns_dict.update({input("Enter a url: "): input("Enter ip ")}) 
    dns_dict.update({input("Enter a url: "): input("Enter ip ")}) 
    dns_dict.update({input("Enter a url: "): input("Enter ip ")}) 
    print("The new dns_dict:\n-------\n" + str(dns_dict))
elif(a=="4"):
    word=input("Enter a word: ")
    if (word == word[::-1]):
        print("This is polindrom!")
    else: 
        print("This isn't polindrom!")    
else:
    print("Enter 1-4 only!!!..")       
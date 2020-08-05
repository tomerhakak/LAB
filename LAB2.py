
print("now we will calclate your marketing:\n--------------\nTomato=3 NIS\nCucumber=2 NIS\ncola=5 NIS\nchickin=20  NIS\n--------------  ")

Tomato=int(input("Enter how many tomatos ? "))
Cucumber=int(input("Enter how many Cucumber ? " ))
cola=int(input("Enter how many cola ? "))
chickin=int(input("Enter how many chickin ? "))

print("\n----------- \nsummary of your order:\n----------- \nTomatos:" + str(Tomato) +  "\nCucumbers:" + str(Cucumber) + "\ncolas:" + str(cola) + "\nchickins:" + str(chickin))

summary=(Tomato*3)+(Cucumber*2)+(cola*5)+(chickin*20)
print("\nYou have to pay:" +str(summary) + " NIS without tax")
print("\nYou have to pay: " + str("%.2f" % (summary*1.17)) + " NIS with tax")

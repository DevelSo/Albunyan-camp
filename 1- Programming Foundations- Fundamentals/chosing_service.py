
# this small program in merge of condition and input
# which will push the cutomer to chose one service and then give him the ticket number
print("Hi there! i hope you'll enjoy our services")

#services types
def service_type(service):
    if service == "1":
        print("This the number of your ticket 145356789")
    elif service == "2":
        print("This the number of your ticket 245356789")
    else:
        print("Please enter a valid number")

#taking the argument (number of service)
number = input("We have two services... \n1- vip will cost you 10$ \n2- normal will cost you 5$ \nPlease chose '1' or '2' ")

service_type(number)

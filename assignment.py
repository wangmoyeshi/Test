age = int(input("enter your age:"))
status = input("are you a student?(yes or no):")

if age <= 12:
    print("you are eligible for a discount on the movie ticket")
elif 13 <= age <= 18 and status == "yes":
    print("you are eligile fora discount on the movie ticket")
else:
    print("you are not eligible for discount")
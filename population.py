pop = int(input("Enter Population number: "))

if pop > 1000000 :
    print("Highly Populated")
elif pop >= 100000 and pop <= 1000000 :
    print("Moderately Populated")
elif pop < 100000 :
    print("Low Population")
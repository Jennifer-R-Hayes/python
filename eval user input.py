## Eval. user input value

x = str(raw_input("Do you want to add, subtract or multiply? "))

if x == "add":
    val1 = int(raw_input("Enter an integer"))
    val2 = int(raw_input("Enter an integer"))
    ans = val1 + val2
    print "Your answer is", ans
elif x == "subtract":
    val1 = int(raw_input("Enter an integer"))
    val2 = int(raw_input("Enter an integer"))
    ans = val1 - val2
    print "Your answer is", ans
else:
    val1 = int(raw_input("Enter an integer"))
    val2 = int(raw_input("Enter an integer"))
    ans = val1 * val2
    print "Your answer is", ans
        

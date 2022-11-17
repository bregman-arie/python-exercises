Solutions:

    def double_number(n):
        return lambda x : x * n
 
    result = double_number(2)
    print("The double number of 11 =", result(11))
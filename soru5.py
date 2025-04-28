my_list = [5, 2, -5, 10, 23, -21, 78, 1, -876]
if not my_list:
    biggest_int = None
else:
    biggest_int = my_list[0]
    for number in my_list:
        if number > biggest_int:
            biggest_int = number
print("En büyük sayı:", biggest_int)



  
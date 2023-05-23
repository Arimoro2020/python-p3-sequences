#!/usr/bin/env python3

def print_fibonacci(length):
        my_list = []
        for i in range(length):
            if i <= 1:
                    my_list.append(i)

            else:
                f_minus_2 = my_list[i - 2]
                f_minus_1 = my_list[i - 1]
                f = f_minus_2 + f_minus_1
                my_list.append(f)

        print(my_list)
                    
            

        
  


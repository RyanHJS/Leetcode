def DecimalToBinary(num):
     
    if num >= 1:
        temp = num // 2
        print(f'Temp is: {temp}')
        DecimalToBinary(temp)
    new = num % 2
    print(f'Num is: {num}, new is: {new}')
    # print(new, end = '?')
    
# Driver Code
if __name__ == '__main__':
     
    # decimal value
    dec_val = 5
     
    # Calling function
    DecimalToBinary(dec_val)

    print()
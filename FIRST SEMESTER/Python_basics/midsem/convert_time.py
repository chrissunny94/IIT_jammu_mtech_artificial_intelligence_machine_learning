def convert24(str1):
     
    if str1[-2:] == "AM" and str1[:2] == "12":
        return "00" + str1[2:-2]
         
    elif str1[-2:] == "AM":
        return str1[:-2]
     
    elif str1[-2:] == "PM" and str1[:2] == "12":
        return str1[:-2]
         
    else:
         
        return str(int(str1[:2]) + 12) + str1[2:8]

Input_time=(input())
# print(Input_time)
# broken_time = Input_time.split(':')

print(convert24(Input_time))
def Even_Odd_Sum(List_):
    count = 1
    Even_sum = 0
    Odd_sum = 0
    #print(List_)
    for i in List_:
        if(count%2 == 0):
            Even_sum = Even_sum + i
        else:
            Odd_sum = Odd_sum + i
        count+=1
    if (Even_sum >= Odd_sum):
        Max = Even_sum
    else:
        Max = Odd_sum
    #print(Odd_sum , Even_sum)
    return Max

def main():
    number_of_elements = int(input())
    string_of_elemenets = str(input())
    res = string_of_elemenets.strip('][').split(' ')
    final_list = []
    for element in res:
        final_list.append(int(element))
    print(Even_Odd_Sum(final_list))

if __name__ == "__main__":
    main()
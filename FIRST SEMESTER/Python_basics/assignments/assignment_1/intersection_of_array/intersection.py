def intersection(lst1, lst2):
    #lst3 = [value for value in lst1 if value in lst2]
    lst3 = list(set(lst1) & set(lst2))
    return lst3



def main():
    # creating an empty list
    inp_lst_1 = ""
    # number of elements as input
    inp_list_1_number = int(input())
    inp_lst_1 = str(input()) 
    
    # Converting string to list
    res_list_1 = inp_lst_1.strip('][').split(' ')
    final_list_1 = []
    for element in res_list_1:
        final_list_1.append(int(element))
    
    # creating an empty list
    inp_lst_2 = ""
    # number of elements as input
    inp_list_2_number = int(input())
    inp_lst_2 = str(input()) 
    
    # Converting string to list
    res_list_2 = inp_lst_2.strip('][').split(' ')
    final_list_2 = []
    for element in res_list_2:
        final_list_2.append(int(element))

    intersection_list =  intersection(final_list_1,final_list_2)
    #print(intersection_list)
    intersection_list_string = ''
    element_1 = True
    for element in intersection_list:
        if(element_1):
            intersection_list_string =  str(element)
            element_1 = False
        else:
            intersection_list_string = intersection_list_string + ' ' + str(element)

    print(intersection_list_string)
    

    
if __name__ == "__main__":
    main()
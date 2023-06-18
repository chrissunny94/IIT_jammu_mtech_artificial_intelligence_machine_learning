

def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i 
    return num

def count_frequent(List,element):
    counter = 0
    for i in List:
        #print(i, element)
        if(element == int(i)):
            counter +=1 
    return counter



def main():
    # creating an empty list
    inp_lst = ""
    # number of elements as input
    inp_lst = str(input()) 
    occurance_element=int(input())
    # Converting string to list
    res = inp_lst.strip('][').split(',')
    final_list = []
    for element in res:
        final_list.append(int(element))
    print(count_frequent(final_list,occurance_element)) 


    
if __name__ == "__main__":
    main()
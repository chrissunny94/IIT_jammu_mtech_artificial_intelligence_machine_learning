
def Maximum(List_):
    return max(List_)

def Minimum(List_):
    return min(List_)





def main():
    number_of_elements = int(input())
    string_of_elemenets = str(input())
    res = string_of_elemenets.strip('][').split(' ')
    final_list = []
    for element in res:
        final_list.append(int(element))
    print(Maximum(final_list))
    print(Minimum(final_list))


if __name__ == "__main__":
    main()
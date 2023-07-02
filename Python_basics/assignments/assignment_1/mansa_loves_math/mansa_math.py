import sys

class Mansa(object):
    def solve(self, input_string):
        l = len(input_string)
        if l == 1:
            if int(input_string) % 8 == 0:
                return "YES"
            else:
                return "NO"
        elif l == 2:
            if int(input_string) % 8 == 0 or int(input_string[::-1]) % 8 == 0:
                return "YES"
            else:
                return "NO"

        hm = [0 for _ in range(10)]
        for char in input_string:
            hm[int(char)] += 1

        for i in range(0, 1000, 8):
            copy = list(hm)
            s = "00" + str(i)
            j = -1
            while j >= -3:  # check 3 digits
                d = int(s[j])
                if copy[d] <= 0: break
                copy[d] -= 1
                j -= 1
            if j == -4:
                return "YES"
        return "NO"


if __name__ == "__main__":
    
    f = sys.stdin
    Number_testcases = int(f.readline().strip())
    s=""
    for t in range(Number_testcases):
        input_string = f.readline().strip()
        s =s+ "%s\n" % (Mansa().solve(input_string))
    print( s)
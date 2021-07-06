import math
import itertools as it

def prime(temp):
    flag = 0
    temp2 = temp.copy()
    for word in temp:
        if (word % 2 == 0 or word % 5 == 0 or word % 7 == 0 or word % 11 == 0):
            temp2.remove(word)
            continue
        for i in range(11, math.isqrt(word), 2):
            if (word % i == 0):
                flag = 1
                break
        if (flag or word == 1):
            temp2.remove(word)
        flag = 0
    #print(temp2)
    return int(math.fsum(temp2))

def to_int(item):
    count = 0;
    for i in range(len(item)):
        count += int(item[i])
        if (i == 0):
            word = item[i]
            continue
        word += item[i]
    if (count % 3 == 0):
        flag = 1
    else:
        flag = 0
    word = int(word)
    return word, flag

def permutation(num, n):
    temp = list()
    case = list() 
    ans = list()
    for i in range(n):
        perm = it.permutations(num[i])
        for j, item in enumerate(perm):
            if (j == 0):
                temp.append(item)
                word, flag = to_int(item)
                if (flag):
                    break
                else:
                    case.append(word)
                    continue
            if (item not in temp):
                temp.append(item)
                word, flag = to_int(item)
                case.append(word)
        if (flag):
            ans.append(0)
        else:
            ans.append(prime(case))
        temp.clear()
        case.clear()
    return ans
        

if __name__ == '__main__':
    n = int(input())
    num = list()
    for i in range(n):
        num.append(input())
    ans = permutation(num, n)
    for value in ans:
        print(value)

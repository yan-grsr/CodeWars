# https://www.codewars.com/kata/546dba39fa8da224e8000467/train/python

def run_length_encoding(s):
    rle_list = []
    j = 0
    if s == '':
        return rle_list
    
    rle_list.append([1,s[0]])

    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            rle_list[j][0] += 1
        else:
            j += 1
            rle_list.append([1,s[i]])

    return rle_list

if __name__ == '__main__':
    print(run_length_encoding(''))
    print(run_length_encoding('abc'))
    print(run_length_encoding('aaaabbbccd'))
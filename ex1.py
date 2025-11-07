def find(s, n):
# write your implementation here
    pair = [0,0]
    for first_index in range(0,len(s)-1):
        for second_index in range(1+first_index,len(s)):
            if s[first_index] + s[second_index] == n:
                pair[0] = first_index
                pair[1] = second_index
                return pair
    return None
print(find([2,7,11,15],9))

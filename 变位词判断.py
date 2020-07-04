def solution4(s1, s2):  #总操作次数 2N+26 数量级为O(N)，但需要更多的储存空间

    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos]+=1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos]+=1

    stillok = True
    j = 0

    while j < 26 and stillok:
        if c1[j] == c2[j]:
            j+=1
        else:
            stillok = False

    return stillok

print(solution4("apple", "pleap"))

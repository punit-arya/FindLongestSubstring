def solution(S):
    # Implement your solution here
    pass
    # S = "abacb"
    if not S:
        return 0
    mySet = set(S)
    myDict = {}
    for c in mySet:
        myDict[c] = 0
    # print(mySet, myDict)
    myList = []
    for i in range(len(S)):
        length = 2
        for j in range(length, len(S) + 1, 2):
            if i + j > len(S):
                continue
            candidate = S[i:i + j]
            # print("candidate:", candidate)
            length += 2
            candidateSet = set(candidate)
            # print("candidateSet:", candidateSet)
            for c in candidateSet:
                if candidate.count(c) % 2:
                    break
            else:
                myList.append(candidate)
                # print("myList:", myList)
    # print(myList)
    if myList:
        return max(list(map(len, myList)))
    else:
        return 0

if __name__ == "__main__":
    print("solution('abacb'):", solution("abacb"))
    print("solution('zthtzh'):", solution("zthtzh"))
    print("solution(''):", solution(""))
    print("solution('a'):", solution("a"))
    print("solution('ab'):", solution("ab"))
    print("solution('aa'):", solution("aa"))
    print("solution('abcdabcd'):", solution("abcdabcd"))
    print("solution('baaadadabcc'):", solution("baaadadabcc"))
    print("solution('abaaadadabcca'):", solution("abaaadadabcca"))

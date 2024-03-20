def solution(word):
    length = len(word)
    scores = { 'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4 }
    answer = 0
    for i in range(length):
        nums = 1
        total = 0
        nums *= scores[word[i]]
        total += (nums+1)
        print(nums, total)
        for j in range(i+1, 5):
            nums *= 5
            total += nums
        print("total", total)
        answer += total
        
    print(answer)
    return answer
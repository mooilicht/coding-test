def solution(answers):
    answer1 = [1, 2, 3, 4, 5]
    answer2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0, 0, 0]
    
    while len(answers) > len(answer1):
        answer1 += answer1
    
    while len(answers) > len(answer2):
        answer2 += answer2
        
    while len(answers) > len(answer3):
        answer3 += answer3
        
    for i in range(len(answers)):
        if answers[i] == answer1[i]:
            count[0] += 1
        if answers[i] == answer2[i]:
            count[1] += 1
        if answers[i] == answer3[i]:
            count[2] += 1
            
    answer = []
    for i in range(len(count)):
        if max(count) == count[i]:
            answer.append(i+1)
    return answer
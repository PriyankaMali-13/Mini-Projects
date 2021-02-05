#Accenture Coding Question
#Find the number of elements having absolute difference of less than equal to 'diff' with 'num'.
def FindCount(n,arr,num,diff):
    count = 0
    for i in range(len(arr)):
        if abs(num-arr[i]) <= diff:
            count +=1
    if count == 0:
        return -1
    else:
        return count

n = int(input())
arr = list(map(int, input().split()))
num = int(input())
diff = int(input())

print(FindCount(n,arr,num,diff))
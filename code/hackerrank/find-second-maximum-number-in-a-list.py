'''
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

Sample Input:
5
2 3 6 6 5

Sample Output:
5

Explanation:
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(set(arr))
    scores.remove(max(scores))
    print(max(scores))

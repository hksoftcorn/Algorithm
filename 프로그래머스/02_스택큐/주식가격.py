"""
문제 설명 : 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.
컨셉 : 1) Stack 2) 뒤에서부터 꺼내어 앞의 수와 비교합니다.

"""

def solution(prices):
    answer = [0]
    price = prices.pop()    # prices의 길이는 2이상 100000 이하입니다.

    while prices:
        prev_price = prices.pop()


    return answer
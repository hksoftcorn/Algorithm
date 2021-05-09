
wtoi = {
    'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
}

def solution(s):
    answer = ''
    tmp = ''
    for char in s:
        if char.isdigit():
            answer += char
        else:
            tmp += char

        if tmp in wtoi:
            answer += str(wtoi[tmp])
            tmp = ''

    return answer
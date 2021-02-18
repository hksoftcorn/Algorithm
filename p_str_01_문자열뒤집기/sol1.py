"""
# 1.
# 2. 직접
# 3. 재귀
"""

# 슬라이싱
word = 'abcde'
print(word[::-1])


# while문
idx = len(word) - 1
r_word = ''
while idx >= 0:
    r_word += word[idx]
    idx -= 1
print(r_word)


# 재귀
def solv(word):
    idx = len(word) - 1
    # base(escape) code
    if idx == 0:
        return word[idx]
    return word[idx] + solv(word[:idx])





# for w in range(len(word)//2):
#     word




#


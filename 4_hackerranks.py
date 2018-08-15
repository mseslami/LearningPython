# https://www.hackerrank.com/challenges/the-minion-game/problems
'''
for both users, make substrings with all possible length,
then consider if substring starts with a vowel or not.
for every accepted substring, user gets a +1 point.
compare user's score and print max score.
'''

inputstring = input().upper()
# inputstring = "BANANA"


# count and return stuart's score.:
def stuart_score():
    stuartscore = 0
    for length in range(1, len(inputstring) + 1):  # return length of substring
        for index in range(len(inputstring) - length + 1):
            # print(inputstring[index])
            if not isvowel(inputstring[index]):
                substring = inputstring[index:index + length]
                # print(substring)
                stuartscore += 1

    return (stuartscore)


# count and return kevins's score:
def kevin_score():
    kevinscore = 0
    for length in range(1, len(inputstring) + 1):  # return length of substring
        for index in range(len(inputstring) - length + 1):
            # print(inputstring[index])
            if isvowel(inputstring[index]):
                substring = inputstring[index:index + length]
                # print(substring)
                kevinscore += 1

    return (kevinscore)


# return true if given char (start of the substring) is vowel
def isvowel(mychar):
    is_vowel = False
    for char in "AEIOU":
        if mychar == char:
            is_vowel = True
    return is_vowel


if __name__ == '__main__':

    stuartscore = stuart_score()
    kevinscore = kevin_score()

    if stuartscore > kevinscore:
        print('Stuart ', stuartscore)
    elif stuartscore < kevinscore:
        print('Kevin ', kevinscore)
    else:
        print('Draw')

# def minion_game(inputstring):
#     # your code goes here
#     stuartscore = 0
#     for length in range(1, len(inputstring) + 1):  # return length of substring
#         for index in range(len(inputstring) - length + 1):
#             # print(inputstring[index])
#             is_vowel = False
#             for char in "AEIOU":
#                 if inputstring[index] == char:
#                     is_vowel = True
#
#             if not is_vowel:
#                 # if not isvowel(inputstring[index]):
#                 substring = inputstring[index:index + length]
#                 # print(substring)
#                 stuartscore += 1
#     kevinscore = 0
#     for length in range(1, len(inputstring) + 1):  # return length of substring
#         for index in range(len(inputstring) - length + 1):
#             # print(inputstring[index])
#             is_vowel = False
#             for char in "AEIOU":
#                 if inputstring[index] == char:
#                     is_vowel = True
#
#             if is_vowel:
#             # if isvowel(inputstring[index]):
#                 substring = inputstring[index:index + length]
#                 # print(substring)
#                 kevinscore += 1
#
#     if stuartscore > kevinscore:
#         return ('Stuart ' + str(stuartscore))
#     elif stuartscore < kevinscore:
#         return ('Kevin ' + str(kevinscore))
#     else:
#         return ('Draw')
#
#
# if __name__ == '__main__':
#     print(minion_game("BANANA"))

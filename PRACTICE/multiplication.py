import random


# generate a random exam score from 0 - 100
def random_score():
    number_list = []
    k = 1
    while k <= 5:
        number = random.randint(0, 100)
        number_list.append(number)
        k += 1
    print(number_list)
    return number_list


score_list = random_score()
print(sum(score_list))

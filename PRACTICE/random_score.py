import random


# generate a random exam score from 0 - 100
def random_score():
    number_list = []
    k = 1
    while k <= 1000:
        number = random.randint(0, 100)
        number_list.append(number)
        number_list.sort()
        k += 1
    return number_list


# calculate the mean value of the generated scores
def mean_value(lst):
    mean = sum(lst) / len(lst)
    return mean


scores_list = random_score()
print("\nGENERATED SCORES: ", scores_list)

result = mean_value(scores_list)
print("\n\nTHE MEAN SCORE IS: ", result)

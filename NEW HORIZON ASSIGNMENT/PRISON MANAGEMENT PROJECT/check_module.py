import random


# generate a random word from list of words
def random_word():
    list_items = ["biology", "seven", "savage", "happy", "messi", "apple", "banana", "cherry", "grape", "orange",
                  "kiwi", "mango", "watermelon", "strawberry", "pineapple", "Python", "Java", "JavaScript", "Swift",
                  "Go", "Ruby", "PHP", "Rust", "TypeScript", "Kotlin", "Perl", "Haskell", "Scala", "Dart", "Lua",
                  "MATLAB", "Ballet", "Hip", "Salsa", "Tango", "Contemporary", "Breakdown", "Ballroom", "Swing",
                  "Bollywood", "Flamenco", "Tap", "Zomba", "Jazz", "Street", "Folk", "Belly", "Trumping", "Samba",
                  "Irish", "Pole", "Zeus", "Athena", "Thor", "Odin", "Ra", "Horus", "Vishnu", "Shiva", "Loki", "Anubis",
                  "Apollo", "Aphrodite", "Artemis", "Hera", "Isis", "Jupiter", "Neptune", "Mars", "Hades", "Hermes",
                  "Football", "Basketball", "Tennis", "Soccer", "Cricket", "Baseball", "Golf", "Rugby", "Hockey",
                  "Volleyball", "Badminton", "Table Tennis", "Swimming", "Athletics", "Boxing", "Martial Arts",
                  "Gymnastics", "Cycling", "Skiing", "Snowboarding"]
    return random.choice(list_items)


# give hint to player the length of the word
def new_guess_output(word):
    length = 1
    n = []
    while length <= len(word):
        k = '_ '
        n.append(k)
        length += 1
    print(n)
    return n


# get every letter in the fixed variable and compare if user input is in the word
def linear_search(word, target):
    # Get all the index in the word
    for i in range(0, len(word)):
        if word[i] == target:
            return i
    return None


# update the hint if user finds a correct letter
def reload(target, word, load):
    for i in range(len(word)):
        if word[i] == target:
            load[i] = target
    return load


# track all the index of the actual word
def repeated(word, target):
    track_value = {}
    count = 0
    for i in word:
        track_value[i] = track_value.get(i, 0) + 1
    for k, v in track_value.items():
        if k == target and (count is None or v > count):
            count = v
            return count
    return None

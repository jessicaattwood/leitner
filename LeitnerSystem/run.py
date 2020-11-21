import data

### next time - implement removal of key,value pairs from appropriate dictionaries (use correct() and incorrect()
# as a source for the opposite)

easy = data.easy
medium = data.medium
hard = data.hard
difficulty_options = data.difficulty_options

def correct(k, difficulty):
    if difficulty != hard:
        i = difficulty_options.index(difficulty) + 1
        assign_to = difficulty_options[i]
        coming_from = difficulty
        assign_to[k] = coming_from[k]

def incorrect(k, difficulty):
    if difficulty != easy:
        i = difficulty_options.index(difficulty) - 1
        assign_to = difficulty_options[i]
        coming_from = difficulty
        assign_to[k] = coming_from[k]

def set_difficulty():
    difficulty_setting = str.lower((input("What difficulty setting? Type Easy, Medium or Hard: ")))

    if difficulty_setting == "easy":
        return easy

    elif difficulty_setting == "medium":
        return medium

    elif difficulty_setting == "hard":
        return hard


def quiz():
    '''
    loops through the keys (roman), getting the associated value and performing the quiz questions each loop.
    :return:
    '''

    difficulty = set_difficulty()

    correct_dict = {}
    incorrect_dict = {}

    for key in difficulty.keys():
        value = difficulty.get(key)
        answer = input(value + ": ")

        if answer == key:
            print("correct")
            correct_dict[key] = difficulty[key]

        else:
            print("incorrect")
            incorrect_dict[key] = difficulty[key]

    for key in correct_dict:
        correct(key, difficulty)

    for key in incorrect_dict:
        incorrect(key, difficulty)



quiz()
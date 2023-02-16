# add function
def add(number1, number2):
    answer = number1 + number2
    return answer


# subtract function
def subtract(number3, number4):
    answer1 = number3 - number4
    return answer1


# multiply function
def multiply(number3, number4):
    answer2 = number3 * number4
    return answer2


# divide function
def divide(number3, number4):
    answer3 = number3 / number4
    return answer3


def add_lots(*numbers):
    answer = 0
    for n in numbers:
        answer += n
    # make sure return is indented
    return answer


# test
if __name__ == '__main__':
    answer = add(1, 2)
    answer1 = subtract(1, 2)
    answer2 = multiply(1, 2)
    answer3 = divide(1, 2)
    print(answer, answer1, answer2, answer3)

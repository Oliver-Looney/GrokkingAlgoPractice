def BadCountDown(i):
    print(i)
    BadCountDown(i - 1)


def CountDown(i):
    print(i)
    if i <= 0:
        return
    else:
        CountDown(i - 1)


CountDown(10)

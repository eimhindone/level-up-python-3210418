def getprime(number):
    myprime = []
    curnum = 2

    while curnum <= number:
        if number % curnum == 0:
            myprime.append(curnum)
            number = number // curnum
        else:
            curnum += 1
    return myprime
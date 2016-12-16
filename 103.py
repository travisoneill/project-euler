def is_special(sett):
    lst = sorted(sett)
    if lst[0] + lst[1] < lst[-1]:
        return False

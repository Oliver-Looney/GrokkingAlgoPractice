voted = {}


def checkVoter(name):
    value = voted.get(name)
    if value:
        return False
    else:
        voted[name] = True
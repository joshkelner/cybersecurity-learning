import hashlib
import requests
from enum import Enum
import getpass
import re

 

def checkPwnedAPI(password):
    hashedPassword = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5 = hashedPassword[:5]
    suffix = hashedPassword[5:]
    url = f"https://api.pwnedpasswords.com/range/{first5}"
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError("HaveIBeenPwned API Request Failed")
    for line in response.text.splitlines():
        hash, count = line.split(':')
        if hash == suffix:
            return int(count)
    return 0

class Problem(Enum):
    SHORT = 1
    UPPER = 2
    LOWER = 3
    NUMBER = 4
    SPECIAL = 5

def checkStrength(password):
    problemList = []
    if len(password) < 8:
        problemList.append(Problem.SHORT)
    if not re.search(r"[A-Z]", password):
        problemList.append(Problem.UPPER)
    if not re.search(r"[a-z]", password):
        problemList.append(Problem.LOWER)
    if not re.search(r"\d", password):
        problemList.append(Problem.NUMBER)
    if not re.search(r"[!@#$%^&*()\{\}\[\],./<>?:;|\-_+=`~\\]", password):
        problemList.append(Problem.SPECIAL)
    return problemList
def getRating(problemList):
    rating = ''
    match len(problemList):
        case 0: 
            rating = 'STRONG'
        case x if x < 3:
            rating = 'MODERATE'
        case _:
            rating = 'WEAK'
    return rating
def printResponse(breach, problemList, rating):
    response = f"\nYour password is rated: {rating}\n"
    if rating =='STRONG':
        response += "\nYour password meets complexity standards! Congrats!"
    else:
        response += "\nPlease consider the following suggestion(s):"
        for problem in problemList:
            if problem == Problem.SHORT:
                response += "\n- Your password should be at least 8 characters"
            elif problem == Problem.UPPER:
                response += "\n- Your password should contain at least one upper case character"
            elif problem == Problem.LOWER:
                response += "\n- Your password should contain at least one lower case character"
            elif problem == Problem.NUMBER:
                response += "\n- Your password should contain at least one number"
            elif problem == Problem.SPECIAL:
                response += "\n- Your password should contain at least one special character"
    if breach == 0:
        response += "\n\nYour password has not appeared in known data breaches according to HaveIBeenPwned. \nThis data is up to date with the current HaveIBeenPwned dataset.\n"
    else:
        response += f"\n\nWARNING: Your password has been detected {breach} times in known data breaches according to HaveIBeenPwned.\n Regardless of its strength rating you should consider using a different password.\n"
    print(response)
def main():
    password = getpass.getpass("Please enter your password: ")
    breach = checkPwnedAPI(password)
    problemList = checkStrength(password)
    rating = getRating(problemList)
    printResponse(breach, problemList, rating)

    
    


if __name__ == "__main__":
    main()
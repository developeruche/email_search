import re


# Defining function for validation of username
def reValidateUsername(username):
    return re.search('/^[a-z0-9_-]{3,16}$/', username)

# Defining function for vaildating password


def reValidatePassword(password):
    return re.search('/^[a-z0-9_-]{6,18}$/', password)

# Defining function for validating Hex value


def reValidateHexValue(hexinput):
    return re.search('/^#?([a-f0-9]{3})$/', hexinput)

# Defining function for validateing Email


def reValidateEmail(email):
    return re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)


if __name__ == '__main__':
    inputarray = ['were@gmail.com', 'jjkhdjj@yahoo.com', '0803300229', 'testing@agile.com',
                  'testmailing@thegrate.rt', 'work ', 'working ass a worker', 'uche@gmail.com', 'nweleuchennadavid@gmail.com']
    emails = []

    for i in inputarray:
        print(reValidateEmail(i))
        if reValidateEmail(i):
            emails.append(i)
        else:
            pass

    print(emails)

#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
    password = ''
    for n in range(passLen):
        password += random.choice(string.ascii_uppercase + string.digits)

    return password

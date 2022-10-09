#! python

import string

def upper(yourstr, fromm = string.ascii_lowercase, to = string.ascii_uppercase):
    str = ''
    for f in (yourstr):
        count = -1
        for a in fromm:
            count += 1
            if f == a:
                str += to[count]
                break

    return str

def lower(yourstr):
    return upper(yourstr, string.ascii_uppercase, string.ascii_lowercase)

def mirror(yourstr):
    str = ''
    for f in yourstr:
        if f in string.ascii_lowercase:
            str += upper(f)
        if f in string.ascii_uppercase:
            str += lower(f)

    return str
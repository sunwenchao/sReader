# -*- coding: utf-8 -*-
import re
import string

# email
EMAIL_REGEX = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
email_re = re.compile(EMAIL_REGEX)

def isEmail(em):
    return email_re.match(em) is not None

# password
PWD_REGEX = '^[\w\d]{6,12}$'
pwd_re = re.compile(PWD_REGEX)

def isPassword(pw):
    return pwd_re.match(pw) is not None

# py cookbook p19
def translator(frm='', to='', delete='', keep=None):
    if len(to) == 1:
        to *= len(frm)

    trans = string.maketrans(frm, to)

    if keep is not None:
        allchars = string.maketrans('', '')
        realKeep = keep.translate(allchars, delete)
        delete = allchars.translate(allchars, realKeep)

    def translate(s):
        return s.translate(trans, delete)

    return translate

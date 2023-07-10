__description__ = 'contains the wildcard characters available in redex'
__filename__ = 'wildcards.py'
__author__ = 'Timo Kats'

import string

wildcard = {
    '*': [char for char in string.printable],
    '*num': [char for char in string.digits],
    '*alpha': [char for char in string.ascii_letters],
    '*special': [char for char in string.punctuation],
    '*upper': [char for char in string.ascii_uppercase],
    '*lower': [char for char in string.ascii_lowercase],
    '*space': [char for char in string.whitespace],
    '*punct' : ['.',',','?','!']
}

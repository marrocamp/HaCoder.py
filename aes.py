#!/usr/bin/env python

import string
import random

random = ''.join([random.choice(string.ascii_letters + string.digits) for n in xrange(32)])
print random

import sys

path = '/Users/domantasjurkus/Downloads/csnit/roganlog/roganlog_flask'

if path not in sys.path:
    sys.path.append(path)

# from __init__ import app as application

from app import app
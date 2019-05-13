import os

def handler(context, event):
    return os.environ['RETURNED_TEXT']

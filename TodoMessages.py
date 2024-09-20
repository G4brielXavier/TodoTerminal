from random import choice

# Controlling Messages and Outputs

TagMessages = [
    'Ok!',
    'Okay!',
    'Nice!',
    'Good!',
    'Godlike',
    'WoW!',
    'LoL!',
    'Very Good',
    ':]',
    '(O > -) |3',
    '^_^',
    '✪ ω ✪',
]

Messages = [
    'ERROR_COMMAND',
    'ERROR_TASK',
    'ERROR_TAG',
    'ERROR_FAVOURITE',  
    'ERROR_INPUT_EMPTY',
    'ERROR_LIST_EMPTY',
    'EXCEPTION_NONE'
]

def msg_result(msg):
    print()
    print(msg)
    print()

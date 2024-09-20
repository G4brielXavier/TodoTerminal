from TodoMessages import *
from TodoClass import Todo

from os import system

# task manager instance
todo = Todo()

# function to show terminal info
def initial_info(version):
    print(f'Todo Terminal v{version}')
    print(f'© All rights reserved to Environ')
    print()

# function to control commands inputs
def ipt():
    cmd = input('> ')
    print()

    return cmd

# qk - to create a task quick
def qk():
    todo.quick_task()

# tsk simp - to create a simple task
def tsk_simple_new():
    todo.simple_task()

# tsk vall - view all your tasks
def tsk_view_all():
    todo.view_all()

# tsk mv - view all mini info your tasks
def tsk_miniview():
    todo.minimalist_view()

# tsk bigg - to create a big task
def tsk_bigger_new():
    todo.bigger_task()
    
# tsk remove - to remove a task
def tsk_remove():
    todo.remove_task()
    
# tsk edit - to edit a task
def tsk_edit(): 
    todo.edit_task()

# tsk uniq - to view a specific task
def tsk_uniq():
    todo.view_unique()







def interpreter(cmd):
    match cmd:

        case 'qk':
            qk()
            
        case 'tsk vall':
            tsk_view_all()
            
        case 'tsk mv':
            tsk_miniview()
            
        case 'tsk simp':
            tsk_simple_new()
        
        case 'tsk bigg':
            tsk_bigger_new()
            
        case 'tsk remove':
            tsk_remove()
            
        case 'tsk edit':
            tsk_edit()
            
        case 'tsk uniq':
            tsk_uniq()
        
        case 'cls' | 'clear':
            system('cls')
        
        case _:
            msg_result(f'{Messages[0]} ~ This "{cmd}" not exist or undefined')



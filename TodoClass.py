from TodoMessages import msg_result, TagMessages, choice, Messages

# function to control asks yes or no
def you_want(ask_c):
    print(ask_c)
    answer = input('[Y]es or [N]o : ').lower()
    
    return answer

# function to control asks of options
def you_want_options(ask_c, opt_1, opt_2):
    print(ask_c)
    answer = input(f'[{opt_1[0]}]{opt_1[1:]} or [{opt_2[0]}]{opt_2[1:]}: ')
    
    return answer

# function to manage inputs
def manage_inputs(type_task):
    bas = {}
    
    # set identifier to task
    if type_task == 'Quick Task':
        bas['ID'] = ''
    else:
        answer_id = you_want('you want set a ID to task?')
        if answer_id == 'y':
            print()
            bas['ID'] = input('~ ID: ')
        else:
            bas['ID'] = ''
    
    
    # standard commands
    bas['task_name'] = input('~ task_name: ')
    bas['status'] = 'not done'
    
    # set contents to task
    if type_task == 'Quick Task' or type_task == 'Simple Task':
        bas['content'] = ''
    else:
        bas['content'] = input('~ content: ')
    
    # auto set
    bas['type'] = type_task

    # TAGS
    bas['tag'] = ''
    
    # set favourite
    if type_task == 'Quick Task':
        bas['favourite'] = False
    else:
        print()
        answer_favourite = you_want(f'you want set "{bas['task_name']}" as your favourite?')
        if answer_favourite == 'y':
            bas['favourite'] = True
        else:
            bas['favourite'] = False
            
    return bas

# function to adjust content of a bigger task
def adjust_content(content):
    print()
    print(f' | ~ content: ')
    print(f' |      {content}')
    print()

# function to verify conditionals and set a correct print
def printer_ifs(dict, assunt, title):
    if not dict['type'] == 'Quick Task':
        if not dict[assunt] == '':
            if assunt == 'content':
                adjust_content(dict[assunt])
            else:
                print(f' | ~ {title}: {dict[assunt]}')
                
            return
        
        print(f' | ~ {title} ...')
        return
    else:
        print(f' | ...')
        return

class Todo:
    def __init__(self):
        self.tasks = []
    
    # function to show quantity of tasks
    def __size__(self):
        return len(self.tasks)

    # function to create a quick task
    def quick_task(self):
        bas = manage_inputs('Quick Task')

        self.tasks.append(bas.copy())
        bas.clear()

        msg_result(f'{choice(TagMessages)} be quick.')
    
    # function to create a simple task
    def simple_task(self):
        bas = manage_inputs('Simple Task')
        
        self.tasks.append(bas.copy())
        bas.clear()
        
        msg_result(f'{choice(TagMessages)} Your task was created.')

    # function to create a bigger task
    def bigger_task(self):
        bas = manage_inputs('Bigger Task')
        
        self.tasks.append(bas.copy())
        bas.clear()
        
        msg_result(f'{choice(TagMessages)} Very detailed task.')
        
    # functio to remove a task
    def remove_task(self):
        answer_identifier = you_want(f'you want use ID? (verify if your task has a ID)')
        
        if not answer_identifier == '':
            if answer_identifier == 'y':
                print()
                id_task = input('~ ID: ')
                print()
                index_task = next((i for i, d in enumerate(self.tasks) if d['ID'] == id_task), None)
                
                if index_task is not None:
                    answer_remove = you_want(f'you want remove "{self.tasks[index_task]['task_name']}"?')
                
                    if answer_remove == 'y':
                        del self.tasks[index_task]
                        print()
                    else:
                        msg_result(f'{choice(TagMessages)} canceled.')
                else:
                    msg_result(Messages[6])
                    
            else:
                print()
                task_name_v = input('~ task_name: ')
                print()
                task_name_for = next((i for i, d in enumerate(self.tasks) if d['task_name'] == task_name_v), None)
                
                if task_name_for is not None:
                    answer_remove = you_want(f'you want remove "{self.tasks[task_name_for]['task_name']}"?')
                
                    if answer_remove == 'y':
                        del self.tasks[task_name_for]
                        print()
                    else:
                        msg_result(f'{choice(TagMessages)} canceled.')
                else:
                    msg_result(Messages[6])
        else:
            msg_result(f'{Messages[4]}')
                 
    # function to view all tasks created 
    def view_all(self):
        if not self.__size__() == 0:
            for id, task in enumerate(self.tasks):
                print()
                print(f' | !Type: {task['type']}')
                print(f' | ID: {id}') if task['ID'] == '' else print(f' | ID: {task['ID']}')
                printer_ifs(task, 'tag', 'Tag')                
                print(f' | ~ task_name: {task['task_name']}')
                printer_ifs(task, 'content', 'content')
                print(f' | ~ is_favourite?: {task['favourite']}')
                print()
            return
                
        msg_result(f'{(Messages[5])} ~ No has tasks to show.')        
        return

    # function to view minimalist infos of all tasks
    def minimalist_view(self):
        if not self.__size__() == 0:
            for task in self.tasks:
                print()
                print(f' | !Type: {task['type']}', end=' ')
                print(f' | ID: ...', end=' ') if task['ID'] == '' else print(f' | ID: {task['ID']}', end=' ')          
                print(f' | ~ task_name: {task['task_name']}')
                print()
            return
                
        msg_result(f'{(Messages[5])} ~ No has tasks to show.')        
        return

    # function to edit a specific task
    def edit_task(self):
        answer_identifier = you_want(f'you want use ID? (verify if your task has a ID)')
        
        if not answer_identifier == '':
            if answer_identifier == 'y':
                print()
                id_task = input('~ ID: ')
                print()
                index_task = next((i for i, d in enumerate(self.tasks) if d['ID'] == id_task), None)
                
                if index_task is not None:
                    answer_edit = you_want_options('what do you want change?', 'TaskName', 'Contents')
                    
                    if not answer_edit == '':
                        if answer_edit == 't':
                            print()
                            self.tasks[index_task]['task_name'] = input('~ task_name: ')
                            print()
                        else:
                            print()
                            self.tasks[index_task]['content'] = input('~  content: ')
                            print()
                    else:
                        msg_result(Messages[4])
                else:
                    msg_result(f'{Messages[6]} ~ None value')
                
            else:
                print()
                task_name_d = input('~ task_name: ')
                print()
                task_name_for = next((i for i, d in enumerate(self.tasks) if d['task_name'] == task_name_d), None)
                
                if task_name_for is not None:
                    answer_edit = you_want_options('what do you want change?', 'TaskName', 'Contents')
                    
                    if not answer_edit == '':
                        if answer_edit == 't':
                            print()
                            self.tasks[task_name_for]['task_name'] = input('~ task_name: ')
                            print()
                        else:
                            print()
                            self.tasks[task_name_for]['content'] = input('~  content: ')
                            print()
                    else:
                        msg_result(Messages[4])
                else:
                    msg_result(f'{Messages[6]}')
                
        else:
            msg_result(f'{Messages[4]}')
            
    # function to view a specific task
    def view_unique(self):
        answer_identifier = you_want(f'you want use ID? (verify if your task has a ID)')
        
        if not answer_identifier == '':
            if answer_identifier == 'y':
                print()
                id_task = input('~ ID: ')
                print()
                index_task = next((i for i, d in enumerate(self.tasks) if d['ID'] == id_task), None)
                
                if index_task is not None:
                    print()
                    print(f' | !Type: {self.tasks[index_task]['type']}')
                    print(f' | ID: ...') if self.tasks[index_task]['ID'] == '' else print(f' | ID: {self.tasks[index_task]['ID']}')
                    printer_ifs(self.tasks[index_task], 'tag', 'Tag')                
                    print(f' | ~ task_name: {self.tasks[index_task]['task_name']}')
                    printer_ifs(self.tasks[index_task], 'content', 'content')
                    print(f' | ~ is_favourite?: {self.tasks[index_task]['favourite']}')
                    print()
                else:
                    msg_result(f'{Messages[6]} ~ None Value')
                
            else:
                print()
                task_name_d = input('~ task_name: ')
                print()
                task_name_for = next((i for i, d in enumerate(self.tasks) if d['task_name'] == task_name_d), None)
                
                if task_name_for is not None:
                    print()
                    print(f' | !Type: {self.tasks[task_name_for]['type']}')
                    print(f' | ID: {id}') if self.tasks[task_name_for]['ID'] == '' else print(f' | ID: {self.tasks[task_name_for]['ID']}')
                    printer_ifs(self.tasks[task_name_for], 'tag', 'Tag')                
                    print(f' | ~ task_name: {self.tasks[task_name_for]['task_name']}')
                    printer_ifs(self.tasks[task_name_for], 'content', 'content')
                    print(f' | ~ is_favourite?: {self.tasks[task_name_for]['favourite']}')
                    print()
                else:
                    msg_result(f'{Messages[6]} ~ None Value')
                
        else:
            msg_result(f'{Messages[4]}')
task=[]
while True:
    print('Insert the number corresponding to the action you want to perform:\n\
1. insert a new task;\n\
2. remove a task;\n\
3. show all the tasks;\n\
4. close the program.\n\
Your choice: ')
    num=int(input())
    if num==1:
        print('insert a new task:')
        insert=input()
        task.append(insert)
    elif num==2:
        if len(task)>0:
            print('what do you want to delete:')
            delete=str(input())
            for someline in task:
                if someline==delete:
                   task.remove(someline)
                   print(delete,'is removed')
                else :
                   print('can not find task')
        else:
            print('error')
    elif num==3:
        print('show all the tasks:')
        if len(task)>0:
            print(task)
        else:
            print('task is empty')
    elif num==4:
        print('close the program.')
        break
    else:
        print('it is wrong.')

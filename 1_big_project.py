todo_list=[]
def add_task():
    text_1=input("Enter new task:").strip()
    if text_1 == "":
        print(f"Programing can not be empty!")
        return
    for items in todo_list:
        if items["task"]==text_1:
             print("This task was!")
             return
    print(f"this {text_1} add!")
    new_task = {
        "task": text_1,
        "done": False
    }
    todo_list.append(new_task)
def show_tasks():
    if not todo_list:
        print("Your list is empty🎉🎉🎉")
        return
    completed=0
    in_progress=0
    print("--------------------")
    for number,item in enumerate(todo_list,1):
        icon_status=""
        if item["done"]==False:
            icon_status="❌❌"
            in_progress+=1
        else:
            icon_status = "✅✅"
            completed+=1
        print(f"{number}. [{icon_status}] {item['task']}")

    percent = round((completed / len(todo_list)) * 100,1)
    print(f"completed task {completed} 😏,not completed task {in_progress}😟 ")
    print(f"in total task in the list:{len(todo_list)},Done:{percent}%,Still:{in_progress}")
def change_status():
    show_tasks()
    try:
        completed_task=int(input("enter task how you did:"))
        todo_list[completed_task-1]["done"]=True
        print("status task is change")
    except ValueError:
        print("Error! You maybe wrote not number,try again")
    except IndexError:
        print("This current task not find")
def delete_task():
    show_tasks()
    try:
        delete_number = int(input("Enter number task how you want delete:"))
        if delete_number <= 0:
            raise ValueError
        todo_list.pop(delete_number-1)
        print(f"{delete_number} was delete")
    except ValueError:
        print("Error! maybe you wrote not number or integer")
    except IndexError:
        print("Not find this task")
while "YES":
  print("""Choose operation:
       1)add;
       2)show;
       3)change status 
       4)delete task
       5)exit""")
  choose=input("Enter operation:").strip().lower()
  if choose=="1" or choose=="add":
       add_task()
  elif choose=="2" or choose=="show":
       show_tasks()
  elif choose=="3" or choose=="change status":
     change_status()
  elif choose=="4" or choose=="delete task":
      delete_task()
  elif choose=="5" or choose=="exit":
      break
  else:
     print("You enter not correct operation,try again:")

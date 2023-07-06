def view_task():
    f=open("task.txt","r+")
    data=f.read()
    print(f"Your tasks are: {data}")
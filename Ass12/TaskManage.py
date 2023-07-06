def tasks():
    task=input("Enter tasks to be done:")
    f=open("task.txt","+a")
    f.write(task+"\n")
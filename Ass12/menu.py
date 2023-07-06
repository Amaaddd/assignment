def display():
    print("Team Management:")
    print("1) Register yourself")
    print("2) View your team")
    print("3) View your team member's position")
    print("4) Assign task to your team")
    print("5) View task")
    print("6) Exit")

def main():
    display()
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            import UserRegister
            UserRegister.register()
            # break
        elif choice == 2:
            import ViewTeam
            ViewTeam.view_team()
        elif choice == 3:
            import ViewPosition
            ViewPosition.view_pos()
        elif choice == 4:
            import TaskManage
            TaskManage.tasks()
        elif choice == 5:
            import ViewTask
            ViewTask.view_task()
        elif choice==6:
            break
        else:
            print("Invalid choice!")
            break
main()
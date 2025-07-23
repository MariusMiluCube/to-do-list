from random import choice


def show_me():
    print('\nTo do list app')
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")


def load_task():
    try:
        with open('tasks.txt', 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return []


def save_task(tasks):
    with open('tasks.txt', 'w') as f:
        for task in tasks:
            f.write(task + "\n")


def view_task():
    tasks = load_task()
    if not tasks:
        print("No task yet")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f'{i}. {task}')


def add_task():
    task = input('Enter a new task: ')
    tasks = load_task()
    tasks.append(f'[ ] {task}')
    save_task(tasks)
    print('Task added')


def mark_done():
    tasks = load_task()
    view_task()
    try:
        num = int(input('Enter task number to mark as done'))
        if 1 <= num <= len(tasks):
            if '[x]' in tasks[num-1]:
                print('Task already marked as done')
            else:
                task_text = tasks[num-1].replace('[ ]', '[x]')
                tasks[num-1] = task_text
                save_task(tasks)
                print('Task marked as done')
        else:
            print('Invalid number')
    except ValueError:
        print('Please eneter a number.')


def delete_task():
    pass


def main():
    while True:
        show_me()
        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            view_task()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            break
        else:
            print('You have input an invalid option, try again!')


if __name__ == '__main__':
    main()

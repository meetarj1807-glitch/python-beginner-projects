
N = int(input("Enter the No. of tasks to do in this week : "))

Tasklist = {}
for i in range(N):
    task = input("Enter the task to do: ")
    status = input("Current status : ")
    Tasklist[task] = status

print("------WEEKLY TO-DO LIST------")
print("-----------------------------")

for task,status in Tasklist.items():
    print(f" {task} : {status} ")

N2 = int(input("How many tasks are completed till now: "))
Complete = []

for i in range(N2):
    task2 = input("Enter the completed task : ")
    Complete.append(task2)

for task in Tasklist:
    if task in Complete:
         Tasklist[task] = "Done"
    else:
         Tasklist[task] = "Not Done"

print("\n-----The tasks summary-----")
for task, status in Tasklist.items():
    print(f"{task}: {status}")
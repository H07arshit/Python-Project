#project2 
#stage1
# students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
# for i in students:
#     avg=sum(students[i])/3
#     print(f" {i}  : {avg:.2f}")

#stage2
# students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
# for i in students:
#     avg=sum(students[i])/3
#     if avg>=85:
#         grade="A"
#     elif avg>=70:
#         grade="B"
#     elif avg>=50:
#         grade="C"
#     else:
#         grade="F"
#     print(f" {i}  : {avg:.2f} {grade}")


#stage3
# students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
# topper = ""
# max_avg = 0
# for i in students:
#     avg = sum(students[i]) / 3
#     if avg > max_avg:
#         max_avg = avg
#         topper = i
# print(f"Topper: {topper}")



#stage4
# students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}
# while True:
#     print("""1. Add student
#              2. View all
#              3. Show topper
#              4. Exit""")
#     choice = input("Enter choice: ")
#     if choice == "1":
#         name = input("Enter name: ")
#         m1 = int(input("Enter mark 1: "))
#         m2 = int(input("Enter mark 2: "))
#         m3 = int(input("Enter mark 3: "))
#         students[name] = [m1, m2, m3]

#     elif choice == "2":
#         for i in students:
#             avg = sum(students[i]) / 3
#             if avg >= 85:
#                 grade = "A"
#             elif avg >= 70:
#                 grade = "B"
#             elif avg >= 50:
#                 grade = "C"
#             else:
#                 grade = "F"
#             print(f"{i} {avg:.2f} {grade}")

#     elif choice == "3":
#         topper = ""
#         max_avg = 0
#         for i in students:
#             avg = sum(students[i]) / 3
#             if avg > max_avg:
#                 max_avg = avg
#                 topper = i
#         print(f"Topper: {topper}")

#     elif choice == "4":
#         print("Goodbye!")
#         break

#stage5 
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

while True:
    print("""
    1. Add student
    2. View all
    3. Show topper
    4. Exit""")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        if name in students:
            print("Student already exists.")
            continue

        marks = []
        for j in range(1, 4):
            while True:
                mark = int(input(f"Enter mark {j}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark, try again.")

        students[name] = marks

    elif choice == "2":
        for i in students:
            avg = sum(students[i]) / 3
            if avg >= 85:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 50:
                grade = "C"
            else:
                grade = "F"
            print(f"{i} {avg:.2f} {grade}")

    elif choice == "3":
        topper = ""
        max_avg = 0
        for i in students:
            avg = sum(students[i]) / 3
            if avg > max_avg:
                max_avg = avg
                topper = i
        print(f"Topper: {topper}")

    elif choice == "4":
        print("Goodbye!")
        break

students = [[1, 'Zaki', 5000], 12, [2, 'Arsh', 5000]]
def ls(students):
    for s in students:
        if isinstance(s, list):
            print(" In List :")
            for i in s:
                print(i)
        else:
            print('Not in list',s)
ls(students)


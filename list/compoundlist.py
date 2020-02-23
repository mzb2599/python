students = [[1, 'Zaki', 5000],12, [2, 'Arsh', 5000]]
for s in students:
    if isinstance(s, list):
        print(" Is List :")
        for i in s:
            print(s[0])
    else:
        print(s)
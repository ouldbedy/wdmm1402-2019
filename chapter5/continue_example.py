'''
اكتب برنامج لاضافة 3 على جميع عناصر قائمة ما عدا القيمة 98 و 100
'''

l1 = [3, 6, 8, 90, 12, 43, 20, 100, 65, 23, 98, 12, 1, 89, 65]
print('before:', l1)
for i in range(len(l1)):
    if l1[i] is 100 or l1[i] is 98:
        continue
    l1[i] += 3
print('after:', l1)

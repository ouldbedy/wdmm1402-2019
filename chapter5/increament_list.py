'''
اكتب برنامج لاضافة 3 لكل عناصر قائمة
'''

l1 = [3, 6, 8, 90, 12, 43, 20, 100, 65, 23, 98, 12, 1, 89, 65]
print('before:', l1)
for i in range(len(l1)):
    l1[i] += 3

print('after:', l1)

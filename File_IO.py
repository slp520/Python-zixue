# f=open('C:\\Users\\Administrator\\Desktop\\工作总结.txt','r')
# lines=f.readlines()
# print(lines)
#
# for line in lines:
#     print(line.split('、'[0]))

import csv
csv_file=csv.reader(open('C:\\Users\\Administrator\\Desktop\\slp.csv','r'))
print(csv_file)

for stu in csv_file:
    print(stu)
#文字对比脚本
import xlrd
#获取表格位置
data = xlrd.open_workbook("C:\\Users\\Administrator\\Desktop\\2.xlsx")
#定义表格内容
table = data.sheet_by_index(0)
nrows = table.nrows

for i in range(0,nrows):
    a = table.cell_value(i,1)
    a.strip()     #去除前后空格
    ifexit=False
    for j in range (0,nrows):
        if a == (table.cell_value(j,0)).strip():
            ifexit = True
            break
    if ifexit==False:
        print(a)




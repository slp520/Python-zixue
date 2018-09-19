


f=open("C:\\Users\\33940\\Desktop\\11",'w+')
f.write("123444")
f.tell()
f.seek(-(2),2)
print(f.read())
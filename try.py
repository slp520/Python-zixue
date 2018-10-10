# try:
#     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
#     print driver.find_element_by_link_text('CSDN').get_attribute('href')
# finally:
#     driver.close()
#
# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'kw')))
# '''判断某个元素是否被加到了dom树里，并不代表该元素一定可见，如果定位到就返回WebElement'''
# for i in(1,101):
# i=0
# sum=0
# while i<101:
#     sum+=i
#     i+=1
#
# print(sum)

#print(sum(range(1,101)))
# import pymysql.cursors
#
# import pymysql.cursors
#
# # 连接数据库
# connect = pymysql.Connect(
#     host='10.0.6.55',
#     port=3306,
#     user='admin',
#     passwd='Admin_12345',
#     db='python',
#     charset='utf8'
# )
#
# # 获取游标
# cursor = connect.cursor()
#
# # 插入数据
# sql = "INSERT INTO t1 (id, code) VALUES ( '%s', '%s' )"
# data = (4, '13512345678')
# cursor.execute(sql %data)
# connect.commit()
# print('成功插入', cursor.rowcount, '条数据')
#
# # 关闭连接
# cursor.close()
# connect.close()


# def activationcode2sql():
#     #打开数据库连接
#     db=pymysql.connect(host='10.0.6.55', port='3306', user='admin', passwd='Admin_12345', db='python',charset='utf8')
#     #使用cursor()方法创建一个cursor对象，来管理查询
#     cur=db.cursor()
#     #使用execute()方法执行SQL，如果存在则删除
#     cur.execute("drop table if exists t1")
#     #使用预处理创建表
#     cur.execute(" create table t1 (id int auto_increment primary key,code varchar(10))")
#     cur.execute("INSERT INTO t1 SET id=3")
#     # f1=open('text.txt')
#     # for line in f.readlines():
#     #     cur.execute("insert into t1(code)  values('%s')",line.strip())
#     # f1.close()
#     cur.close()

def test():
    print("成功了！")

if __name__ == '__main__':
    test()
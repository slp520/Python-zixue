# -*- coding: utf-8 -*-


"""
1.使用用户的输入来进行搜索的方法，不需要参数
"""
def count_words_byInput():
    # 输入文件位置
    print ("输入文件的绝对路径：")
    while True:
        try:
            source = input(">>")
            # 打开文件
            temp = open(source)
            # 读取内容
            myStr = temp.read()
            # 用break跳出循环
            break
        except Exception:
            # 如果输入有误，则重新输入
            print ("输入有误，请重新输入：")

    # 输入搜索关键字
    print ("请输入你想要查找的单词：")
    while True:
        try:
            key_word = input(">>")
            break
        except Exception:
            print ("输入有误，请重新输入：")

    # 用count()函数来统计单词出现的次数，为了避免大小写的问题，把文本和关键词都用upper()转换为大写。
    num = myStr.upper().count(key_word.upper())
    print ("\n文本内容为:\n>>%s\n\n搜索结果：\n>>有%d个【%s】" % (myStr, num, key_word))
    temp.close()

if __name__ == '__main__':
    count_words_byInput()

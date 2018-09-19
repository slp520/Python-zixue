"""
1. 用户输入一串文字 ，保存到user_input中
2.检查文字是否有敏感词，以及敏感词的具体位置。
        2.1 文件迭代器读取敏感词
        2.2 使用 str.find() 找到敏感词的位置
        2.3  直接使用relpace方式替换掉敏感词！
3.一句话中可能含有多个敏感字，这个时候就要重复2的步骤。
4.使用 ** 替换掉敏感词对应的个数。
"""

user_input=input('Leave your comments:  ')
for filter_word in open('filtered_words.txt'):
    fw=filter_word.rstrip()#去掉空字符
    if fw in user_input:
        fw_len=len(fw)
        user_input=user_input.replace(fw,'*'*fw_len)  #将user_input在原处进行修改，进行下一次循环查找。

else:
    print(user_input)
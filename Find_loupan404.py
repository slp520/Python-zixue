from selenium import webdriver
from time import sleep

#启动浏览器
driver=webdriver.Firefox()
loupan=["beijing","shanghai","chongqing","suzhou","hangzhou","nanjing",
        "guangzhou","shenzhen","yangzhou","qingdao","jiaxing","ningbo",
        "jinan","wuxi","fuzhou","langfang","xiamen","linyi","wuhu",
        "lianyungang","huzhou","wenzhou","chengmai","taiyuan","xian",
        "tianjin","wuhan","kunming","foshan","zhangzhou","luoyang",
        "guiyang","huangshi","haikou","taizhou","xiangyang","zhengzhou",
        "hengyang","yichang","changsha","chengdu","huhehaote","dingan",
        "hefei","qingyuan","zhangjiakou","wenchang","jingzhou","huizhou",
        "dongguan","luzhou","ezhou","shaoxing","chuzhou","xinyang","quanzhou",
        "nantong","weifang","baoding","baishan","jiangmen","zhuhai","changzhou",
        "zhenjiang","zhaoqing","xianyang","liaocheng","qinhuangdao","changzhi",
        "huangshan","sanya","lijiang","hainan","yunnan","haiwai","zunyi","zhongshan",
        "jingmen","tangshan","wanning","liuan","changde","zhangjiajie","maanshan","heyuan"]

for id in loupan:
    driver.get("http://www.fangdd.com/%s"%id)
    driver.maximize_window()
    try:
        txt = driver.find_element_by_id("btn-login").text
    except BaseException:
        print(id)
driver.quit()
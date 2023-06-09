from selenium import webdriver
from time import sleep
import json
import re
id = 912233
# ChromeDriver选项设置
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 隐藏Chrome浏览器窗口

# 启动ChromeDriver并连接到Chrome浏览器
driver = webdriver.Chrome('D:/Download/chromedriver', options=options)

# 访问网页
driver.get(f"https://www.tziakcha.xyz/record/?id={id}")
sleep(1)
# 从Javascript环境中获取变量
stat_variable = driver.execute_script("return stat;")
next = driver.execute_script("return next_id;")

# 将变量保存到文件中
stat_dict = []
for item in stat_variable:
    item.pop('frm', None)
    item.pop('hd', None)
    item.pop('pl', None)
    print(item)
    stat_dict.append(item)


# 将字符串保存到文件中
with open("output.txt", "w") as file:
    for item in stat_dict:
        file.write(str(item))
        file.write("\n")

# 完成操作后关闭浏览器
driver.quit()

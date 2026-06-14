print("nihao,Python","yuanjie","jinnian","25","sui");

age=25
print(age) ;

#int类型
num1=10
num2=-5

#float 浮点数，小数
height = 1.75
weight = 9.9

#str,字符串，文本
name = "袁杰"
hobby = "写代码"

#bool 布尔值 首字母必须大写，不能加引号
is_student = True
is_finish = False

#查看数据类型的的工具：type()

age = 25
name = "yuanjie"
print (type(age))
print(type(name))

#  符号	作用	例子	结果
#  +	加法	3 + 2	5  #
#  -	减法	3 - 2	1  #
#  * 	乘法	3 * 2	6  #
#  /	除法（结果永远是小数）	7 / 2	3.5  #
#  //	整除（只保留整数部分）	7 // 2	3  #
#  %	取余数	7 % 2	1#
#  **	乘方（几次方）	3 ** 2	9  #


name = "袁杰"       # 字符串
age = 25            # 整数
height = 1.75       # 浮点数
is_learning = True  # 布尔值，这一行之前漏掉了，必须加上

# 2. 打印个人信息
print("===== 个人信息 =====")
print("姓名：", name)
print("年龄：", age, "岁")
print("身高：", height, "米")
print("是否在学习：", is_learning)


# # 4. 算术运算练习
# #核心知识点：f-string 格式化输出
# #先讲你看到的 f"..." 是什么：
# #这是 Python 里最常用的「格式化字符串」，用法就是在字符串的引号前面加一个小写的 f，然后在字符串里面用 {变量名} 把变量包起来。#
# #程序运行的时候，会自动把 {变量名} 替换成变量里的真实值，写起来非常直观，不用再用逗号拆成好几段。#

# name = "袁杰"
# print(f"我的名字是{name}")
# # 运行后输出：我的名字是袁杰



print("\n===== 算术练习 =====")
num1 = 100
num2 = 6
print(f"{num1} + {num2} =", num1 + num2)
print(f"{num1} 除以 {num2}，商是：", num1 // num2, "余数是：", num1 % num2)
print(f"{num1} 的 2 次方 =", num1 ** 2)

print(f"{num1} + {num2} = {num1 + num2}")
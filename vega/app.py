#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/6 14:08
# @Author : zhaocunwei
# @Version：V 0.1
# @File : app.py
# @desc : 控制台程序

from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
import os
import sys

__user_service = UserService()

while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t=========================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t=========================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号：")
    if opt == "1":
        username = input("\n\t用户名:")
        password = getpass("\n\t密码：")
        result = __user_service.login(username, password)
        # 登录成功
        if result == True:
            # 查询角色
            role = __user_service.search_user_role(username)
            os.system("cls")
            while True:
                if role == "新闻编辑":
                    print("test")
                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.用户管理")
                    print(Fore.LIGHTRED_EX, "\n\tabck.退出登录")
                    print(Fore.LIGHTRED_Ex, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号:")
        else:
            print("\n\t登录失败")
    elif opt == "2":
        sys.exit(0)

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

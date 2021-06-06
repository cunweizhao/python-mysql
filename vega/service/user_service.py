#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time : 2021/6/6 13:57
# @Author : zhaocunwei
# @Version：V 0.1
# @File : user_service.py
# @desc :

from db.user_dao import UserDao


class UserService:
    # 创建私有对象
    __user_dao = UserDao()

    # 创建登录函数
    def login(self, username, password):
        result = self.__user_dao.login(username, password)
        return result

    # 查询用户角色
    def search_user_role(self, username):
        role = self.__user_dao.search_user_role(username)
        return role

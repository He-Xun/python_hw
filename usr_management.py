# -*- coding:utf-8 -*-
import re

def usr_management_system():
    main_table = {
        'david': {'age': 47, 'tel': '13xxxxxxxxx', 'gender': 'm'},
        'caroline': {'age': 23, 'tel': '13xxxxxxxxx', 'gender': 'f'},
        'hexun': {'age': 24, 'tel': '13xxxxxxxxx', 'gender': 'm'}
    }

    def delete_handler():
        flag = True
        while flag:
            c = input('please type usrname you wanna delete \n')
            if c in main_table.keys():
                del main_table[c]
                print('usr ' + c + " already deleted")
                break
            else:
                print('usr ' + c + ' not in main_table')

    def update_handler():
        flag = True
        while flag:
            c = input('please add user within this format  usrname:age:tel:gender \n')
            if re.match("\S+\:1?\d{,2}\:\d{11,}\:[MFmf]", c):
                c = c.split(":")
                main_table.update({c[0]: {'age': c[1], 'tel': c[2], 'gender': c[3]}})
                print('usr ' + str(c[0]) + ' added')
                break
            else:
                print('格式错误')

    def find_handler():
        flag = True
        while flag:
            usrname = input("please type usrname you wanna find ")
            if usrname in main_table.keys():
                print('----------------------------')
                print("name:{}".format(usrname))
                print(re.subn("[{}']*", "", str(main_table.get(usrname)))[0])
                print('----------------------------')
                flag = False
            else:
                print('usrname ' + usrname + ' is not in main_table')

    def list_handler():
        print("\nmain_table infomation")
        print('----------------------------')
        for x in main_table:
            print("name:{}".format(x))
            print(re.subn("[{}']*", "", str(main_table[x]))[0])
            print('----------------------------')

    def error_handler(s):
        print("command " + s + " is not exist")

    order_opt = {
        'delete': delete_handler,
        'update': update_handler,
        'find': find_handler,
        'list': list_handler,
        'exit': exit
    }

    def sys_reg():
        flag = True
        while flag:
            command_order = input("please insert command >>> ")
            if command_order.isalpha():
                if command_order in order_opt.keys():
                    for x in order_opt.keys():
                        if command_order == x:
                            order_opt[x]()
                else:
                    error_handler(str(command_order))
            else:
                error_handler(str(command_order))

    return sys_reg


reg = usr_management_system()
reg()

# -*- coding:utf-8 -*-
import re
import getpass


class usr_management_system():
    def __init__(self):
        self.main_table = {
            'david': {'password': 'abc2323232', 'age': 47, 'tel': '13428583882', 'gender': 'm'},
            'caroline': {'password': 'gegog2grgr23232', 'age': 23, 'tel': '18938384994', 'gender': 'f'},
            'hexun': {'password': 'abc2323232', 'age': 24, 'tel': '13100058284', 'gender': 'm'}
        }

        self.order_opt = {
            'delete': self.delete_handler,
            'update': self.update_handler,
            'find': self.find_handler,
            'list': self.list_handler,
            'exit': exit
        }

        self.admin_password = "123456"
        self.sys_reg()

    def validate_admin_pwd(self, psw):
        return psw == self.admin_password

    def delete_handler(self):
        flag = True
        while flag:
            c = input('please type usrname you wanna delete \n')

            if c in self.main_table.keys():
                del self.main_table[c]
                print('usr ' + c + " already deleted")
                break
            else:
                print('usr ' + c + ' not in self.main_table')

    def update_handler(self):
        flag = True
        # s = getpass.getpass('please typein admin password')
        s = input('please typein admin password ')

        if self.validate_admin_pwd(s):
            while flag:
                c = input('please add user within this format  usrname:password(length >= 6):age:tel:gender \n')
                if re.match("\S+\:\S{6,}\:1?\d{,2}\:\d{11,}\:[MFmf]", c):
                    c = c.split(":")
                    self.main_table.update({c[0]: {'password': c[1], 'age': int(c[2]), 'tel': c[3], 'gender': c[4]}})
                    print('usr ' + str(c[0]) + ' added')
                    break
                else:
                    print('format error')
        else:
            # raise ValueError('admin password incorrect')
            print('admin password incorrect')

    def find_handler(self):
        flag = True
        while flag:
            usrname = input("please type usrname you wanna find ")
            if usrname in self.main_table.keys():
                print('----------------------------')
                print("name:{}".format(usrname))
                print(re.subn("[{}']*", "", str(self.main_table.get(usrname)))[0])
                print('----------------------------')
                flag = False
            else:
                print('usrname ' + usrname + ' is not in self.main_table')

    def list_handler(self):
        s = input('please typein sort condition (tel/age/name) ')
        a = re.findall('tel|age|name', s.strip())
        tmp_list = []
        if bool(a):
            for x in self.main_table.items():
                tmp_list.append(x)

            if a[0] != 'name':
                tmp_list = sorted(tmp_list, key=lambda x: x[1][a[0]])
            else:
                tmp_list = sorted(tmp_list, key=lambda x: x[0])

        else:
            print('sort condition error')
            return

        print("\nself.main_table infomation")
        print('----------------------------')
        for x in tmp_list:
            cur_display = x
            cur_display[1]['password'] = len(cur_display[1]['password']) * '*'
            print("name:{}".format(cur_display[0]))
            print(re.subn("[{}']*", "", str(cur_display[1]))[0])
            print('----------------------------')

    def error_handler(self, s):
        print("command " + s + " is not exist")

    def sys_reg(self):
        flag = True
        while flag:
            command_order = input("please insert command >>> ")
            if command_order.isalpha():
                if command_order in self.order_opt.keys():
                    for x in self.order_opt.keys():
                        if command_order == x:
                            self.order_opt[x]()
                else:
                    self.error_handler(str(command_order))
            else:
                self.error_handler(str(command_order))


usrmg = usr_management_system()

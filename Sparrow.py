#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# author: TheEnterprisePC
#Code Name:Sparrow.
#***It is a small project. \(*￣▽￣*)/***



#读取模块
import socket
import webbrowser
import platform
import tkinter as tk
import tkinter.messagebox
import winreg
import uuid
import os
import sys
import shutil
import time
import datetime
import threading


#读取系统信息&GUI
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]

addr_num = hex(uuid.getnode())[2:]
mac = "-".join(addr_num[i: i+2] for i in range(0, len(addr_num), 2))

key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion")
BuildLab = winreg.QueryValueEx(key,"BuildLabEx")

CPUinfo = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0")
CPUID = winreg.QueryValueEx(CPUinfo,"ProcessorNameString")

Frequency = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"HARDWARE\DESCRIPTION\System\CentralProcessor\0"),"~MHz")

EditionID = platform.release()
if EditionID == "Vista" and "XP":
   EditionID = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion"),"EditionID_bak")
else:
   EditionID = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion"),"EditionID")

window = tk.Tk()
window.title("麻雀工具箱")
window.geometry('500x400')
var_1 = tk.StringVar()
var_2 = tk.StringVar()
var_3 = tk.StringVar()
var_4 = tk.StringVar()
var_5 = tk.StringVar()
var_6 = tk.StringVar()
var_7 = tk.StringVar()
var_8 = tk.StringVar()
var_9 = tk.StringVar()
var_10 = tk.StringVar()
var_11 = tk.StringVar()
var_12 = tk.StringVar()
tk.Label(window, text='系统信息',font=("Song Ti",20)).pack()
frame = tk.Frame(window)
frame.pack()
frame_l = tk.Frame(frame)
frame_r = tk.Frame(frame)
frame_l.pack(side='left')
frame_r.pack(side='right')
tk.Label(frame_l, text='OS位数、类型：',).pack()
tk.Label(frame_l, text='机器架构：',).pack()
tk.Label(frame_l, text='OS信息：',).pack()
tk.Label(frame_l, text='处理器：',).pack()
tk.Label(frame_l, text='处理器频率(MHz)、核心数：',).pack()
tk.Label(frame_l, text='OS版本：',).pack()
tk.Label(frame_l, text='OS名称：',).pack()
tk.Label(frame_l, text='Build号：',).pack()
tk.Label(frame_l, text='完整Build号：',).pack()
tk.Label(frame_l, text='IP地址：',).pack()
tk.Label(frame_l, text='MAC地址：',).pack()
tk.Label(frame_l, text=' ',).pack()
tk.Label(frame_r, textvariable=var_1,).pack()
tk.Label(frame_r, textvariable=var_2,).pack()
tk.Label(frame_r, textvariable=var_3,).pack()
tk.Label(frame_r, textvariable=var_4,).pack()
tk.Label(frame_r, textvariable=var_12,).pack()
tk.Label(frame_r, textvariable=var_5,).pack()
tk.Label(frame_r, textvariable=var_6,).pack()
tk.Label(frame_r, textvariable=var_7,).pack()
tk.Label(frame_r, textvariable=var_8,).pack()
tk.Label(frame_r, textvariable=var_9,).pack()
tk.Label(frame_r, textvariable=var_10,).pack()
tk.Label(frame_r, textvariable=var_11,).pack()

on_hit = False
def scan():
    global on_hit
    if on_hit == False:
        on_hit = True
        var_1.set(platform.architecture())
        var_2.set(platform.machine())
        var_3.set(platform.platform())
        var_4.set(CPUID)
        var_12.set(Frequency)
        var_5.set(EditionID)
        var_6.set(platform.system())
        var_7.set(platform.version())
        var_8.set(BuildLab)
        var_9.set(ip)
        var_10.set(mac)
        var_11.set('')
    else:
        on_hit = False
        var_11.set('检测出来了!')
 
b = tk.Button(window, text='检测', width=10, height=1, command=scan)
b.pack()


#工具
def CleanCache():
   os.system("CleanCache.bat")
def ControlPanel():
   os.system("Control Panel")
def gpedit():
   os.system("gpedit.msc")
def msconfig():
   os.system("msconfig.exe")
def cmd():
   os.system("cmd")
def cmptrmgmt():
   os.system("compmgmt.msc")
def taskmgr():
   os.system("taskmgr.exe")
def services():
   os.system("services.msc")
def osk():
   os.system("osk.exe")
def dxdiag():
   os.system("dxdiag.exe")
def SysRestore():
   os.system("rstrui.exe")
def fdj():
   os.system("magnify.exe")
def ping():
   if os.system("ping -n 1 www.baidu.com") == 0:
      tkinter.messagebox.showinfo(title='结果', message='可访问互联网')
   else :
      tkinter.messagebox.showinfo(title='结果', message='不可访问互联网')
def RepairExeFiles():
   os.system("RepairExe.reg")
def UnlockReg():
   os.system("reg import UnlockReg.reg")
def shutdownwindow():
   win = tk.Tk()
   win.title('定时关机')
   win.geometry('240x180')
   Label3=tkinter.Label(text=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
   Label3.pack()
   def trickit():
      currentTime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
      Label3.config(text=currentTime)
      Label3.after(1000, trickit)
   Label3.after(1000, trickit)
   l1 = tkinter.Label(win, text="请输入小时")
   l1.pack()
   inputhour=tkinter.Entry(win,bd='0',width='10')
   inputhour.pack()
   l2 = tkinter.Label(win, text="请输入分钟")
   l2.pack()
   inputminute=tkinter.Entry(win,bd='0',width='10')
   inputminute.pack()
   def gettime():
      hour = int(inputhour.get())
      minute = int(inputminute.get())
      print(hour,minute)
      curtime = datetime.datetime.now()
      curtime_hour = curtime.hour
      curtime_minute = curtime.minute
      hours = ((hour + (minute / 60)) - (curtime_hour + curtime_minute / 60))
      minutes = hours * 60
      seconds = hours * 60 * 60
      tkinter.messagebox.showinfo('提示', "距离关机还有%d分钟" % minutes)
      os.system('shutdown -s -t %d' % seconds)
   tkinter.Button(win,text="确定关机",command=gettime).pack()
   def cancel():
      if os.system("shutdown -a") ==1116:
         tkinter.messagebox.showinfo('提示', "您当前没有设置关机任务")
      else:
         tkinter.messagebox.showinfo('提示', "取消成功")
   tkinter.Button(win,text="取消关机",command=cancel).pack()
   win.mainloop()
      
   
#对话框
counter = 0
def do_job():
    global counter
    l.config()
    counter += 1
def about():
    tkinter.messagebox.showinfo(title='关于', message='制作by TheEhterprisePC\n部分命令运行时可能会有命令提示符的窗口出现')

def link():
    webbrowser.open('github.com/TheEnterprisePC/SparrowToolBox',new=1,autoraise=True)

#工具栏
menubar = tk.Menu(window)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label='关于', command=about)
filemenu.add_command(label='Github项目链接', command=link)

toolmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=filemenu)
menubar.add_cascade(label='工具', menu=toolmenu)
toolmenu.add_command(label='清理垃圾', command=CleanCache)
toolmenu.add_command(label='修复.exe文件的关联', command=RepairExeFiles)
toolmenu.add_command(label='解禁注册表', command=UnlockReg)
toolmenu.add_command(label='定时关机', command=shutdownwindow)

WindowsToolMenu = tk.Menu(menubar, tearoff=0)
toolmenu.add_cascade(label='Windows自带工具(如果有的话)', menu=WindowsToolMenu)
WindowsToolMenu.add_command(label='控制面板', command=ControlPanel)
WindowsToolMenu.add_command(label='组策略', command=gpedit)
WindowsToolMenu.add_command(label='系统配置实用程序', command=msconfig)
WindowsToolMenu.add_command(label='命令提示符', command=cmd)
WindowsToolMenu.add_command(label='计算机管理', command=cmptrmgmt)
WindowsToolMenu.add_command(label='任务管理器', command=taskmgr)
WindowsToolMenu.add_command(label='Windows服务', command=services)
WindowsToolMenu.add_command(label='屏幕键盘', command=osk)
WindowsToolMenu.add_command(label='DirectX诊断工具', command=dxdiag)
WindowsToolMenu.add_command(label='系统还原', command=SysRestore)
WindowsToolMenu.add_command(label='放大镜', command=fdj)

NetworkTools = tk.Menu(menubar, tearoff=0)
toolmenu.add_cascade(label='网络工具', menu=NetworkTools)
NetworkTools.add_command(label='检测是否能访问互联网', command=ping)

window.config(menu=menubar)

window.mainloop()






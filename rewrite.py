# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 10:44:35 2018

@author: 123
"""
#去除剪切板中的回车键
import win32clipboard as wc
import win32con
import time

def getCopyText():
    wc.OpenClipboard()
    copy_text = wc.GetClipboardData(win32con.CF_TEXT)
    wc.CloseClipboard()
    return copy_text

def setText(aString):#写入剪切板  
    wc.OpenClipboard()  
    wc.EmptyClipboard()  
    wc.SetClipboardText(aString)  
    wc.CloseClipboard() 

## test
#import chardet
#print( chardet.detect(getCopyText()) )  # 找到包含中文内容的字符串编码
#print( getCopyText().decode('GB2312') ) # 转码
#print( getCopyText() ) #输出bytes与结果对比去除效果
    
#ss = getCopyText().decode()
#uu = ss.replace('\n','').replace('\r','')
#print(uu)
#
#setText(uu)

if __name__ == '__main__':

    while True:
        ss = getCopyText().decode('GB2312')
        uu = ss.replace('\n','').replace('\r','')
#        print(uu)
        setText(uu)
        time.sleep(5*1)#refresh clipboard every 5s
#        print('RUNNING\n')



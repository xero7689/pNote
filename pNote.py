#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PNote - Python Command-Line Note App

Still under develope...

author: xero
mail: volleyp7689@gmail.com
last edit: July 17 2014
"""

import datetime
import tempfile
import getpass
import os

_LINE_BREAK = "\n"
_DEFAULT_ENCODE = "utf-8"

_USER = getpass.getuser()
_USER_HOME_DIR = os.path.expanduser("~")
_DEFAULT_PNOTE_DIR = os.path.join(_USER_HOME_DIR, "pNote")

_NOW = datetime.datetime.now().ctime().split()

def init_dir():
    if not os.path.exists(_DEFAULT_PNOTE_DIR):
        os.makedir(_DEFAULT_PNOTE_DIR)

def output_note():
    pass
    
def main():
    pass

class PNote:
    
    def __init__(self, title = "", time = _NOW, tag = []):
        self.title = title #string
        self.time = time #list
        self.tag = tag #list? or dict ?
    
    def addTag(self):
        pass
    def takeNote(self):
        # message to user
        print("pNote - Start !")
        print("Hi " + _USER + "! Right now is " +  _NOW[3])
        
        #set title
        if len(self.title) == 0:
            print("What's the title of this note ?")
            while True:
                self.title = input("->")
                if len(self.title) == 0:
                    print("Need a title !")
                else:
                    break
        else:
            print("Title: " + self.title)
        
        #take note
        print("Write something down :")
        tf = tempfile.TemporaryFile()
        
        while True:
            text = input()
            if len(text) == 0:
                break
            else:
                text = text + _LINE_BREAK
                tf.write(text.encode(_DEFAULT_ENCODE))
        #self.content
        self.content = tf

if __name__ == "__main__":
    main()

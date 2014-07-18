#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
PNote - Python Command-Line Note App

author: xero
mail: volleyp7689@gmail.com
last edit: July 17 2014
"""

import datetime
import tempfile
import getpass
import os
import copy
import sys

_VERSION = "1.0"
_AUTHOR = "xero"

_LINE_BREAK = "\n"
_DEFAULT_ENCODE = "utf-8"
_DEFAULT_DECODE = "utf-8"
_FILENAME_EXT = ".pn"

_USER = getpass.getuser()
_USER_HOME_DIR = os.path.expanduser("~")
_DEFAULT_PNOTE_DIR = os.path.join(_USER_HOME_DIR, "pNote")

_NOW = datetime.datetime.now().ctime().split()

NOTE_LIST = []

'''Data structure'''
class newNote:
    
    def __init__(self, title = "", time = _NOW, tag = []):
        self.title = title #string
        self.time = time #list
        self.tags = tag #list? or dict ?
        self.takeNote()
    
    def addTag(self, *tags):
        for tag in tags:
            self.tags.append(tag)
        print("Add tag: ", end = "")
        for tag in self.tags:
            print(tag, end=",")
            
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

    
'''Command'''
def init_dir():
    if not os.path.exists(_DEFAULT_PNOTE_DIR):
        os.makedir(_DEFAULT_PNOTE_DIR)

def add():
    new = newNote()
    NOTE_LIST.append(new)

def output():
    PNote = NOTE_LIST.pop()
    
    # file name
    fn = os.path.join(_DEFAULT_PNOTE_DIR, PNote.title + _FILENAME_EXT)
    
    # check directory
    init_dir()
    
    # check file is existed, if exist than modify file name
    while os.path.isfile(fn):
        fn = os.path.join(fn, "-rp")
    
    # seek and decode Pnote
    # should use a copy of pnote.
    output_note = copy.copy(PNote)
    output_note.content.seek(0)
    output = output_note.content.read().decode(_DEFAULT_DECODE)
    
    # create file and output
    with open(fn, "a+") as f:
        # should format out-put
        f.write("Title: " + output_note.title + "\n")
        
        date = ""
        for i in output_note.time:
            date = date + i + "-"
        f.write("Date: " + date + "\n")
        
        f.write("Content: \n")
        f.write(output)

def listNote():
    for note in os.listdir(_DEFAULT_PNOTE_DIR):
        if note.endswith(_FILENAME_EXT):
            NOTE_LIST.append(note)
    print(NOTE_LIST)

def _quit():
    sys.exit("Bye!\n")
    
command = dict(a = add, 
                o = output,
                ll = listNote,
                q = _quit)

def commandLine():
    ''' prompting message '''
    print("\nWelcome to pNote-" + _VERSION)
    
    while True:
        print("\nCommand:")
        print("(a)Add (o)Output (ll)List (q)Quit")
        action = input("->")
        try:
            command[action]()
        except KeyError:
            print("command error, choose again!")
            
def main():
    commandLine()
    
if __name__ == "__main__":
    main()

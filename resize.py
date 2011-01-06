#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        resize.py
#created:        2011-01-05 21:35
import re
from sys import exit

from optparse import OptionParser

from os.path import abspath
from os.path import dirname as dirname
from os.path import join as pathjoin

try:
    import Image
except:
    print "Please install PIL module for python before using this script"
    exit(1)


def getPath(sufix=""):
    '''get absolute path of the current dir'''
    path = dirname(__file__)
    try:
        index=path.index("..")
        if index!=-1:
            path=path[:index]
    except:
        pass
    return pathjoin(abspath(path), sufix).replace('\\','/')


def getOptions():
    '''get and parse options '''
    usage = "usage: %prog [options] FILE1 [ FILE2 ...]"
    parser=OptionParser(usage=usage)

    parser.add_option("-r", "--resolution", dest="resolution", help="the destination resolution in 1024x768 format. You may use Non-digital chars to separate width and height, but do not use space as delimiter")
    parser.add_option("-p", "--percent", dest="percent", help="the destination resolution in 90 format, where 90 stands for 90% percent. Please do not add the '%' sign.")

    parser.add_option("-d", "--destination", dest="destination", help="the path to save the result. if omitted, the current folder will be used.")

    (options, args) = parser.parse_args()
    if not ( options.resolution or options.percent):
        print parser.parse_args( [ '--help' ] )
        exit(1)
    if not args:
        print "Please Specify Picture files to resize!"
        print parser.parse_args( [ '--help' ] )
        exit(1)
    if not (options.destination):
        options.destination=getPath()
    return{
        'files': args,
        'option': options,
    }

def resize(files, resolutionString="", percent=None, output="./"):
    '''resize all files with given opts'''

    size=[]

    if resolutionString:
        size=re.findall(r"\d+", resolutionString)
        size=[int(i) for i in size]
        if not size:
            print "Seems the resolution argument is not correct."
            exit(1)

    elif percent:
        percent=int(percent)
        if not percent:
            print "Seems the percent argument is not correct."
            exit(1)

    all=len(files)
    index=0

    for file in files:
        try:
            im=Image.open(file)
            try:
                filename=re.findall(r"[^/]+$", file)[0]
            except:
                print 'Error occured when try to get the real filename'
                continue
            outputfilename=pathjoin(abspath(output), "r_"+filename).replace('\\','/')

            if percent and not size:
                size=[int(i * percent / 100) for i in im.size ]

            result=im.resize(size, Image.ANTIALIAS)
            result.save(outputfilename)
            index+=1
            print "[%d of %d] %s has been resized." % (index, all, file)

        except:
            print "Error occured when resizing %s" % file


if __name__=="__main__":

    args=getOptions()
    files=args['files']
    option=args['option']
    resize(files, resolutionString=option.resolution,
            percent=option.percent,
            output=option.destination)



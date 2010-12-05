#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        format_html.py
#created:        2010-08-04
import re,sys

indent="\t"
f=open(sys.argv[1])
content=f.read()
f.close()
content=content.strip()

#combine < \n..> lines
x=re.search(r"(<[^<>]+)\s*\n\s*",content) 
while x: 
    content=content.replace(x.group(0),x.group(1)+" ")
    x=re.search(r"(<[^<>]+)\s*\n\s*",content)

content=re.sub(r"(?m)(?<!^)\s*(?=<)","\n", content)
content=re.sub(r"(?<=>)\s*(?=\S)","\n", content);
lines=content.splitlines()

level=0
for l in lines: 
    l = re.sub(r'''(?i)<((?:!|img|input|link|meta)[^>]+)\s*(?<!/)>''', r"<\1 />", l)
    if "/>" in l:
        print "%s%s"%(indent*level,l)
    elif l[:2]=='</' :  
        level -=1
        print "%s%s"%(indent*level,l)
    elif l[:1]=='<': 
        print "%s%s"%(indent*level,l)
        level +=1 
    else:
        print "%s%s"%(indent*level,l)

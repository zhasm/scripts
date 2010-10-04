#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#author:         rex
#blog:           http://iregex.org
#filename        threatexpert.py
#created:        2010-10-03 13:25

import re
import sys
import urllib2 
import commands 
import cgi

email_account="****@****"

def get_V(p, regex=None):
    """return cgi GET parameter; strip white spaces at both ends if any;
    if verify pattern provided, do match test; only return matched values.
    Note: it uses re.match to check , not re.search.
    """
    import cgi
    form = cgi.FieldStorage()
    value= form.getfirst(p)
 
    if not value:
        return None
    value=value.strip()
 
 
    if regex is not None:
        import re
        if re.match(regex+"$",value):
            return value
        else:
            return None
    else:
         return value

def online_open(url):
    fd=urllib2.urlopen(url)
    try:
        data=fd.read()
        fd.close()
        return data
    except:
        return None

def get_hash(html, fn):
    if not html: return 

    result = re.findall(r'(?s)id="__VIEWSTATE"\s+value="([^"]+)".*?id="__EVENTVALIDATION"\s+value="([^"]+)".*(NeatUpload_[A-F0-9]+-FileUpload)', html)

    if not result: return
    viewstate=result[0][0]
    valid=result[0][1]
    uploadid=result[0][2]
    data={
        "txtEmail":email_account,
        "chAgreeWithTerms":"on",
        "btnSubmit.x":"40",
        "btnSubmit.y":"15",
        "__EVENTVALIDATION":valid,
        uploadid:"@%s" % fn,
        "__EVENTTARGET":"",
        "__EVENTARGUMENT":"",
        "__VIEWSTATE":viewstate, 
    }
    return data

def make_cmd(h, url):
    args=" ".join(['''-F "%s=%s"''' % (key, h[key]) for key in h])
    cmd="curl -s %s %s" % (args, url)
    return cmd

def main():
    print "content-type: text/html\n"
    fn=get_V("file")
    if not fn:
        print "No file input!"
        exit()
    url="http://www.threatexpert.com/submit.aspx"
    html=online_open(url)
    data=get_hash(html, fn)
    cmd=make_cmd(data,url)
    out=commands.getoutput(cmd)
    if "accepted" in out:
        print "Submit ok"
    else:
        print "Submit Failed! please upload in traditional way"

if __name__=='__main__':
    main()


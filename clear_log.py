#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Author:xp
# date:20170522
# blog_url: http://blog.csdn.net/wuxingpu5/

import os, time, datetime

# logs directory
data_dir = '/home/dev/app/tomcat_test/logs'


def del_log():
    date = os.popen("date -d '(date +%Y%m%d) -7 days' +%Y-%m-%d").read().strip()
    t2 = time.strptime(date, '%Y-%m-%d')
    # t2 is the seven days ago
    t2 = datetime.datetime(*t2[:3])

    # get each file in the directory
    for filename in os.listdir(data_dir):
        filepath = os.path.join(data_dir, filename)
        # Judgment is a file
        if os.path.isfile(filepath):
            file_date = os.popen("stat %s | sed -n '7p' | awk '{print $2}'" % filepath).read().strip()
            # t1 is the last change time of the file
            t = time.strptime(file_date, '%Y-%m-%d')
            t1 = datetime.datetime(*t[:3])
            log_len = len(filename.split('-'))

            # Compare creation time earlier than seven days ago
            if t1 < t2 and log_len >= 3:
                time.sleep(2)
                os.system("true >%s" % filepath)
                os.system("rm -rf %s" % filepath)


del_log()


# change directory and then run again

# data_dir='/home/dev/app/tomcat_test2/logs'

# del_log()

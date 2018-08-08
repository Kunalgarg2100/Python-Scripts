
import os,shutil
import json
import sys
import subprocess
import datetime

from threading import Timer

array = []
with open('list.json') as json_data:
    d = json.load(json_data)

for i in d:
    for j in i:
        array.append(j)

length = len(array)
location =[]
filename =[]
for g in range(0,length,2):
    location.append(array[g])
for g in range(1,length,2):
    filename.append(array[g])
if sys.argv[1] == "backup":
    lengthl = len(location)
    for g in range(0,lengthl):
        i = location[g]
        if os.path.isfile(i):
            shutil.copyfile(i, filename[g])
            print("Backup have been made for file {}".format(filename[g]))

if sys.argv[1] == "restore":
    lengthl = len(filename)
    for g in range(0, lengthl):
        i = filename[g]
        if os.path.isfile(i):
            shutil.copyfile(i, location[g])
            print("{} file restored".format(i))


if sys.argv[1] == "push":
    subprocess.Popen(['echo', 'Please wait till the process is completed'])
    def star():
        for g in filename:
            subprocess.Popen(['git', 'add', g])
            print("{} file is pushed".format(g))
    def stat():
        subprocess.Popen(['echo', 'Checking status'])
        subprocess.Popen(['git', 'status'])
    def cmt():
        subprocess.Popen(['echo', 'Commiting the files'])
        subprocess.Popen(['git', 'commit', '-m','Files Uploaded on ' + str(datetime.datetime.now().date()) +' at '+ str(datetime.datetime.now().time().hour) + ':'\
    + str(datetime.datetime.now().time().minute) + ':' + str(datetime.datetime.now().time().second)])
    def tym():
        subprocess.Popen(['git', 'push', 'origin', 'master'])
    def helo():
        subprocess.Popen(['echo', 'Process Completed'])

    f = Timer(1,star)
    q = Timer(2,stat)
    w = Timer(3,cmt)
    p = Timer(4, tym)
    t = Timer(26, helo)
    f.start()
    q.start()
    w.start()
    p.start()
    t.start()

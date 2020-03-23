import os, sys
import shutil
from datetime import datetime

home_env = os.getenv("HOME")

EDITOR = "nvim -c 'set wrap linebreak'"



if len(home_env) == 0:
    print("error: no HOME environment variable")
    exit()

start_path = os.getcwd()

docs_path = home_env + "/.diary"
diary_path = docs_path + "/diaries"

def extract():
    os.chdir(docs_path)
    os.system(f"tar -xvf diary.tgz")
    os.chdir(start_path)

def compress():
    os.chdir(docs_path)
    os.system(f"tar -czvf diary.tgz diaries")
    shutil.rmtree(diary_path)
    os.chdir(start_path)

if not os.path.exists(docs_path):
    os.mkdir(docs_path)
if not os.path.exists(diary_path):
    os.mkdir(diary_path)
if not os.path.isdir(docs_path):
    print("error: docs path is a file (wtf?)")
    exit()
if not os.path.isfile(docs_path + "/diary.tgz"):
    print("no diary found")
else:
    extract()

# at this point the directory ~/Documents/diary exists

try:
    iso_date = str(datetime.date(datetime.now()).isoformat())
    if len(sys.argv) > 1:
        iso_date = sys.argv[1]
    os.system(EDITOR + " " + diary_path + "/" + iso_date + ".txt")

except Exception as e:
    print(e)
    compress()
else:
    compress()






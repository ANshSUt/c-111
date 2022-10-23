import os
import shutil
from_dir="C:\Users\hasmu\Downloads"
to_dir ="C:\Users\hasmu\Desktop\Project111"
list_of_files = os.listdir(from_dir)
print (list_of_files)
for i in list_of_files :
    name,extention=os.path.splitext(i)
    print (name)
    if
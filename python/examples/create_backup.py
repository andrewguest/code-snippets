import zipfile
import os
import time


month = time.strftime("%m")
day = time.strftime("%d")
year = time.strftime("%Y")
backup_date = month + "-" + day + "-" + year

# THE DIFFERENT FORMATS FOR THE DIFFERENT OS PATHS
# windows_source_dir = "C:\\Users\\Andrew\\Documents\\mydir"
# linux_source_dir = '/home/code/test'

os.chdir(os.path.dirname(linux_source_dir))
with zipfile.ZipFile(backup_date + '.zip', "w", zipfile.ZIP_DEFLATED) as zf:
    for root, _, filenames in os.walk(os.path.basename(linux_source_dir)):
        for name in filenames:
            name = os.path.join(root, name)
            name = os.path.normpath(name)
            zf.write(name, name)
            
            
            
            
 '''
 Example of how the script works.
 Directory structure:
 home
   '--> code
          '--> test
                 '--> folder1
                          '--> file1.txt
                          '--> pic1.jpg
                 '--> folder2
                          '--> taxes.doc
                          '--> receipt.pdf
                          

After running this script this is what you would end up with:

test.zip
    '--> test
           '--> folder1
                    '--> file1.txt
                    '--> pic1.jpg
           '--> folder2
                    '--> taxes.doc
                    '--> receipt.pdf 
 '''

from zipfile import *

fp = ZipFile('test.zip','w',ZIP_DEFLATED)
fp.write("log2.txt")
fp.write("mylog.txt")
fp.close()




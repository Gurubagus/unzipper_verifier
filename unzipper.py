import sys
import os
import time
import logging
import zipfile
import verify_filesize
path = sys.argv[1] if len(sys.argv) > 1 else '.'


def main():
	global fname
	cwd = os.getcwd()
	f = os.listdir(cwd)
    
	for file in f:
		if file.endswith('.zip'):
			fname = str(file)
			zip_ref = zipfile.ZipFile(cwd+'/'+fname,'r')
			verify_filesize.main(fname)
			zip_ref.extractall()
			zip_ref.close()
			


if __name__== "__main__":
    main()
        
        
    

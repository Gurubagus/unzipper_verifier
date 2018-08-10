import os
import sys
import verify_filesize
	
def main():
    global fname
    cwd = os.getcwd()
    f = os.listdir(cwd)
    
    for file in f:
        if file.endswith('.txt'):
            fname = str(file)
            #zip_ref = zipfile.ZipFile(cwd+'/'+fname,'r')
            verify_filesize.main(fname)

if __name__=="__main__":
    main()
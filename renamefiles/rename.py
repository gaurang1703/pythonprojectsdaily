# this is python code to rename multipl files in a directory/folder

import os

def main():

    for count,filename in enumerate(os.listdir("/home/bikram/Downloads/images/")):
        dst="File"+str(count)+".jpeg"
        src="/home/bikram/Downloads/images/"+filename
        dst="/home/bikram/Downloads/images/"+dst

        # rename function will rename all the files
        os.rename(src,dst)

if __name__ == "__main__":
    main()
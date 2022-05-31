from os import access
from tkinter import DOTBOX
from tracemalloc import Snapshot
from cv2 import VideoCapture
import dropbox
import time
import random
import cv2

startTime=time.time()


def take_Snapshot():
    number=random.randint(0,100)
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True    
    while(result):
        ret,frame=VideoCaptureObject.read()
        imageName="image"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        startTime=time.time()
        result=False
    return imageName
    print("Picture Taken")
    VideoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadImage(imageName):
    access_token="sl.BHrB42Vj5EkYn9UDB73J8va7YOMQla1NvWItGJQP7jrOGDyqm3cLtbGW26noWOqztiOEuIxpedJ1MG6NkF4m1t_4mPrqgMdXgT-sMRdf6RR0lv1hyyfDsG6USp7qiEtTOXGdbcWqFzQ"
    file=imageName
    filefrom=file
    fileto="/imageFolder/"+(imageName)
    dbx=dropbox.Dropbox(access_token)
    with open(filefrom, 'rb') as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("file Uploaded")
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=take_Snapshot()
            uploadImage(name)
main()
import cv2
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject= cv2.videoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite("NewPicture1.jpg", frame)
        result = false
    return img_name
    print("snapshot taken")

    videoCaptureObject.release()
    cv2.destroyAllWindows()

take_snapshot()

def upload_file(img_name):
    access_token = "riFu6YbhcAAAAAAAAAAIJ_A5fl_EVHtEp33bdEjXapu5jLJLT38D6g_Hz25genB"
    file = img_counter
    file_from = file
    file_to = "newFolder1/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to , mode = dropbox.files.WriteMode.overwrite)
        print("File uploaded")

def main():
    while(True):
        if((time.time() - start_time)>=300):
            main = take_snapshot()
            upload_file(name)

main()
    

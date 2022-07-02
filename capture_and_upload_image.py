import cv2
import dropbox
import time
import random

start_time=time.time()
def take_snapshot():
    number=random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token="sl.BKhWaowNyD4ydsR7Wm06KIlYrTW6oO5MqUkpysM6ElpnRKjUfoYmscdXQLeZy1hovXjg_2wJzZCCkaurgQJyN6L8Kov624F2G7ShoRVZcM9eczbCNLF2zmcDRbW1LEyn-fK554s"
    file=img_name
    file_from=file
    file_to="/NewFolder1/"+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb')as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            uploadFile(name)

main()            
 
    
    

    

    
        
         

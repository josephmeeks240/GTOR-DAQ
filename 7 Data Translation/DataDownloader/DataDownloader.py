import shutil
import os
import time
#handles data download and includes basic progress bar
def downloadData(src, dst):
    #sets oldTime
    oldTime = time.time()
    #initializes a variable to keep track of last download speed
    previousDownloadSpeed = 0
    #initializes variable to keep track of num megs to have in buffer
    numMegs = 10
    #creates boolean to tell program if it should wait to reduce buffer size
    wait = True
    #opens the source and destination files    
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        #creates a variable to keep track of data copied so far
        copied = 0
        #creates a variable to hold buffer size
        bufferSize = numMegs * 1024 * 1024  # Copy in numMegsMB chunks
        while True:
            #reads data from file into buffer (I think this uses shutil but not sure)
            buf = fsrc.read(bufferSize)
            #if buffer is empty
            if not buf:
                break
            #write buffer to file
            fdst.write(buf)
            #add buffer length to copied variable
            copied += len(buf)
            #calculate download speed (if it downloades numMegs in less than a second than call download speed infinite)
            try:
                downloadSpeed = round(((numMegs)/(time.time() - oldTime)),2)
                if (downloadSpeed < previousDownloadSpeed) and not wait:
                    numMegs -= 2
                    #prevent numMegs from going below 1
                    if numMegs <= 0:
                        numMegs = 1
                    previousNumMegs = numMegs
                    wait = True
                elif wait:
                    wait = False
                previousDownloadSpeed = downloadSpeed
            except:
                downloadSpeed = float(inf)
            #increments numMegs to try and find optimum download rate
            if not wait:
                numMegs += 1

def updateProgressBar(src, dst, progressBar, progressBarPage, label, parentPage):
    sourceFileSize = os.path.getsize(src)
    while os.path.getsize(dst) != sourceFileSize:
        percentage = os.path.getsize(dst)/sourceFileSize * 100
        progressBar["value"] = percentage
        label.config(text = str("Download Progress " + str(round(percentage,2)) + "%"))
        label.pack()
        progressBar.pack()
        progressBarPage.update()
    progressBarPage.destroy()
    parentPage.deiconify()
    
    
            

# iterate all folder include child folders
# keep only videos and torrents
import os

def deleteFiles(dir, extension):
    res = open('videoNames2.txt','a')
    res.write('Files deleted:\r')
    for dirName, subdirList, fileList in os.walk(dir):
        for fname in fileList:
            if fname.lower().endswith(extension):
                filepath = os.path.join(dirName,fname)
                os.remove(filepath)
                res.write('\t%s\r' % filepath) 
                res.write('\t%s\r' % fname)
    res.close()   
            
    

def getAllFile(dir):
    res = open('videoNames2.txt','w')
    for dirName, subdirList, fileList in os.walk(dir):
        res.write('Found directory: %s\r' % dirName)
        for fname in fileList:
            res.write('\t%s\r' % fname)
    res.close()

dir = os.getcwd()
#getAllFile(dir)
deleteFiles(dir,'____')
deleteFiles(dir,'.html')
deleteFiles(dir,'.chm')



    
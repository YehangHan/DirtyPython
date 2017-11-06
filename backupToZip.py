#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.
#
import zipfile, os


def backupToZip(folder,ext):
    # Backup certain type of contents of "folder" into a ZIP file based on the file extension.
    
    folder = os.path.abspath(folder) # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        finalzipFilename = os.path.join(folder,zipFilename)
        if not os.path.exists(finalzipFilename):
            break
        number = number + 1
    # TODO: Create the ZIP file.
    print('Creating %s...' % (finalzipFilename))
    backupZip = zipfile.ZipFile(finalzipFilename,'w')

       # TODO: Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
           # Add the current folder to the ZIP file.
        backupZip.write(foldername)
            # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                   continue   # don't backup the backup ZIP files
            if(filename.endswith(ext)):       
                backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip(r'dir','.pdf')
    
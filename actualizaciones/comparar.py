import fnmatch
import os
import shutil
import zipfile
import sys
import filecmp

def unzip(zfilename):
    # open the zipped file
    zfile = zipfile.ZipFile( zfilename, "r" )
    # retrieve information about the zip file
    zfile.printdir()
    print '-'*40
    # get each archived file and process the decompressed data
    for info in zfile.infolist():
        fname = info.filename
        # decompress each file's data
        data = zfile.read(fname)
        
        if not data:
            if os.path.exists('unzipped_' + fname):
                shutil.rmtree('unzipped_' + fname)
                os.makedirs('unzipped_' + fname)
            else:
                os.makedirs('unzipped_' + fname)

        else:
            # save the decompressed data to a new file
            filename = 'unzipped_' + fname
            fout = open(filename, "w")
            fout.write(data)
            fout.close()
            print "New file created --> %s" % filename
            print '-'*40


def compareAndSwitch():
    matches = []
    for root, dirnames, filenames in os.walk("/home/systmatic2/Desktop/examples/actualizaciones/"):
        for filename in fnmatch.filter(filenames, '*.txt'):
            matches.append(os.path.join(root, filename))

    print '-'*40
    print "Verify Files"
    print '-'*40
    print matches

    for filen in matches:
        #import pdb; pdb.set_trace()
        if not filecmp.cmp(filen, '../prueba.txt'):
            print "File updated --> %s" % str(filen)
            shutil.copy(filen, '../prueba.txt')


compareAndSwitch()
#unzip('vm.zip')
#compareAndSwitch()
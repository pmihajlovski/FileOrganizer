import argparse
import os
import shutil
parser = argparse.ArgumentParser()
parser.add_argument("file",help="Inserire file da spostare", type=str)
args = parser.parse_args()
audio_ext = ["png","jpg","jpeg"]
text_ext = ["txt","odt"]
music_ext = ["mp3","mp4"]
#utilizzo il codice presente nel main senza utilizzare il ciclo for
#il nome del file viene passato attraverso il terminale
def addfile(file):
    path= os.getcwd()+"/files"
    name, extensions = os.path.splitext(file)
    extensions = extensions[1:]
    print ("{} type:{}  size{}".format(name,extensions,os.path.getsize(path+"/"+file)))
    with open(path+"/recap.csv", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(1000)
        if len (data) > 0:
            file_object.write("\n")
        file_object.write("{} type:{}  size{}".format(name,extensions,os.path.getsize(path+"/"+file)))
    if extensions in text_ext:
        shutil.move(path+"/"+file, path+"/docs/"+file)
    elif extensions in audio_ext:
        shutil.move(path+"/"+file, path+"/images/"+file)
    elif extensions in music_ext :
        shutil.move(path+"/"+file, path+"/audio/"+file)
print(addfile(args.file))
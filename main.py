import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):

    def on_created(self, event):

        # 1. Get list of all current folders
        folderNames = [f.name for f in os.scandir(downloadsPath) if f.is_dir()]
        fileNames = [f.name for f in os.scandir(downloadsPath) if f.is_file()]

        # 2. For the new file, check if the folder exists
        for fileName in fileNames:
            extension = fileName.split('.')[-1]
            filePath = downloadsPath + '/' + fileName

            # 3. If not, make a new folder for it
            if extension not in folderNames:
                os.mkdir(downloadsPath + '/' + extension)

            destinationPath = downloadsPath + '/' + extension + '/' + fileName

            # 4. Move the file in respective folder
            os.rename(filePath, destinationPath)


downloadsPath = "/Users/omdharme/Downloads"

observer = Observer()
handler = Handler()

observer.schedule(handler, downloadsPath)
observer.start()

try:
    while True:
        time.sleep(5)
except KeyboardInterrupt:
    observer.stop()

observer.join()

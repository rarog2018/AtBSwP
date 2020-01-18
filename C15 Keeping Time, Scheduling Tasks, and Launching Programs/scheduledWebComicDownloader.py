#! python3
# checks if the comic site was updated since last visit and downloads new
# images if it was

# TODO: functions that checks if the sites were updated since last visit, 
# or maybe it will be done as plugins, so each site will have its own unique
# function that will do the job, each can open in a different thread

import datetime, json, os, threading
import comicPlugins.xkcdPlugin as xkcd
import comicPlugins.lhtPlugin as lht

# global variables
infoFName = 'info.json' 
pluginList = [xkcd, lht]
fileDict = {}       # dictionary that stores the contents of the info file
comicRange = []     # store the ranges of comics to download for each plugin

# setups downloads in multiple threads
def multithreadDownload():
    downloadThreads = []    # will be used to wait till all threads are done
    plugNum = 0             # helper variable to index comicRange list
    downloading = False     # to print message if downloading was finished

    # update time
    fileDict["updated"] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # loop through every plugin in pluginList
    for plugin in pluginList:
        # range starts with the start, end indexes for specific plugin in 
        # comicRange list, each plugin is added to the list in a certain order
        # and each has specific indexes reserved for it
        for i in range(comicRange[plugNum], comicRange[plugNum + 1], 100):
            downloading = True
            # prevent the situation when last comic number is for example 1250
            # to not go from 51 to 99
            if i + 99 > comicRange[plugNum]:
                # in that case we go to 1250 instead of 1299
                downloadThread = threading.Thread(
                    target=plugin.download_comics, args=(i, comicRange[plugNum + 1] + 1))
            else:
                downloadThread = threading.Thread(
                    target=plugin.download_comics, args=(i, i+99))
            downloadThreads.append(downloadThread)  # update thread list
            downloadThread.start()  # start new thread

        # update the dictionary so the info file will show store the last 
        # downloaded comic number for each plugin
        fileDict[str(plugin)] = comicRange[plugNum + 1]
        plugNum += 2    # update plugin index, to fetch correct range

    # wait till the threads are done
    for downloadThread in downloadThreads:
        downloadThread.join()

    if downloading:
        print("Downloading finished, threads closed.")
    else:
        print("Comics up to date")

def writeToFile():
    infoFile = open(infoFName, 'w')
    json.dump(fileDict, infoFile)
    infoFile.close()

# if the file info does not exist or its empty
if not os.path.isfile(infoFName) or os.path.getsize(infoFName) == 0:
    print("The file %s does not exist or is empty" % infoFName)
    print("Preparing first download")

    # create downloads directory
    os.makedirs('comicDownloads', exist_ok=True)
    
    # if we are here then we will need to call the first time functions 
    # update comicRange
    for plugin in pluginList:
        comicRange.append(0)
        comicRange.append(plugin.first_preparation())

    print("Preparations finished")

    # download the comics
    multithreadDownload()

    # set up the info file
    writeToFile()

# if the file exists and is not empty
else:
    # read the file
    infoFile = open(infoFName, 'r')
    fileDict = json.load(infoFile)
    infoFile.close()

    # update comic ranges
    for plugin in pluginList:
        comicRange.append(fileDict[str(plugin)])
        comicRange.append(plugin.check_last_number())

    # print info about time    
    print("Last updated %s" % fileDict["updated"])

    # download the comics
    multithreadDownload()

    # write data to the file
    writeToFile()

print("Done")

import glob, os



def find(name, path):
    #path = "/Users/hirenkumarpatel/Desktop/pyth/*/"
    file_dir_extension = os.path.join(path, name)
    # "/Users/hirenkumarpatel/Desktop/pyth/*/*.xlsx"
    print(file_dir_extension)
    for f in glob.iglob(file_dir_extension):  # generator, search immediate subdirectories
        print(f)

def dailyDownloadFile():
    import time
    import datetime
    mydate = datetime.datetime.now()
    file_extn = "CFS_ANZ_Daily_Download_"
    currentMonth = mydate.strftime("%b")
    print(mydate.strftime("%b"))
    todayDate = time.strftime(currentMonth+"_%dth_%Y.xlsx")
    print(file_extn+todayDate)
    return  todayDate

while True:
    givenName = input('Give file name ? >')
    if givenName == "":
        givenName = dailyDownloadFile()

    if givenName == 'done':
        break
    if givenName == 'help':
        print('type in Give File Nmae *.extention or filr name')
        print('type in Give File Path /dir1/secondary diectory/')
        print("type 'done' to exit programe ")
    if givenName == "sifile":
         pathName = input('give path to get Daily down load file ? >')

         pathNameExten = os.path.join(pathName, '*/')
         #dailyDownloadFile()
         continue

    else:
        pathName = input('Give file path >')
        pathNameExten = os.path.join(pathName, '*/')
        find(givenName, pathNameExten)
        continue













import glob, os



def find(name, path):
    #path = "/Users/hirenkumarpatel/Desktop/pyth/*/"
    file_dir_extension = os.path.join(path, name)
    # "/Users/hirenkumarpatel/Desktop/pyth/*/*.xlsx"
    print(file_dir_extension)
    for f in glob.iglob(file_dir_extension):  # generator, search immediate subdirectories
        print(f)



while True:
    givenName = input('Give file name ? >')

    if givenName == 'done':
        break
    if givenName == 'help':
        print('type in Give File Nmae *.extention or filr name')
        print('type in Give File Path /dir1/secondary diectory/')
        print("type 'done' to exit programe ")
    else:
        pathName = input('Give file path >')
        pathNameExten = os.path.join(pathName, '*/')
        find(givenName, pathNameExten)
        continue













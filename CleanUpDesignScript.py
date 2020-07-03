import os
import shutil
import re

# FOLDERS TO REMOVE
ddirs = ['BackupDatabase',
         'Layout_Temp',
         'Replay',
         'Output',
         'Layout/3D',
         'Instrument',
         'amalakho',
         'bak',
         'CES',
         'ProjectBackup',
         'cdbback',
         'cdbsvr']

# FILES TO REMOVE
del_files = [r'\b[.]\brec_\d$',
             r'\b[.]\btrs_\d$',
             r'\bCheckSum[.]\bdat',
             r'\bJobPrefsDB[.]\bbak$',
             r'\bPCBIndicators[.]\bcaf$',
             r'\bSession[.]\blog$',
             r'\bDffSliverViolations[.]\bdat$',
             r'\bFailures[.]\btxt$',
             r'\bSketchPlanVer[.]\bdatErr[.]\btxt$',
             r'\bPlayback[.]\btrs$',
             r'\bProjectBackupLog[.]\btxt$',
             r'\bfui[.]\btxt$',
             r'\bsvrmsglog[.]\btxt$',
             r'\bSR\-\bTF\-\bdesign[.]\btxt$',
             r'\bSR\-\bStat[.]\btxt$',
             r'\bOpens\-\bBeforeSR[.]\btxt$',
             r'\bOpens\-\bAfterSR[.]\btxt$',
             r'\bsvrmsglog[.]\btxt$',
             r'\bAutoRouteReport[.]\btxt$',
             r'\bCustomAR[.]\btxt$',
             r'\bDrcDff[.]\btxt$',
             r'\bMVO[*]\brules[*]\blog[.]\btxt$']


#currentdir = input("Please enter the directory: ") #/Users/alex/PycharmProjects/CleanUpDesignFolder/issue18
currentdir = '/Users/alexey/PycharmProjects/CleanUpDesignScript/Example'

print('\n' + '*' * 40 + ' CLEANUP STARTS FROM HERE ' + '*' * 40 + '\n')
print('-'*110)
for roots, dirs, files in os.walk(currentdir):
    for dir in dirs:
        dir_path = os.path.join(roots,dir)
        #print("Directory : %s" % dir_path)
        for ddir in ddirs:
            cur_path=os.path.join(roots,ddir)
            if dir_path == cur_path:
                #print(dir_path)
                print('THIS FOLDER WAS REMOVED: '+(dir_path))
                #shutil.rmtree(dir_path) # удаление найденой директории
                print('-'*110)
            #else:
                #print("Чего-то не то!")
    for file in files:
        #print(file)
        for del_file in del_files:
            file_refs = re.compile(del_file)
            matches = file_refs.search(file)
            file_path = os.path.join(roots, file)
            if matches:
                print('THIS FILE WAS REMOVED: ' + (file_path))
                #os.remove(file_path) # удаление найденного файла
                print('-' * 110)
            #else:
                #print("Чего-то не то!")
'''
if os.path.exists(currentdir):
else:
    print("!!!No such directory!!!")
'''
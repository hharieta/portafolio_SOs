# Comandos usados en los niveles de Bandit

## Level 0 `->` 1

```bash 
du -a
cat $HOME/readme
********************************
exit
```

## Level 1 `->` 2

```bash
find . -type f -name - 2> /dev/null
cat ~/-
********************************
exit
```

## Level 2 `->` 3

```bash
du -a
cat ./"spaces in this filename"
********************************
exit
```

## Level 3 `->` 4

```bash
ls -a ~/inhere
cat ~/inhere/.hidden
********************************
exit
```

## Level 4 `->` 5

```bash
ls
cd inhere
#du -h
#du -a
#find . -type f -exec sh -c 'file -b {} &> /dev/null' \; -print
find . -type f | xargs file | grep text
cat ./-file07
********************************
exit
```

## Level 5 `->` 6

```bash
ls -a ~/inhere
#find . -size 1033 -type f | xargs file | grep text
find . -size 1033c -type f | xargs file | grep text
cat $HOME/inhere/maybehere07/.file2 
********************************
exit
```

## Level 6 `->` 7

```bash
#find . -size 33c -user bandit7 -group bandit6 -type f
#find / -size 33c -user bandit7 -group bandit6 -type f
find / -size 33c -user bandit7 -group bandit6 -type f 2> /dev/null
ls -la /var/lib/dpkg/info/bandit7.password
cat /var/lib/dpkg/info/bandit7.password
********************************
exit
```

## Level 7 `->` 8

```bash
ls 
#cat data.txt
#cat data.txt | base64 -d
#cat data.txt | grep  millionth
#cat data.txt | grep -w  millionth
#cat data.txt | grep -w millionth | head -1
#cat data.txt | grep -w millionth | head -1 | awk {$2} | print
#cat data.txt | grep -w millionth | head -1 | awk {print $2}
cat data.txt | grep -w millionth | head -1 | awk '{print $2}'
********************************
exit
```

## Level 8 `->` 9

```bash
ls
#cat data.txt | uniq -c
#sort data.txt | uniq
#sort data.txt | uniq -c
#awk '!x[$0]++' data.txt
#grep -wo data.txt | sort data.txt | uniq -c
#grep -wo data.txt | sort data.txt | uniq -c | awk '{if ($? == 0) print}'
#grep -wo data.txt | sort data.txt | uniq -c | awk '$1 ~ /1/ {print}' data.txt
#grep -wo data.txt | sort data.txt | uniq -c | awk '$1 == "1" {print $2}' data.txt
#grep -wo data.txt | sort data.txt | uniq -c | awk '$1 == "1" {print $2}'
#********************************
sort data.txt | uniq -c | awk '$1 == 1 {print $2}'
********************************
exit
```

## Level 9 `->` 10

```bash
ls
#cat data.txt
#grep "=====" data.txt
#xxd data.txt
#xxd data.txt | awk '{print $10}'
#xxd data.txt | awk '$10 ~ !/^==/ {print $10}'
#xxd data.txt | awk '($10 ~ /^[A-Za-z0-9\s]/ {print $10}'
#xxd data.txt | awk '($10 !~ /^=*/) && ($10 !~ /^.*/) {print $10}'
#xxd data.txt | awk '$10 !~ /*..*/ {print $10}' | grep -A 1 "========"
#xxd data.txt | awk '$10 !~ /^..*/ {print $10}' | grep -A 1 "========"
#xxd data.txt | awk '$10 !~ /...*/ {print $10}' | grep -A 1 "====="
#xxd data.txt | awk '{print $10}' | grep -A 1 "="
#xxd data.txt | awk '{print $10}' | grep -A 1 "^="
#xxd data.txt | awk '{print $10}' | grep -A 1 "^=" | tail -1
#6J3kTb8A7j9Lgryw
#6J3kTb8A7j9LgrywtEUlyyp6s
strings data.txt | awk '$1 ~/=/ {print $2}'
strings data.txt | awk '$1 ~ /=/ {print $2}' | grep "^G"
********************************
exit
```

## Level 10 `->` 11

```bash
base64 -d data.txt
base64 -d data.txt | awk '{print $4}'
********************************
exit
```

## Level 11 `->` 12

![ejemplo de rotación](assets/letras.jpg)

```bash
#cat data.txt
#base64 -d data.txt | tr "A-Za-z" "N-ZA-Mn-za-m"
#cat data.txt | tr "A-Za-z" "N-ZA-Mn-za-m"
cat data.txt | tr "A-Za-z" "N-ZA-Mn-za-m" | awk '{print $4}'
********************************
exit
```

## Level 12 `->` 13

```bash
ls
mkdir /tmp/gatovsky
cp data.txt /tmp/gatovsky && cd /tmp/gatovsky
mv data.txt data
cat data | xxd -r > data1
file data1
#data1: gzip compressed data
ls
mv data1 data2.gz
gzip -c data2.gz
gzip -d data2.gz
file data2
#data2: bzip2 compressed data
mv data2 data3.bz
bzip2 -d data3.bz
file data3
#data3: gzip compressed data
ls
mv data3 data4.gz
gzip -d data4.gz
file data4
#data4: POSIX tar archive
cp data4 data4-2 # respaldo por si la cago
mv data4 data5.tar
tar -xf data5.tar
ls
./data5.bin
file data5.bin
#data5.bin: POSIX tar archive
mv data5.bin data6.tar
tar -xf data6.tar
file data6.bin
#data6.bin: bzip2 compressed data
mv data6.bin data7.bz
bzip2 -d data7.bz
ls
file data7
data7: POSIX tar archive
mv data7 data8.tar
tar -xf data8.tar
file data8.bin
#data8.bin: gzip compressed data
ls
mv data8.bin data9.gz
gzip -d data9.gz
file data9
#data9: ASCII text
cat data9 | awk '{print $4}'
********************************
exit
```

## Level 13 `->` 14

```bash
#ssh-keygen
#mkdir .shh
#ssh-copy-id -i sshkey.private bandit14@bandit
#ssh bandit14@bandit 
#ssh bandit14@bandit -i sshkey.private
#ssh bandit14@localhost -i sshkey.private
ssh bandit14@localhost -i sshkey.private -p 2220
```

## Level 14 `->` 15

```bash
cat /etc/bandit_pass/bandit14 
********************************
#nc "********************************" localhost 30000
cat /etc/bandit_pass/bandit14 | nc localhost 30000
********************************
exit
exit
```

## Level 15 `->` 16

```bash
cat /etc/bandit_pass/bandit15 
openssl s_client -connect localhost:30001
#cat /etc/bandit_pass/bandit15 | openssl s_client -connect localhost:30001
#cat /etc/bandit_pass/bandit15 | openssl aes-256-cbc localhost:30001
#cat /etc/bandit_pass/bandit15 | openssl aes-256-cbc s_client localhost:30001
#cat /etc/bandit_pass/bandit15 | openssl -ign_eof localhost:30001
cat /etc/bandit_pass/bandit15 | openssl s_client -ign_eof localhost:30001
Correct!
********************************
exit
```

## Level 16 `->` 17

```bash
nc -zv localhost 31000-32000 >& /tmp/ports.txt 
cat /tmp/ports.txt 
cat /tmp/ports.txt |  grep "^Connection"
cat /tmp/ports.txt |  grep "^Connection" | awk '{print $5}' > /tmp/ports2.txt
cat /tmp/ports2.txt
31046
31518
31691
31790
31960
#for i in $(cat /tmp/ports2.txt); do openssl s_client -connect localhost:$i; done;
#openssl s_client -connect localhost:31046
openssl s_client -connect localhost:31518
#openssl s_client -connect localhost:31691
openssl s_client -connect localhost:31790
#openssl s_client -connect localhost:31960
#********************************
echo "********************************" | openssl s_client -ign_eof localhost:31518
cat /etc/bandit_pass/bandit16 | openssl s_client -ign_eof localhost:31790
cat /etc/bandit_pass/bandit16 | openssl s_client -ign_eof localhost:31790 | grep -A 26 "BEGIN RSA"  > /tmp/sshkey.private
cat /tmp/sshkey.private
ssh -i /tmp/sshkey.private bandit17@localhost -p 2220
```

## Level 17 `->` 18

```bash
diff -c passwords.new passwords.old
cat passwords.new | grep "********************************"
********************************
exit 
exit
```

## Level 18 `->` 19

```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 
Byebye !
#ssh bandit18@bandit.labs.overthewire.org -p 2220 | cat ~/readme
#sh bandit18@bandit.labs.overthewire.org -p 2220 && cat ~/readme
sh bandit18@bandit.labs.overthewire.org -p 2220  “cat ~/readme”
********************************
```

## Level 19 `->` 20

```bash
/bandit20-do
./bandit20-do id
uid=11019(bandit19) gid=11019(bandit19) euid=11020(bandit20) groups=11019(bandit19)
file bandit20-do
ls -ll bandit20-do
groups bandit19
#id -u
#./bandit20-do id cat /etc/bandi>&t_pass/bandit20
./bandit20-do cat /etc/bandit_pass/bandit20
********************************
exit
```

## Level 20 `->` 21

* nc -l – This command will instruct the local system to begin listening for TCP connections and UDP activity on a specific port number.

🗒️ Nota: levantar un servidor  que escuche conexiones `TCP / UDP` en segundo plano a través de un puerto específico y que devuelva la contraseña del nivel actual, verificar que el server esté levantado y posterior hacer uso del binario `suconnect` con el puerto del servidor

```bash
ls
./suconnect
Usage: ./suconnect <portnumber>
#./suconnect 2220 | "cat /etc/bandit_pass/bandit20"
#cat /etc/bandit_pass/bandit20 | ./suconnect 2220
#"********************************" | nc -l localhost 31002
#"********************************" | nc -l localhost 31002 & # proceso levantado erroneamente
#3051766 # IDP
echo "********************************" | nc -l localhost 31002 &
3051922 # IDP
ps aux 
kill 3051766 # matar proceso levantado por error
./suconnect 31002 # ejecutar el binario con el puerto especificado anteriormente 
Read: ********************************
Password matches, sending next password
********************************
exit
```

## Level 21 `->` 22

```bash
ps aux
cd /etc/cron.d
ls -la
#crontab -l
#crontab -e
cat cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
cat /usr/bin/cronjob_bandit22.sh 
#!/bin/bash
chmod 644 /tmp/********************************
cat /etc/bandit_pass/bandit22 > /tmp/********************************

cat /tmp/********************************
********************************
exit
```

## Level 22 `->` 23

```bash
cd /etc/cron.d/
ls -la
cat cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /etc/bandit_pass/$myname > /tmp/$mytarget

bash /usr/bin/cronjob_bandit23.sh
cat /tmp/********************************
********************************

#md5sum /tmp/********************************
#vim /tmp/superHacker.sh
#ls -la /usr/bin/cronjob_bandit23.sh
#chmod 750 /tmp/superHacker.sh

#Busca la clave MD5 que corresponde a bandit23, su password ya está en /tmp/”clave”
myname=bandit23
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo $mytarget
********************************
cat /tmp/********************************
********************************
exit
```

## Level 23 `->` 24

```bash
cd /etc/cron.d
ls -la
cat cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
***** bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null

cat /usr/bin/cronjob_bandit24.sh

mkdir /tmp/wenas
touch /tmp/wenas/pass
cat >> /tmp/wenas/gatovksyHacker.sh << EOF
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/wenas/pass
EOF

chmod 777 /tmp/wenas/pass
chmod 777  /tmp/wenas/gatovksyHacker.sh

cp /tmp/wenas/gatovskyHacker.sh /var/spool/bandit24/foo
bash /usr/bin/cronjob_bandit24.sh 
cat /tmp/wenas/pass
********************************
exit
```
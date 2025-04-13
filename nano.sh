#!/usr/bin/sh 
printf "\033c\033[43;30m\ndownloa gcc"
wget "https://www.nano-editor.org/dist/v4/nano-4.0.tar.gz" 
gzip -d 'nano-4.0.tar.gz'
tar --extract -f 'nano-4.0.tar'
cd linux-6.15-rc1
 
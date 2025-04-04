printf "\033c\033[43;30m\n"
ls -l $1
zip -r -9  $1.wallet $1 
ls -l $1.wallet
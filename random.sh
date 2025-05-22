printf "\033c\033[43;30m\n"
while true
    do
        
        
        echo "" > index.tmp
        for a in range 1 2 3 4 5 6 7 8
            do
                random_number=$(od -An -N2 -i /dev/urandom)
                r=$(expr $random_number '/' 1000)
                printf $r, >> index.tmp
            done
        cat index.tmp
        cp index.tmp index.html
        sleep 24
    done

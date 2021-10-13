
screenmsg() {
    echo $* > /dev/ttyprintk 2>&1
}


#!/bin/bash

if [[ $EUID -ne 0 ]];
then
    echo "must be root !"
    exit 1
fi

if [[ $# < 1 ]];
then
    echo "must have target"
    exit 1
fi

if [ ! -d $1 ];
then
    echo "target must be a directory"
    exit 1
fi

TARGET=$1

echo "begin install plugin"

# copy frontend and ui
sudo cp -v usr/lib/ubiquity/plugins/ubi-packagesetup.py $TARGET/usr/lib/ubiquity/plugins/
sudo cp -v usr/share/ubiquity/gtk/stepPackageSetup.ui $TARGET/usr/share/ubiquity/gtk/

# copy command
sudo cp -rvf usr/lib/ubiquity/packagesetup $TARGET/usr/lib/ubiquity/
sudo chmod +x $TARGET/usr/lib/ubiquity/packagesetup/*

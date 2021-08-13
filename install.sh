#!/bin/bash

if [[ $EUID -ne 0 ]];
then
    echo "must be root !"
    exit 1
fi

echo "begin install plugin"


# copy frontend and ui
sudo cp -v usr/lib/ubiquity/plugins/ubi-packagesetup.py /usr/lib/ubiquity/plugins/
sudo cp -v usr/share/ubiquity/gtk/stepPackageSetup.ui /usr/share/ubiquity/gtk/

# copy command
sudo cp -rvf usr/lib/ubiquity/packagesetup /usr/lib/ubiquity/
sudo chmod +x /usr/lib/ubiquity/packagesetup/*

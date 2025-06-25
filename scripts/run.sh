#!/bin/bash

VERSION=$(cat desktopapptemplate/src/desktopapptemplate/resources/VERSION)

if [ "${1}" == "" ]; then

    cd desktopapptemplate
    briefcase dev

elif [ "${1}" == "--test" ]; then

    cd desktopapptemplate
    briefcase dev --test

elif [ "${1}" == "--exe" ]; then

    cd desktopapptemplate
    briefcase run

elif [ "${1}" == "--build" ]; then

    rm -rf desktopapptemplate/build
    python scripts/python/updatetomlversion.py ${VERSION}
    python scripts/python/updatetomlrequirements.py
    cd desktopapptemplate
    briefcase create
    briefcase build

elif [ "${1}" == "--package" ]; then

    cd desktopapptemplate
    briefcase package --adhoc-sign
fi
#!/usr/bin/env bash

case "$(uname -sr)" in

Darwin*)
    echo 'Mac OS install not implemented, please refer to the README.md'
    ;;

Linux*Microsoft*)
    # Windows Subsystem for Linux
    echo 'WSL install not implemented, please refer to the README.md'
    ;;

Linux*)
    echo 'Linux install not implemented, please refer to the README.md'
    ;;

CYGWIN* | MINGW* | MINGW32* | MSYS*)
    # MS Windows
    read -p "Enter Blender version e.g. 3.1 > " VER
    DIR="${APPDATA}/Blender Foundation/Blender/${VER}"
    if [ ! -d "$DIR" ]; then
        read -p "Blender version ${VER} doesn't exist, please enter correct version > " VER
        DIR="${APPDATA}/Blender Foundation/Blender/${VER}"
        echo $DIR
    fi
    if [ ! -d "$DIR" ]; then
        echo "Blender version ${VER} doesn't exist, exiting."
        exit 1
    fi
    
    read -p "Install configs (y/n)?" CPCONF
    case "$CPCONF" in
    y | Y)
        cp -r ./HEAVYPOLY_Blender/config "$DIR"
        cp -r ./config "$DIR"
        ;;
    *) ;;
    esac

    read -p "Install scripts (y/n)?" CPSCRIPTS
    case "$CPSCRIPTS" in
    y | Y)
        cp -r ./HEAVYPOLY_Blender/scripts "$DIR"
        cp -r ./scripts "$DIR"
        ;;
    *) ;;
    esac
    ;;

*)
    echo 'Install not supported on this OS'
    ;;
esac

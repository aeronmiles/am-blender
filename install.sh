#!/usr/bin/env bash

read -p "Enter Blender version e.g. 3.3 > " VER
DIR="${APPDATA}/Blender Foundation/Blender/${VER}"
if [ ! -d "$DIR" ]; then
    read -p "Blender version ${VER} doesn't exist, please enter correct version > " VER
    DIR="${APPDATA}/Blender Foundation/Blender/${VER}"
fi
if [ ! -d "$DIR" ]; then
    echo "Blender version ${VER} doesn't exist, exiting."
    exit 1
fi

case "$(uname -sr)" in

Darwin*)
    echo 'Mac OS install not implemented, feel free to submit a merge request. Otherwise, keep calm and carry on.'
    ;;

Linux*Microsoft*)
    echo 'WSL install not implemented, feel free to submit a merge request. Otherwise, keep calm and carry on.'
    ;;

Linux*)
    echo 'Linux install not implemented, feel free to submit a merge request. Otherwise, keep calm and carry on.'
    ;;

CYGWIN* | MINGW* | MINGW32* | MSYS*)
    # MS Windows

    # read -p "Install configs (y/n)? " CPCONF
    # case "$CPCONF" in
    # y | Y)
    #     cp -r ./config "$DIR"
    #     ;;
    # *) ;;
    # esac

    # read -p "Install scripts (y/n)? " CPSCRIPTS
    # case "$CPSCRIPTS" in
    # y | Y)
    #     cp -r ./HEAVYPOLY_Blender/scripts "$DIR"
    #     cp -r ./scripts "$DIR"
    #     ;;
    # *) ;;
    # esac

    ### USDZ
    if [ -d "$DIR/scripts/addons/io_scene_usdz" ]; then
        rm -r "$DIR/scripts/addons/io_scene_usdz"
    fi
    cp -r ./extern/addons/BlenderUSDZ/io_scene_usdz "$DIR/scripts/addons"

    ### reload_addons
    if [ -f "$DIR/scripts/addons/reload_addons.py" ]; then
        rm -f "$DIR/scripts/addons/reload_addons.py"
    fi
    cp ./extern/addons/john-kanji/reload_addons.py "$DIR/scripts/addons"

    ### am-blender
    if [ -d "$DIR/scripts/addons/am-blender" ]; then
        rm -r "$DIR/scripts/addons/am-blender"
    fi
    cp -r ./scripts "$DIR"

    ;;
*)

    echo 'Install not supported on this OS'
    ;;
esac

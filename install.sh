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

    ### HEAVYPOLY as addon
    echo '@TODO: io scene & heavypoly move to addons'

    ### Bake Groups
    if [ -d "$DIR/scripts/addons/addon_bake_groups" ]; then
        rm -r "$DIR/scripts/addons/addon_bake_groups"
    fi
    cp -r ./3rd-party/addons/addon_bake_groups "$DIR/scripts/addons"

    ### USDZ
    if [ -d "$DIR/scripts/startup/io_scene_usdz" ]; then
        rm -r "$DIR/scripts/startup/io_scene_usdz"
    fi
    cp -r ./3rd-party/addons/BlenderUSDZ/io_scene_usdz "$DIR/scripts/startup"
    
    ### HEAVYPOLY
    cp -r ./3rd-party/addons/HEAVYPOLY_Blender/scripts "$DIR"

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

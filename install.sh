#!/usr/bin/env bash

read -p "Enter Blender version e.g. 3.3 > " VER

# Determine the user's directory based on the operating system
case "$(uname -sr)" in
Darwin*)
    # macOS
    USER_PATH="/Users/${USER}/Library/Application Support/Blender/${VER}"
    ;;
Linux*Microsoft*)
    # WSL
    USER_PATH="${APPDATA}/Blender Foundation/Blender/${VER}"
    ;;
Linux*)
    # Linux
    USER_PATH="${HOME}/.config/blender/${VER}"
    ;;
CYGWIN* | MINGW* | MINGW32* | MSYS*)
    # MS Windows
    USER_PATH="${APPDATA}/Blender Foundation/Blender/${VER}"
    ;;
*)
    # Unsupported operating system
    echo "Install not supported on this OS"
    exit 1
    ;;
esac

if [ ! -d "$USER_PATH" ]; then
    echo "Blender version ${VER} doesn't exist, exiting."
    exit 1
fi

# Install Extern addons
# USDZ
if [ -d "$USER_PATH/scripts/addons/io_scene_usdz" ]; then
    rm -r "$USER_PATH/scripts/addons/io_scene_usdz"
fi
cp -r ./addons-extern/BlenderUSDZ/io_scene_usdz "$USER_PATH/scripts/addons"

# Install Intern addons
# remove previous heavypoly
if [ -d "$USER_PATH/scripts/addons/heavypoly" ]; then
    rm -r "$USER_PATH/scripts/addons/heavypoly"
fi
# remove previous reload_addons
if [ -d "$USER_PATH/scripts/addons/reload_addons" ]; then
    rm -r "$USER_PATH/scripts/addons/reload_addons"
fi
### remove previous am_blender
if [ -d "$USER_PATH/scripts/addons/am_blender" ]; then
    rm -r "$USER_PATH/scripts/addons/am_blender"
fi
cp -r ./addons "$USER_PATH/scripts"
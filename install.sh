#!/usr/bin/env bash

read -p "Enter Blender version e.g. 3.3 > " VER

# Determine the user's addons directory based on the operating system
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

# Install the addons
# USDZ
if [ -d "$USER_PATH/scripts/addons/io_scene_usdz" ]; then
    rm -r "$USER_PATH/scripts/addons/io_scene_usdz"
fi
cp -r ./extern/addons/BlenderUSDZ/io_scene_usdz "$USER_PATH/scripts/addons"

# reload_addons
if [ -f "$USER_PATH/scripts/addons/reload_addons.py" ]; then
    rm -f "$USER_PATH/scripts/addons/reload_addons.py"
fi
cp ./extern/addons/john-kanji/reload_addons.py "$USER_PATH/scripts/addons"

### am-blender
if [ -d "$USER_PATH/scripts/addons/am-blender" ]; then
    rm -r "$USER_PATH/scripts/addons/am-blender"
fi
cp -r ./scripts "$USER_PATH"

#!/bin/bash

# variables
SCRIPT_MIN_VERSION=$2
if [ "$UID" -ne "0" ] ; then
    SCRIPT_CONF_DIR=~/.config/sedoo
else
    SCRIPT_CONF_DIR=/etc/sedoo
fi 
SCRIPT_CONF_FILE=$SCRIPT_CONF_DIR/$1

# vérifications script
if [ -e "$SCRIPT_CONF_FILE" ] ; then
    read -r SCRIPT_CONF_FILE_VERSION<$SCRIPT_CONF_FILE
    SCRIPT_MIN_VERSION_INT=$((SCRIPT_MIN_VERSION))
    SCRIPT_CONF_FILE_VERSION_INT=$((SCRIPT_CONF_FILE_VERSION))
    if [ $SCRIPT_CONF_FILE_VERSION_INT -ge $SCRIPT_MIN_VERSION_INT ]; then
        exit 0
    else
        if [ $SCRIPT_CONF_FILE_VERSION_INT -eq 0 ]; then
            echo "Version invalide du script $1"
            exit -1
        fi
        echo "Le script $1 doit être réinstallé"
        echo "Version installée = $SCRIPT_CONF_FILE_VERSION_INT"
        echo "Version requise = $SCRIPT_MIN_VERSION_INT"
        exit $SCRIPT_CONF_FILE_VERSION_INT
    fi
else
    echo "Il faut d'abord installer le script $1"
    exit -1
fi

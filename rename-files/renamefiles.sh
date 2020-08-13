#! /bin/bash

dirname=$( basename "$( cd "${@: -1}" && pwd )" )
prefix=""

for arg in "$@"
do
    case $arg in
        -d | --directory)
            prefix="$prefix$dirname - "
            shift
            ;;
            
        -a | --artist)
            prefix="$prefix$2 - "
            shift
            shift
            ;;
        
        -al | --album)
            prefix="$prefix$2 - "
            shift
            shift
            ;;
    esac
done

printf "Prefix to be added:\n\t$prefix.\n Continue? (y/n)"
read choice

if [ $choice != "y" ]
then
    exit
fi

for file in "$1"/*
do
    if [ -f "$file" ]
    then
        mv \"$file\" \"$1/"$prefix$( basename "$file" )"\"
    fi
done



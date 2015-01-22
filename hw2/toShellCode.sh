#!/bin/sh

#Wrote by nia

if [ $# != 1 ]; then
    echo "Usage: $(basename $0) [asm file]"
    exit 1
fi

elf=$(mktemp)
nasm -f elf32 -o "$elf" "$1"
elfdump=$(mktemp)
objdump -d -M intel "$elf" > "$elfdump"
sed -nr -e 's/ *[0-9a-f]+:\t(([0-9a-f]{2} )+).*/\1/gp' "$elfdump" | tr -d '\n' | sed -r -e 's/ +//g' -e 's/../\\x&/g'


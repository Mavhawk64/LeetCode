#!/usr/bin/env sh

set -e

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <number> <file-extension>"
    exit 1
fi

NUM="$1"
EXT="$2"

DIR=$(printf "%04d" "$NUM")
FILE="${NUM}.${EXT}"

mkdir "$DIR"
cd "$DIR"
code "$FILE"

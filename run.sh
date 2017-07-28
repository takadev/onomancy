#!/bin/sh
echo $0
echo $1
echo $2
echo $#

if [ $# -ne 2 ]; then
	exit 1
fi

python create_name.py $1 $2

name_file=$2".txt"
target_file="boy.txt"
if [ $1 = "f" ]; then
	"${target_file}"="girl.txt"
fi

cp "${name_file}" "${target_file}"

python onomancy.py $1

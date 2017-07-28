#!/bin/sh

if [ $# -ne 2 ]; then
	exit 1
fi

name_file=$2".txt"
if [ -e  $name_file ]; then
	echo "$name_file already exists"
else
	python create_name.py $1 $2
fi

target_file="boy.txt"
if [ $1 = "f" ]; then
	target_file="girl.txt"
fi

cp "${name_file}" "${target_file}"

python onomancy.py $1

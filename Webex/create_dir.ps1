#! /bin/bash
read ndir
while [ -d "$ndir"]
do
cd $ndir
done
mkdir $ndir
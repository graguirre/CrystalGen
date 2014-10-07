#!/bin/sh

echo `wc -l $1` > $1.xyz
echo >> $1.xyz
cat $1 >> $1.xyz


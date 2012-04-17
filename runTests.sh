#!/bin/zsh
while true
do
    inotifywait *.py --event modify --quiet --quiet
    python pySpiderTest.py
done

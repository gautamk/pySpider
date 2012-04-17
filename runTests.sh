#!/bin/zsh
while true
do
    python pySpiderTest.py
    inotifywait *.py --event modify --quiet --quiet
done

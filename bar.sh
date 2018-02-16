#!/usr/bin/env bash

killall lemonbar 2>&1

background="#1E2127"
foreground="#ABB2BF"
underline="#1E2127"
./pyfreekbar.py | lemonbar -p -g 1366x25+0+0 -B "$background" -U "$underline" -F "$foreground" -u 4 -o 0 -f "FuraCode Nerd Font:style=Retina:pixelsize=11" -o -1 -f "Wuncon Siji:pixelsize=11" 2>&1 &

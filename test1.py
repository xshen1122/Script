# test1.py
# coding: utf-8
import os
cmd="adb shell /data/local/tmp/rvencApp /data/local/tmp/c0042_1280x720_25.yuv -i w=1280,h=720 -l 6 -v -p  -o /data/local/tmp/out.rv -a O,p=PBB -k i=125 -k q=5000 -r fps=25 -r kb=1500 -r rP=2"
s.system(cmd)
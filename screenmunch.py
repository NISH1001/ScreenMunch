#!/usr/bin/env python3

from gi.repository import Gdk
import subprocess
import os
import shutil


def exe(command):
    command = command.strip()
    c = command.split()
    p = subprocess.Popen(c,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE)
    output, error = p.communicate()
    output = output.decode('utf-8').strip()
    error = error.decode('utf-8').strip()
    return (output, error)

def cast(filename="screencast", resolution=(1366, 768)):
    default = Gdk.get_default_root_window()
    if not resolution:
        x, y, w, h = default.get_geometry()
        resolution = (w, h)
    try:
        exe("ffmpeg -f x11grab -r 25 -s {0}x{1} -i :0.0 -vcodec huffyuv {2}.avi".format(resolution[0], resolution[1], filename))
    except KeyboardInterrupt:
        print("--- compressing ---")
        exe("ffmpeg -i {0}.avi -vcodec libx264 temp.mp4".format(filename))
        os.remove("{}.avi".format(filename))
        os.rename("temp.mp4", "{}.mp4".format(filename))

def main():
    cast(filename="screencast", resolution="")

if __name__ == "__main__":
    main()


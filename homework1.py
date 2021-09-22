import os
import sys
import argparse
import time
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="input file")
parser.add_argument("-s", "--size", help="Output Size of files in MB", action="store_true")
parser.add_argument("-ls", help="List all files in a directory", action="store_true")
parser.add_argument("--rename", help="Change file name", default="")
parser.add_argument("-m", "--mtime", help="Print modification time", action="store_true")
args = parser.parse_args()
print("Args", args)
print("filename", args.file)
if args.ls:
    print("files in a directory:", ', '.join(os.listdir()))
if args.mtime:
    st = os.stat(args.file)
    print("last modified: %s" % time.ctime(st.st_mtime))
if args.size:
    stats = os.stat(args.file)
    print("file size in Megabytes", stats.st_size/1024)
if args.rename != "":
    os.rename(args.file, args.rename)

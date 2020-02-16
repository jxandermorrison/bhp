import sys
import socket
import getopt
import threading
import subprocess

listen              = False
command             = False
upload              = False
execute             = ""
target              = ""
upload_destination  = ""
port                = 0

def usage():
    print "BHP Net Tool"
    print
    print "Usage: netcatx.py -t target_host -p target_port"
    print
    print "-l --listen"
    print "listen on [host]:[port] for incoming connections"
    print
    print "-e --execute=file_to_run"
    print "execute the given file upon receiving connection"
    print
    print "-c --command"
    print "initialize a command shell"
    print
    print "-u --upload=destination"
    print "upon receiving a connection upload a file and write to"
    print "destination"
    print
    print
    print "Examples:"
    print "netcatx.py -t 192.168.0.1 -p 5555 -l -c"
    print "netcatx.py -t 192.168.0.1 -p 5555 -l -u=c:\\target.exe"
    print "netcatx.py -t 192.168.0.1 -p 5555 -l -e=\"cat /etc/passwd\""
    print "echo \"ABCEDEF\" | netcatx.py -t 192.168.0.1 -p 135 -l -"
    sys.exit(0)

def main():
    global listen
    global command
    global upload
    global execute
    global target
    global upload_destination
    global port

    if not(len(argv[1:])):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hle:t:p:cu:",
                ["help", "listen", "execute", "target", "port", "command",
                    "upload"])
    except getopt.GetoptError as err:
        print str(err)
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-l", "--listen"):
            listen = a
        elif o in ("-e", "--execute"):
            execute = a
        elif o in ("-c", "--command"):
            command = True

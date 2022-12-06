import time, sys
indent = 0
increaseIndent = True

try:
    while True:
        print(" " * indent, end="")
        #for quite some time, it did not work as planned because I did not put a blank space in the line before.
        print("********")
        time.sleep(0.1)
        if increaseIndent:
            indent = indent + 1
            if indent == 20:
                increaseIndent = False
            
        else:
            indent = indent -1
            if indent == 0:
                increaseIndent = True

except KeyboardInterrupt:
    sys.exit
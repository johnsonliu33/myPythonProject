# 'r'   open for reading (default)
# 'w'    open for writing, truncating the file first
# 'x'       create a new file and open it for writing
# 'a'       open for writing, appending to the end of the file if it exists
# 'b'       binary mode
# 't'       text mode (default)
# '+'       open a disk file for updating (reading and writing)+
#                  Must have exactly one of create/read/write/append mode and at most one plus

f = open("test.txt", "w")
f.write("tttttttttttttt")
f.close()

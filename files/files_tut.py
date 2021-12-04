# file objects

f = open('test.txt', 'r')

print(f.mode) # tells the mode the file is opened in

f.close()


# using a context manager (preferred method) -- best practice
# automatically closes file after the code block

with open('test.txt', 'r') as f:
    #f_contents = f.read()
    f_contents = f.readlines() # stores each line in a list (including newline)
    f_content = f.readline()   # grabs the next line of the file
    print(f_contents, end='')

    for line in f:              # reads each line with no memory issues
        print(line, end='')



with open('test2.txt', 'w') as f:
    f.write('Test')
    f.seek(0)
    f.write('R')                # Rest


with open('test.txt', 'r') as rf:
    with open('test_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)

# working with binary files
with open('bronx.jpg', 'rb') as rf:
    with open('bronx_copy.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


            
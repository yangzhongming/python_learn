
file_read = open('readme')
file_write = open('readmebak','w')

text = file_read.read()
file_write.write(text)

file_read.close()
file_write.close()



import glob; import io
path = '*.html'
files=glob.glob(path)
for filename in files:
    f = open(filename); text = ""; l = f.readline(); start = False
    while "</html>" not in l:
        if '</font>' in l: start = False
        if start: text += l.replace("<br>", "")
        if '</font></font><font size="3" face="Verdana, Arial, Helvetica, sans-serif"><br>' in l: start = True
        l = f.readline()
    f.close()
    with io.FileIO(filename + ".txt", "w") as newfile: newfile.write(text)
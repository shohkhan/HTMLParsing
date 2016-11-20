import glob
import io

from HTMLParserTreeS import HTMLParserTreeS

path = '*.html'
files=glob.glob(path)
for filename in files:
    parser = HTMLParserTreeS()
    f = open(filename, 'r')
    parser.feed(f.read())
    f.close()
    '''
    Change the following line to find data by tag and attributes.
    Attributes should be provided as an array of touples.
    '''
    data = parser.getdata("font", [('size', '3')])
    parser.close()

    if len(data) > 0:
        text = ""
        for d in data:
            text += d
        with io.FileIO(filename + ".txt", "w") as newfile: newfile.write(text)
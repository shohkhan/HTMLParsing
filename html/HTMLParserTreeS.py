from HTMLParser import HTMLParser
import collections

'''
This can be used to find a data (text) by HTML tag and attributes. Created using HTMLParser.
I wanted to create a complete tree, however, the more precise goal of finding a data (text) by HTML tag and attributes can be done using this code.
'''
class HTMLParserTreeS(HTMLParser):
    tree = collections.defaultdict(lambda: collections.defaultdict())
    index = 0
    currentPath = []
    def handle_starttag(self, tag, attrs):
        if tag != "br":
            self.index += 1
            if len(self.currentPath) == 0: par = -1
            else: par = self.currentPath[len(self.currentPath) - 1]

            self.tree[self.index]["id"] = self.index
            self.tree[self.index]["tag"] = tag
            self.tree[self.index]["parent"] = par #have to check if this is workig correctly
            self.tree[self.index]["data"] = ""
            self.tree[self.index]["attributes"] = attrs
            #self.tree[self.index]["children"] = [] #Future work

            self.currentPath.append(self.index)

    def handle_endtag(self, tag):
        self.currentPath.pop()

    def handle_data(self, data):
        if len(self.tree) > 0 : self.tree[self.currentPath[len(self.currentPath) - 1]]["data"] += data

    '''
    Get Data by tag and attributes. Attributes are not mandatory.
    '''
    def getdata(self, tag, attrs):
        datas = []
        for key, node in self.tree.items():
            if node["tag"] == tag:
                if len(attrs) > 0:
                    for a1, v1 in attrs:
                        for a2, v2 in node["attributes"]:
                            if a1 == a2 and v1 == v2:
                                if len(node["data"].strip()) > 0:
                                    datas.append(node["data"])
                else:
                    datas.append(node["data"])
        return datas
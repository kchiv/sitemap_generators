import os

def parse_input(_file, filetitle):

    output = """<?xml version="1.0" encoding="utf-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">"""
    for element in _file:
        output += "\n\t<url>\r"
        output += "\t\t%s" % element
        output += "\t\t<priority>1.0</priority>\r"
        output += "\t</url>"
    output += "\n</urlset>"
    updatedfiletitle = filetitle.replace(".txt", ".xml")
    file = open(updatedfiletitle, "w")
    file.write(output)
    file.close()
    print "success"


if __name__ == '__main__':
    for filename in os.listdir('"""Add path to files"""'):
        if filename.endswith(".txt"):
            with open(filename, "r") as url_file:
                parse_input(url_file, filename)

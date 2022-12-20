def gen_opf(title,name,author):
    import os
    opf=f'''<?xml version="1.0" encoding="utf-8" standalone="no"?>

<package version="2.0" xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
<dc:identifier id="bookid">666</dc:identifier>
<dc:title>{name}</dc:title>
<dc:creator opf:role="aut">{author}</dc:creator>
<dc:date>2022</dc:date>
<dc:language>zh-CN</dc:language>
</metadata>
<manifest>
<item id="ncxtoc" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
<item id="htmltoc"  href="book-toc.html" media-type="application/xhtml+xml"/>
<item id="css" href="style.css" media-type="text/css"/>\n'''
    for i in range(len(title)):
        opf+=f'<item id="chapter{i}" href="chapter{i}.html" media-type="application/xhtml+xml"/>\n'
    opf+='''</manifest>
<spine toc="ncxtoc">
<itemref idref="htmltoc" linear="yes"/>\n'''
    for i in range(len(title)):
        opf+=f'<itemref idref="chapter{i}" linear="yes"/>\n'
    opf+='''</spine>
<guide>
<reference href="book-toc.html" type="toc" title="Table Of Contents"/>
<reference href="chapter0.html" type="text" title="Beginning"/>
</guide>
</package>'''
    if os.path.exists('./temp')==False:
        os.mkdir('./temp')
    f=open('./temp/content.opf','w',encoding='utf-8')
    f.write(opf)
    f.close()

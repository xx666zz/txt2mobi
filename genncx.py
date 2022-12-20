def gen_ncx(title,name,author):
    import os
    ncx=f'''<?xml version="1.0" encoding="utf-8" standalone="no"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head>
<meta name="dtb:depth" content="1"/>
</head>

<docTitle>
<text>{name}</text>
</docTitle>
<docAuthor>
<text>{author}</text>
</docAuthor>

<navMap>\n'''
    for i in range(len(title)):
        ncx+=f'''<navPoint id="{i+1}" playOrder="{i+1}">
<navLabel><text>{title[i]}</text></navLabel>
<content src="chapter{i}.html"/>
</navPoint>\n
'''
    ncx+='''</navMap>
</ncx>'''
    if os.path.exists('./temp')==False:
        os.mkdir('./temp')
    f=open('./temp/toc.ncx','w',encoding='utf-8')
    f.write(ncx)
    f.close()

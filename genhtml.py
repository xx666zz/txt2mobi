def gen_toc(title):
    import os
    html='''<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta name="generator" content="EasyPub v1.50" />
<title>
Table Of Contents
</title>
<link rel="stylesheet" href="style.css" type="text/css"/>
</head>
<body>
<h2 class="titletoc">
目录
</h2>
<div class="toc">
<dl>\n'''
    for i in range(len(title)):
        html+=f'<dt class="tocl2"><a href="chapter{i}.html">{title[i]}</a></dt>\n'
    html+='''</dl>
</div>
</body>
</html>\n'''
    if os.path.exists('./temp')==False:
        os.mkdir('./temp')
    f=open('./temp/book-toc.html','w',encoding='utf-8')
    f.write(html)
    f.close()
def gen_chapter(title,content,ii):
    import os
    html=f'''<?xml version="1.0" encoding="utf-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="zh-CN">
<head>
<meta http-equiv="Content-Type" content="application/xhtml+xml; charset=utf-8" />
<meta name="generator" content="EasyPub v1.50" />
<title>
chapter {ii}
</title>
<link rel="stylesheet" href="style.css" type="text/css"/>
</head>
<body>
<h2 id="title" class="titlel2std">{title}</h2>'''
    for i in content:
        if i!='':
            html+=f'<p class="a">{i}</p>\n'
    html+='''</body>
</html>
'''
    if os.path.exists('./temp')==False:
        os.mkdir('./temp')
    f=open(f'./temp/chapter{ii}.html','w',encoding='utf-8')
    f.write(html)
    f.close()


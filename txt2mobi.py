import tools,os,subprocess,shutil,re
name=input(r"输入文件位置（如C:\1.txt）:")
nam=input('请输入小说名：')
print("读取中...")
author='unknown'
try:
    f=open(name,'r',encoding='utf-8')
    content=f.readlines()
except:
    f=open(name,'r',encoding='gbk')
    content=f.readlines()
f.close()
buf=""
buf1=[]
for line in content:
    buf+=line
    buf1.append(line)
title,content=tools.cut(buf,buf1)
for i in title:
    print(i)
while input('分成这样，是否手动输入正则表达式，输1不输入并进行生成，输2输入：')=='2':
    reg=input("请输入表达式:")
    title,content=tools.cut1(buf,reg,buf1)
    for i in title:
        print(i)
del buf,buf1
print('生成ncx、opf、css文件中...')
tools.gen_ncx(title,nam,author)
tools.gen_opf(title,nam,author)
tools.copy()
print('生成html中...')
tools.gen_toc(title)
for i in range(len(title)):
    tools.gen_chapter(title[i],content[i],i)
print('生成mobi中')
subprocess.run(r'kindlegen.exe .\temp\content.opf',shell=False,stdout=subprocess.PIPE,text=True,encoding='utf-8')
print('生成完成')
shutil.move(r".\\temp\\content.mobi", f".\\{nam}.mobi")
shutil.rmtree(r'.\\temp')
print('清理临时文件完成')

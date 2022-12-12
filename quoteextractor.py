import os

with open("quotes/365 Motivational Quotes for Success - The STRIVE.html", "r",encoding="utf8") as file:
    content =  file.read()

content = content.split("“")

del content[1], content[0]

txt = ""
for i in content:
    i = i.split('”')
    i = i[0]
    i = i.replace("<br>", "-----")
    txt = txt + i + "_***_\n"

with open("quotes.txt", "w", encoding="utf8") as file:
    file.write(txt)
    file.close()



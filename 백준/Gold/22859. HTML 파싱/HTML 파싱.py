import sys

html = sys.stdin.readline().strip()
html = html.replace("<main>", "").replace("</main>", "")
result = ""

for div in html.split("<div "):
    if not div:
        continue
    div = div.replace("</div>", "").split('"')
    if result != "":
        result += '\n'
    result += f'title : {div[1]}'
    for p in div[2].split("<p>"):
        if p == ">":
            continue
        result += f'\n'
        p = p.replace("</p>", "").strip()
        tag = False
        for pp in p:
            if pp == "<":
                tag = True
            elif pp == ">":
                tag = False
            elif not tag:
                if result[-1] == " " and pp == " ":
                    continue
                result += pp

print(result)
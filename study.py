file = "./explain_GUI.txt"
text = []
with open(file, 'r', encoding="UTF8")as f:
    line = f.readlines()
    for lines in line:
        text.append(lines)

print(text)
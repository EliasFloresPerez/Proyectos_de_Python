def count_char(texto,char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("nombre del archivo :")
with open(filename) as f:
    text = f.read()



for char in "aeiou":
    por = 100*count_char(text,char)/len(text)
    print(char,"-",round(por,2),"%")
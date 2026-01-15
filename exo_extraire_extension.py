def raw_ext_file(f):
    if "." in f:
        return f.split(".")[-1].lower()
    else :
        return ""

def descript_ext_file(f):
    if raw_ext_file(f) == "":
        return "No extension"
    for i in definition_extensions:
        if raw_ext_file(f) in i:
            return i[-1]
    else :
        return "Unknown extension"

def descript_ext(l):
    for f in l:
        print(f"{f} ({descript_ext_file(f)})")

files =("notepad.exe","my.file.doc","notes.TXT","holiday.JPEG","planning","data.dat")

definition_extensions=(("doc","Word Document"),
                       ("exe","Executable"),
                       ("txt","Texte File"),
                       ("jpeg","JPEG Image"))

descript_ext(files)
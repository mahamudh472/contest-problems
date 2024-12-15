inp = input()
r_s = "\ "[:1]
dic = {
    "a" : "/"+r_s,
    "b" : "|3",
    "c" : "(",
    "e" : "|{",
    "f" : "|=",
    "m" : "|\/|",
    "h" : "|-|",
    "u" : "|_|",
    "d" : "|)",
    "M" : "|\/|",
    "n" : "|\|",
    "s" : "$",
    "o" : "()",
    "g" : "(r",
    "i" : "|"
     
}
converted_name = ""

for i in inp:
    converted_name = converted_name + "".join(dic[i]) + " "  
        
print(converted_name)
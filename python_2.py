k='''Chan Tai Man,1,0,2,0,0,0
K,0,0,0,1,2,5
Chan Siu Ming,0,0,0,0,0,0'''

#k = open("demo.txt", "r").read()

result=""
rank = ["light demerit","minor demerit","major demerit","light merit","minor merit","major merit"]
for q in k.split("\n"):
    w=q.split(",")
    result+="\n"+w.pop(0)+": "
    n=sum(map(lambda x: int(x),w))
    if n:
        for i,e in enumerate(w):
            if int(e):
                if not n:
                    result+=", "
                result+=str(e)+" "+rank[int(i)]
                if int(e)>1:
                    result+="s"
                n=0
        result+="."
    else:
        result+=" NIL"
print(result)

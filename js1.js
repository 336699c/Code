k=`Chan Tai Man,1,0,2,0,0,0
Chan Siu Ming,0,0,0,0,0,0`


var result="";
const rank=["light demerit","minor demerit","major demerit","light merit","minor merit","major merit"];
k.split("\n").forEach(q=>{
    var n=0,w=q.split(",");w.map(w=>n+=(parseInt(w)?parseInt(w):0));
    result+="\n"+w.shift()+": ";
    if(n>0)w.forEach((q,i)=>{if(q>0){result+=(n<0?", ":"")+q+" "+rank[i]+(q>1?"s":"");n=-1}});
    result+=(n?".":"NIL");
});
console.log(result)

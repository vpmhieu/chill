var o = []
var s = "";
for(var i=0;i<o.length;i++){
  var j = o[i].search("(lengt)")
  s = s+ o[i].substring(0,j-2) + "'";
}
console.log(s);

document.cookie="bar-notdark=1;expires='';path=/";

window.Meebo||function(c){function p(){return["<",i,' onload="var d=',g,";d.getElementsByTagName('head')[0].",
j,"(d.",h,"('script')).",k,"='//cim.meebo.com/cim?iv=",a.v,"&",q,"=",c[q],c[l]?
"&"+l+"="+c[l]:"",c[e]?"&"+e+"="+c[e]:"","'\"></",i,">"].join("")}var f=window,
a=f.Meebo=f.Meebo||function(){(a._=a._||[]).push(arguments)},d=document,i="body",
m=d[i],r;if(!m){r=arguments.callee;return setTimeout(function(){r(c)},100)}a.$=
{0:+new Date};a.T=function(u){a.$[u]=new Date-a.$[0]};a.v=5;var j="appendChild",
h="createElement",k="src",l="lang",q="network",e="domain",n=d[h]("div"),v=n[j](d[h]("m")),
b=d[h]("iframe"),g="document",o,s=function(){a.T("load");a("load")};f.addEventListener?
f.addEventListener("load",s,false):f.attachEvent("onload",s);n.style.display="none";
m.insertBefore(n,m.firstChild).id="meebo";b.frameBorder="0";b.name=b.id="meebo-iframe";
b.allowTransparency="true";v[j](b);try{b.contentWindow[g].open()}catch(w){c[e]=
d[e];o="javascript:var d="+g+".open();d.domain='"+d.domain+"';";b[k]=o+"void(0);"}try{var t=
b.contentWindow[g];t.write(p());t.close()}catch(x){b[k]=o+'d.write("'+p().replace(/"/g,
'\\"')+'");d.close();'}a.T(1)}({network:"<>network<>"});

Meebo('addButton',{
id:"mb_<>id<>",
type:"widget",
icon:"http://meebojasonb.nfshost.com/<>icon<>",
label:"<>label<>",
width:<>px_w<>,
height:<>px_h<>,
		notResizable:true,
		noBorder:true,
onCreate:function(widget,element){
		
			var mb_<>id<>div=document.createElement('div');
			var mb_<>id<>img=document.createElement('img');
			
			mb_<>id<>img.src="http://meebojasonb.nfshost.com/<>image<>";	
			mb_<>id<>div.appendChild(mb_<>id<>img);
			element.appendChild(mb_<>id<>div);
		}	
});

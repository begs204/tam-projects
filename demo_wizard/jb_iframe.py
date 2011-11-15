def save_iframe(network,string):
	w_file = open('../'+network+'/index.html','w')
	w_file.write(string)
	w_file.close()
	print 'http://meebojasonb.nfshost.com/'+network

def iframe_web(network, url):
	string = """

	<html>
	<style>
		div {overflow:hidden; height:99.99%; width:99.99%}
		iframe {overflow:hidden; height:100%; width:100%}
	</style>
	<body>

	<script type="text/javascript">
	default_URL = "<>url<>";
	 URL = document.location.href;
	 mb_domain_tag = '?meebo_domain=';
	 mb_ad_tag = '/#meeboAd='
	 mb_src = "blah";

	
	if (URL.indexOf(mb_domain_tag) != -1){
		 sub_index = URL.indexOf(mb_domain_tag) + mb_domain_tag.length;
		if (URL.indexOf(mb_ad_tag) == -1){
			mb_src = URL.substring(sub_index);
		}
		else
		{
			mb_src = URL.substring(sub_index, URL.indexOf(mb_ad_tag));
		}
		
	}
	else
	{
		mb_src = default_URL;
	}
	if (mb_src.indexOf('http://') == -1)
	{
	mb_src = 'http://' + mb_src;
	}
	</script>

	
	<div>
	<iframe id ="mb_iframe" FRAMEBORDER="0" BORDER="0"> </iframe>
	<script  type="text/javascript" > document.getElementById('mb_iframe').src = mb_src</script>
	</div>
	<script type="text/javascript" src="http://meebojasonb.nfshost.com/<>network<>.js"></script>
	</body>
	</html>
	
	"""
	string2 = string.replace('<>url<>',url)
	string3 = string2.replace('<>network<>', network + '/' + network)
	
	save_iframe(network,string3)
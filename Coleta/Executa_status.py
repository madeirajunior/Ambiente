import os
from os import system
import sys
import commands
import subprocess
import time 
import getpass

print "Gravando em "+os.getcwd()
path=os.getcwd()

hostDmgr=raw_input("Host Dmgr:")
porta=raw_input("Porta:")
usuario = raw_input("Usuario: ")
senha= getpass.getpass("Senha:")

print "==================================="
print "=== Validando Servidores ONLINE ==="
print "==================================="
subprocess.check_call("wsadmin.bat -host "+hostDmgr+" -port "+porta+" -username "+usuario+" -password "+senha+" -lang jython -f "+path+"/TestaWebServers/ListaWebServerStatus.py")
print ""
print 50*"-"
print ""
subprocess.check_call("wsadmin.bat -host "+hostDmgr+" -port "+porta+" -username "+usuario+" -password "+senha+" -lang jython -f "+path+"/TestaWebServers/ListaAppServerStatus.py")
print ""
print 50*"-"
print ""

print "========================================="
print "=== GERANDO URLS para testes EMBEDDOR ==="
print "========================================="
subprocess.check_call("wsadmin.bat -host "+hostDmgr+" -port "+porta+" -username "+usuario+" -password "+senha+" -lang jython -f "+path+"/TestaWebServers/GeraURLsEmbeddorWebServers.py")
print ""
print 50*"-"
print ""
subprocess.check_call("wsadmin.bat -host "+hostDmgr+" -port "+porta+" -username "+usuario+" -password "+senha+" -lang jython -f "+path+"/TestaWebServers/GeraURLsEmbeddorAppServers.py")
print ""
print 50*"-"
print ""

print "==========================="
print "=== Validando EMBEDDORS ==="
print "==========================="
execfile(path+"/TestaWebServers/ValidaUrls.py")

print ""
print 50*"-"
print ""

print "=========================================="
print "=== GERANDO Arquitetura das aplicacoes ==="
print "=========================================="
subprocess.check_call("wsadmin.bat -host "+hostDmgr+" -port "+porta+" -username "+usuario+" -password "+senha+" -lang jython -f "+path+"/TestaWebServers/ListaArquiteturaNode.py")


arquivo = open(path+"/Htmls/index.html", "w")

arquivo.write("""
<html>
<head>
</head>
<script language="javascript" type="text/javascript">

  function resizeIframe(obj) {
    obj.style.height = obj.contentWindow.document.body.scrollHeight + 'px';
  }

function autoResize(id){
    var newheight;
    var newwidth;

    if(document.getElementById){
        newheight=document.getElementById(id).contentWindow.document .body.scrollHeight;
        newwidth=document.getElementById(id).contentWindow.document .body.scrollWidth;
    }

    document.getElementById(id).height= (newheight) + "px";
    document.getElementById(id).width= (newwidth) + "px";
}

</script>

<style>
table {
    border-collapse: collapse;
    font-family:"Verdana", Arial, Helvetica, sans-serif;
    font-size:"11px"    
}
</style>  


<head>
<body>
<h2><center>DMGr: """+hostDmgr+"""</center></h2>
<p>
<table border="0" align="center">
<tr>
<td valign="top">
<!-- IFRAME para Status dos Webservers -->
<iframe src="WebServerStatus.html" style="border: 1px black solid;" id="iframeWeb" align="center" frameborder="0" scrolling="no" onload="autoResize('iframeWeb')"></iframe>
&nbsp;&nbsp;
</td>

<td valign="top">
&nbsp;&nbsp;
<!-- IFRAME para Status dos AppServers -->
<iframe src="AppServerStatus.html" style="border: 1px black solid;" id="iframeApp" align="center" frameborder="0" scrolling="no" onload="autoResize('iframeApp')"></iframe>

</td>
</tr>
<tr>
</table>
<table border="0" align="center">
<td align="center">
<br><br>
<a href="EmbbedorWeb.html" target="iframe_a">
Teste (Embeddor dos WebServers)
</a>
&nbsp;&nbsp;
</td>
<td align="center">
<br><br>
&nbsp;&nbsp;
<a href="EmbbedorApps.html" target="iframe_a">
Teste (Embeddor dos AppServers)
</>
</td>
<td align="center">
<br><br>
&nbsp;&nbsp;
<a href="Arquitetura.html" target="iframe_a">
Arquitetura das Aplicacoes
</>
</td>
</tr>
<tr>
<td colspan="3">
<br>
<center><iframe src="Arquitetura.html" name="iframe_a" onload="autoResize('iframe_a')" frameborder="0" style="border: 1px black solid;"></iframe>

</center>
</td>
</tr>
</table>
</body>
</html>""")

arquivo.close()


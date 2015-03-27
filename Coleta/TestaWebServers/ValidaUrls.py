import os
import sys
import socket
import urllib2
import httplib
from urllib2 import Request, urlopen, URLError, HTTPError
path=os.getcwd()
cont=(1,2)
#req = urllib2.Request('http://www.python.org/fish.html')

for i in cont:
    URLs=""
    if i==1:
        arq = open("TestaWebServers/listaURLsApp.txt", 'r')
        URLs=arq.read()
        arq.close()
        URLs=(URLs).splitlines()
    if i==2:
        arq = open("TestaWebServers/listaURLsWeb.txt", 'r')
        URLs=arq.read()
        arq.close()
        URLs=(URLs).splitlines()

    timeout = 2
    socket.setdefaulttimeout(timeout)
    
    arquivo=""
    if i==1:
        arquivo = open(path+"/Htmls/EmbbedorApps.html", "w")
    if i==2:
        arquivo = open(path+"/Htmls/EmbbedorWeb.html", "w")
    arquivo.write("""<html>
    <head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <style>
    b{font-family:"Verdana", Arial, Helvetica, sans-serif;
    font-size:"11px"  }
    
    a{font-family:"Verdana", Arial, Helvetica, sans-serif;
    font-size:"11px"
    }
    
    u{
    color:"green"
    }
    </style>
    </head>
    <body>
    """)
    if i==1:
        arquivo.write("""<center><b><h3>Teste Embedder dos AppServers</h3></b><br>""")
    if i==2:
        arquivo.write("""<center><b><h3>Teste Embedder dos WebServers</h3></b><br>""")

    
    for url in URLs:
        passou="NAO"
        print url
        try:
    
            urllib2.urlopen(str(url))
            url2=str(url)
            request = urllib2.Request(url2)    
                    
            fd = urllib2.urlopen(request)
                    
            content = fd.read()
            fd.close()
            content=(content).splitlines()
            
            arquivo.write("<p><hr>")
            arquivo.write('<a target="_blank" href="'+url+'">'+url+'</a>')
            for i in content:
                if i.find("Running")!=-1 or i.find("RUNNING")!=-1:
                    passou="SIM"
                    arquivo.write("<b><br>")
                    i=str(i).replace("Running", "<u>RUNNING</u>")
                    i=str(i).replace("RUNNING", "<u>RUNNING</u>")
                    arquivo.write(str(i).replace("<p>", ""))
                    arquivo.write("</b>")
            if passou=="NAO":
                for i in content:
                    arquivo.write("<font color='red'><b>Retorno de Embeddor com Problemas</b></font>")
        except urllib2.HTTPError, e:
            arquivo.write("<p><hr>")
            arquivo.write('<a target="_blank" href="'+url+'">'+url+'</a>')
            arquivo.write("<br><b> <font color='red'>Http Status "+str(e.code)+"</font></b>")
        except urllib2.URLError, e:
            print "<!-- Endereco '"+url+"' nao acessivel -> Validar se o Webserver esta Ativo -->"
            arquivo.write("<!-- Endereco '"+url+"' nao acessivel -> Validar se o Server esta Ativo -->")
            continue
    arquivo.write("</body></html>")
    arquivo.close()
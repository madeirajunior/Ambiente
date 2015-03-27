import os
import sys, java
print " "
print "== Executando ListaWebServerstatus.py =="

lineSeparator = java.lang.System.getProperty('line.separator')
ls=lineSeparator 
path=os.getcwd()
arquivo = open(path+"/Htmls/WebServerStatus.html", "w")

def Palavra(list,delimitador,n=0,n1=1):
    return list.split(delimitador)[n:n1]

def isWebServerRunning(cell,nodename,servername):
    mbean = AdminControl.queryNames('WebSphere:type=WebServer,*')
    status=AdminControl.invoke(mbean,'status','[%s %s %s]' % (cell,nodename,servername),'[java.lang.String java.lang.String java.lang.String ]') 
    return status
#enddef

celula = AdminControl.getCell() 
ihsServer = AdminTask.listServers('[-serverType WEB_SERVER ]').split(lineSeparator) 


arquivo.write("""<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<style>
table {
    border-collapse: collapse;
    font-family:"Verdana", Arial, Helvetica, sans-serif;
    font-size:"11px"    
}

th {
        background-color: #D3D3D3;
        color: #125900;
        padding:3px 7px 2px 7px;

      }
td {
padding:3px 7px 2px 7px;
}
</style>
</head>
<body>
<center>
<b><h3>Status WebServers</h3></b>
<br>
<table border="1" bordercolor="black">
<tr>
<th>Web Server</th>
<th>Status</th>
</tr>
""")
for i in ihsServer:
        
        webName=Palavra(i, "(", n=0, n1=1)        
        webName=str(webName).replace("]", "");webName=webName.replace("[", "");webName=webName.replace("'", "")
        print " "
        print "Executando WebServer -> '"+webName+"'"
        webNode=Palavra(i, "/", n=3, n1=4)
        webNode=str(webNode).replace("]", "");webNode=webNode.replace("[", "");webNode=webNode.replace("'", "")
        
        if str(isWebServerRunning(celula,webNode,webName))=="RUNNING":
            arquivo.write("<tr>")
            arquivo.write("<td>")
            arquivo.write(webName)
            arquivo.write("</td>")
            arquivo.write("<td>")
            arquivo.write("<font color='green'><b>"+isWebServerRunning(celula,webNode,webName)+"</b></font>")
            arquivo.write("</td>")
            arquivo.write("</tr>")
        elif str(isWebServerRunning(celula,webNode,webName))=="STOPPED":
            arquivo.write("<tr>")
            arquivo.write("<td><b>")
            arquivo.write(webName)
            arquivo.write("</b></td>")
            arquivo.write("<td>")
            arquivo.write("<font color='red'><b>"+isWebServerRunning(celula,webNode,webName)+"</b></font>")
            arquivo.write("</td>")
            arquivo.write("</tr>")
        else:    
            arquivo.write("<tr>")
            arquivo.write("<td>")
            arquivo.write(webName)
            arquivo.write("</td>")
            arquivo.write("<td>")
            arquivo.write("<font color='orange'><b>"+isWebServerRunning(celula,webNode,webName)+"</b></font>")
            arquivo.write("</td>")            
arquivo.write("</table>")
arquivo.write("</center>")
arquivo.write("</body></html>")
print ""
print "== ListaWebServerstatus.py Executado=="
print ""
arquivo.close()
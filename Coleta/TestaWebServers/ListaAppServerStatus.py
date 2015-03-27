import sys, java
import os
print " "
print "== Executando ListaAppServerstatus.py =="

lineSeparator = java.lang.System.getProperty('line.separator')
ls=lineSeparator 
path=os.getcwd()
arquivo = open(path+"/Htmls/AppServerStatus.html", "w")

runningServer = AdminControl.queryNames("type=Server,*").splitlines()

def Palavra(list,delimitador,n=0,n1=1):
    return list.split(delimitador)[n:n1]

def isAppServerRunning(appSrvName,nodeName,):
    linha=""
    for servers in runningServer:
        #print servers
        appname=str(Palavra(str(servers), ",", n=0, n1=1));appname=appname.replace("['WebSphere:name=","");appname=appname.replace("']","")
        node=str(Palavra(str(servers), ",", n=3, n1=4));node=node.replace("['node=","");node=node.replace("']","")
        if appname==appSrvName and node==nodeName:
            #print servers
            status=AdminControl.getAttribute(servers, "state")
            return status

appServer=AdminTask.listServers('[-serverType APPLICATION_SERVER]').split(lineSeparator)

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
<b><h3>Status AppServers</h3></b>
<br>
<table border="1" bordercolor="black">

<tr>
<th><b>App Server Name</b></th>
<th><b>Node Name</b></th>
<th><b>Status</b></font></th>
</tr>
""")

for i in appServer:
    appSrvName=Palavra(i, "(", n=0, n1=1)
    appSrvName=str(appSrvName).replace("]", "");appSrvName=appSrvName.replace("[", "");appSrvName=appSrvName.replace("'", "")

    nodeName=Palavra(i, "/", n=3, n1=4)
    nodeName=str(nodeName).replace("]", "");nodeName=nodeName.replace("[", "");nodeName=nodeName.replace("'", "")
    print " "
    print "Executando App Server -> '"+appSrvName+"'"
    try:
        if str(isAppServerRunning(appSrvName, nodeName))=="STARTED":
            arquivo.write("<tr>")
            arquivo.write("<td>"+appSrvName+"</td>")
            arquivo.write("<td>"+nodeName+"</td>")
            arquivo.write("<td><font color='green'><b>"+str(isAppServerRunning(appSrvName, nodeName))+"</b></font></td>")
            arquivo.write("</tr>")
        else:
            arquivo.write("<tr>")
            arquivo.write("<td><b>"+appSrvName+"</b></td>")
            arquivo.write("<td><b>"+nodeName+"</b></td>")
            if str(isAppServerRunning(appSrvName, nodeName))=="None":
                arquivo.write("<td><b><font color='red'>STOPPED</font></b></td>")
                arquivo.write("</tr>")
            else:
                arquivo.write("<td><font color='orange'><b>"+str(isAppServerRunning(appSrvName, nodeName))+"</font></b></td>")
                arquivo.write("</tr>")
            
    except:
            arquivo.write("<tr>")
            arquivo.write("<td><b>"+appSrvName+"</b></td>")
            arquivo.write("<td><b>"+nodeName+"</b></td>")
            arquivo.write("<td><font color='red'><b>ERROR</b></font></td>")
            arquivo.write("</tr>")

arquivo.write("</table>") 
arquivo.write("</center>")
arquivo.write("</body></html>")

print ""
print "== ListaAppServerstatus.py Executado=="
print ""

arquivo.close()
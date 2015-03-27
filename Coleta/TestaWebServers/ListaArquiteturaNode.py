# ===========================================================================================
# === Script , Lista Arquitetura Aplicações
# === A saida está padronizada para importação em excel.
# ===
# ===  26/02/2015 - Script Inicial -  Odair Rodrigues Batista
# ===  17/03/2015 - Inclusao de ServerName - Odair Rodrigues Batista
# 
# === Antes de Executar o script, Valide o Separador de Sua maquina.
# 
#===========================================================================================
import os
import sys, java
path=os.getcwd()
arquivo = open(path+"/Htmls/Arquitetura.html", "w")

# declara o line.separator
ls = java.lang.System.getProperty("line.separator")

#padrao Portugues/Brasil
separador="</td><td>"
#padrao Ingles
#separador="," 

# Coleta de informações de celula e informações para o Cluster
cell = AdminConfig.list("Cell").split()
posicao_p = str(cell).find("(")
celula = cell[0][:posicao_p-2]
apServer= AdminTask.listServers("[-serverType APPLICATION_SERVER ]").split(ls)
cluster = AdminConfig.list("ServerCluster", AdminConfig.getid( "/Cell:"+celula+"/")).split(ls)

arquivo.write("""
<html>
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
<b><h3>Arquitetura das Aplicacoes</h3></b>
<br>
<table border="1" bordercolor="black">

<tr><th><b>Celula</b></th>
<th><b>Cluster</b></th>
<th><b>Node</b></th>
<th><b>Hostname</b></th>
<th><b>ApplicationServer Name</b></th>
<th><b>Applicacao</b></th>
<th><b>Versao Arquitetura</b></font></th></tr>
""")


# Funcao de tratamento para encontrar palavras em um elemento delimitado de uma lista
def Palavra(list,delimitador,n=0,n1=1):
    return list.split(delimitador)[n:n1]

ls = java.lang.System.getProperty("line.separator")
apServer= AdminTask.listServers("[-serverType APPLICATION_SERVER ]").split(ls)
apServer.sort()
nodeGeral=apServer[0]
nodeGeral=Palavra(str(nodeGeral), "/", n=3, n1=4)
nodeGeral=str(nodeGeral).replace("']","");nodeGeral=nodeGeral.replace("['","")



def LimpaRepetidos(lista):
# Remove informações repetidas de uma lista
    lista.sort()
    last = lista[-1]
    for i in range(len(lista)-2, -1, -1):
        if last==lista[i]:
            del lista[i]
        else:
            last=lista[i]
    return lista

# lista os appserver e os Nodes
def ListaAppSrvNameAndNodes():
    
    # Tratamento de nós para uma lista
    pNode=""
    listServers=""
    for listAppServer in apServer:
        pNode=Palavra(listAppServer,"/",n=3,n1=4)
        pCluster=Palavra(listAppServer,"(",n=0,n1=1)
        listServers=listServers+str(pCluster)+":"+str(pNode)

    listServers = listServers.replace("]", "")
    listServers = listServers.replace("[", "")
    listServers = listServers.replace("''", ",")
    listServers = listServers.replace("':'", ":")
    listServers = listServers.replace("'", "")
    listServers=listServers.split(",")
    listServers=filter(None, listServers)
    listServers.sort()
    return listServers


listaAppSrvNameAndNodes=LimpaRepetidos(ListaAppSrvNameAndNodes())



# Lista os Clusters
def ListaClusters(c):
    listac=""        
    # Tratamento para listagem de Clusters para uma lista a partir do "AdminConfig.list"
    for cc in c:
        formata = (cc.split("("))
        if listac<>"":
            listac = listac+","+str(formata[0])
        else:
            listac=str(formata[0])   
    listac =listac.replace('"','')            
    listac = listac.split(",")
    return listac

#Lista cluster e Applications Server
def ListaClustersAppsServer(cluster):
    a=""
    for listaCluster in ListaClusters(cluster):
        
                        
            # Coleta informações do Cluster
            clusterID=AdminConfig.getid("/ServerCluster:"+listaCluster+"/")
            clusterList=AdminConfig.list("ClusterMember", clusterID)
            clusterList=str(clusterList).split(')')
                        
            a=a+str(clusterList)
            
    a = a.replace("]", "")
    a = a.replace("[", "")
    a = a.replace("''", ",")
    a = a.replace("\\r\\n", ",")
    a = a.replace("'", "")
    a = a.replace('"', "")
    a = a.replace(" ", "")
    a=filter(None, a)
    a=a.split(",")
    a=filter(None, a)
    
    res3=""
    for bb in a:
        res=Palavra(bb,"(",n=0,n1=1)
        res=str(res).replace("']", "")
        res=res.replace("['", "")
        
        res2=Palavra(bb,"/",n=3,n1=4)
        res2=str(res2).replace("']", "")
        res2=res2.replace("['", "")
        res2=res2.split("|")[0]
        if res3=="":
            res3=res2+":"+res
        else:
            res3=res3+","+res2+":"+res
    
    res3=res3.split(',')
    return res3


def Servername(nameAppServer,nameNode):
    a=AdminTask.listServerPorts(nameAppServer, '[-nodeName '+nameNode+']').split(ls)[0]
    
    a=a.replace(' ]',']')
    a=a.replace('[ ','[')
    a=a.replace('[[SOAP_CONNECTOR_ADDRESS ','')
    a= a[2:-4]
    a=a.replace('] [',',')
    a=a.replace('[','')
    a=a.replace(']','')
    a=a.split(',')
    #a=tuple(a)
    a=a[0][5:]
    return a

# lista Cluster, nós e applications Servers
def listaClusterNodeAppsName(cluster):
    resultado=""
    for clusters in ListaClustersAppsServer(cluster):
        cluster=str(clusters)
        cluster=Palavra(cluster,":",n=0,n1=1)
        cluster=str(cluster)
        cluster=cluster.replace("['", "")
        cluster=cluster.replace("']", "")
        
        apps1=str(clusters)
        apps1=Palavra(apps1,":",n=1,n1=2)
        apps1=str(apps1)
        apps1=apps1.replace("['", "")
        apps1=apps1.replace("']", "")
        
        for nodes in listaAppSrvNameAndNodes:
            node=str(nodes)
            node=Palavra(node,":",n=1,n1=2)
            node=str(node)
            node=node.replace("['", "")
            node=node.replace("']", "")
            
            apps2=str(nodes)
            apps2=Palavra(apps2,":",n=0,n1=1)
            apps2=str(apps2)
            apps2=apps2.replace("['", "")
            apps2=apps2.replace("']", "")
            
            if apps1==apps2:
                if resultado=="":
                    resultado=cluster+":"+node+":"+apps1
                else:
                    resultado=resultado+","+cluster+":"+node+":"+apps1
    resultado=resultado.split(",")
    return resultado
resultado=""            

listaClusterNodeAppsNameUnique=listaClusterNodeAppsName(cluster)

# Remove informações repetidas de uma lista
listaClusterNodeAppsNameUnique.sort()
last = listaClusterNodeAppsNameUnique[-1]
for i in range(len(listaClusterNodeAppsNameUnique)-2, -1, -1):
    if last==listaClusterNodeAppsNameUnique[i]:
        del listaClusterNodeAppsNameUnique[i]
    else:
        last=listaClusterNodeAppsNameUnique[i]

#print listaClusterNodeAppsNameUnique
# iteração para tratamento e listagem de Bibliotecas Arq_Rigel
for lista in listaClusterNodeAppsNameUnique:
    cluster=str(lista)
    cluster=Palavra(cluster,":",n=0,n1=1)
    cluster=str(cluster)
    cluster=cluster.replace("['", "")
    cluster=cluster.replace("']", "")
    
    node=str(lista)
    node=Palavra(node,":",n=1,n1=2)
    node=str(node)
    node=node.replace("['", "")
    node=node.replace("']", "")
    if node==nodeGeral:
        apps=str(lista)
        apps=Palavra(apps,":",n=2,n1=3)
        apps=str(apps)
        apps=apps.replace("['", "")
        apps=apps.replace("']", "")
        applibs=AdminApp.list("WebSphere:cell="+celula+",node="+node+",server="+apps+"").splitlines()
    
        
        
        for applist in applibs:
            if applist<>"":
                libs = AdminApp.view(applist,"-MapSharedLibForMod") 
                lista2 = libs.split(ls)
                lista2=str(lista2)
                #encontra a posicao da palavra ARQ_RIGEL (biblioteca referente a Arquitetura)
                posicao_ARQ_RIGEL = str(lista2).find("ARQ_RIGEL")
                # varre as posições a partir da posição encontrada  na variavel "posicao_ARQ_RIGEL"
                palavra=""
                for i in range(len(str(lista2))):
                    if i >= posicao_ARQ_RIGEL:
                        palavra=palavra+lista2[i]
                    if -1 == posicao_ARQ_RIGEL:
                        palavra=" "
                    # Encontra a posicao da proxima virgula, (separador)
                    posicao_Virgula=str(palavra).find(",")
                    # varre as posições até a posição encontrada  na variavel "posicao_Virgula"
                    palavra_final=""
                    for p in range(len(palavra)):
                        if -1 == posicao_Virgula:
                            palavra_final="Nao possui Versao de Arquitetura"
                        elif p < posicao_Virgula:
                            palavra_final=palavra_final+palavra[p]
                                    # Imprime valores, no formato para CSV
                serverName=Servername(apps, node)
                print "Gravando informaçao de Arquitetura do ensamblado -> "+applist
                arquivo.write("<tr><td>"+celula+separador+cluster+separador+serverName+separador+node+separador+apps+separador+applist+separador+palavra_final+"</td></tr>")
arquivo.write("</table>")
arquivo.write("</body></html>")

arquivo.close()
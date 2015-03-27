# ===========================================================================================
# === Script , GeraURLsWebservers
# === funcao: O Script lista todos os links para os WebServers.
# ===
# ===  23/03/2015 - Script Inicial -  Odair Rodrigues Batista
# 
# === 
# 
#===========================================================================================

import sys, java

print " "
print "== Executando GeraURLsEmbeddorWebServers.py =="

arq = open("TestaWebServers/listaURLsWeb.txt", "w")

# declara o line.separator
lineSeparator = java.lang.System.getProperty('line.separator')
ls=lineSeparator 


# Coleta de informações de celula e informações para o Cluster
cell = AdminConfig.list("Cell").split()
posicao_p = str(cell).find("(")
celula = cell[0][:posicao_p-2]
apServer= AdminTask.listServers("[-serverType APPLICATION_SERVER ]").split(ls)
cluster = AdminConfig.list("ServerCluster", AdminConfig.getid( "/Cell:"+celula+"/")).split(ls)



  
# Funcao de tratamento para encontrar palavras em um elemento delimitado de uma lista
def Palavra(list,delimitador,n=0,n1=1):
    return list.split(delimitador)[n:n1]

def ListaWebservers():
    lista=""
    ihsServer = AdminTask.listServers('[-serverType WEB_SERVER ]').splitlines()
    for i in ihsServer:
        celula=str(Palavra(i, "(", n=0, n1=1))
        celula=celula.replace("['", "");celula=celula.replace("']", "")
        
    
        node=str(Palavra(i, "/", n=3, n1=4))
        node=node.replace("['", "");node=node.replace("']", "")
        
        
        hsPorts=AdminTask.listServerPorts(celula, '[-nodeName '+node+']')
        hsPorts=hsPorts.splitlines()
        hsPorts= str(hsPorts[0])
        
    
        webServername=str(Palavra(hsPorts, "[", n=7, n1=8))
        webServername=webServername.replace("[", "");webServername=webServername.replace("]", "");webServername=webServername.replace("'", "");webServername=webServername.replace("server", "");webServername=webServername.replace(" ", "")
        
        
        host=str(Palavra(hsPorts, "[", n=5, n1=6))
        host=host.replace("[", "");host=host.replace("]", "");host=host.replace("'", "");host=host.replace("host", "");host=host.replace(" ", "")
        if lista=="":
            lista=host
        else:
            lista=lista+","+host
    return lista
    
def ListaNodes():
    
    # Tratamento de nós para uma lista
    pNode=""
    listServers=""
    for listAppServer in apServer:
        pNode=Palavra(listAppServer,"/",n=3,n1=4)
        if pNode=="":
            listServers=str(pNode)
        else:
            listServers+=","+str(pNode)

    listServers = listServers.replace("]", "")
    listServers = listServers.replace("[", "")
    listServers = listServers.replace("''", ",")
    listServers = listServers.replace("':'", ":")
    listServers = listServers.replace("'", "")
    listServers=listServers.split(",")
    listServers=filter(None, listServers)
    listServers.sort()
    return listServers
nodeP=ListaNodes()[0]

# lista os appserver e os Nodes
def ListaAppSrvNameAndNodes():
    
    # Tratamento de nós para uma lista
    pNode=""
    listServers=""
    for listAppServer in apServer:
        pNode=Palavra(listAppServer,"/",n=3,n1=4)
        pAppServer=Palavra(listAppServer,"(",n=0,n1=1)
        listServers=listServers+str(pAppServer)+":"+str(pNode)

    listServers = listServers.replace("]", "")
    listServers = listServers.replace("[", "")
    listServers = listServers.replace("''", ",")
    listServers = listServers.replace("':'", ":")
    listServers = listServers.replace("'", "")
    listServers=listServers.split(",")
    listServers=filter(None, listServers)
    listServers.sort()
    return listServers

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
        
        for nodes in ListaAppSrvNameAndNodes():
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
def ListaApps(listaClusterNodeAppsNameUnique):
    appsT=""
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
        
        apps=str(lista)
        apps=Palavra(apps,":",n=2,n1=3)
        apps=str(apps)
        apps=apps.replace("['", "")
        apps=apps.replace("']", "")
        if node==nodeP:
            applibs=AdminApp.list("WebSphere:cell="+celula+",node="+node+",server="+apps+"").splitlines()
            for apps in applibs:
                if appsT=="":
                    appsT=apps
                else:
                    appsT=appsT+","+apps
                   
    return appsT.split(',')



listaApps=ListaApps(listaClusterNodeAppsNameUnique)

listaApps.sort()
last = listaApps[-1]
for i in range(len(listaApps)-2, -1, -1):
    if last==listaApps[i]:
        del listaApps[i]
    else:
        last=listaApps[i]


listaWebservers=ListaWebservers().split(",") 
for webServers in listaWebservers:
    print " "
    print "Listando URLS para teste no servidor '"+webServers+"'"
    for apps in listaApps:
        url1="http://"+webServers+"/"+apps+"/Embeddor"
        url2="https://"+webServers+"/"+apps+"/Embeddor"            
        
        # Gravando em arquivo
        arq.write(url1)
        arq.write("\n")
        arq.write(url2)
        arq.write("\n")
        
arq.close()

print ""
print "== GeraURLsEmbeddorWebServers.py Executado =="
print ""
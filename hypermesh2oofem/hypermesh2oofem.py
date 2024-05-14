hypermeshFile = "TPBPlaneStress3D.inp"
f = open(hypermeshFile)   
outFile=open("in.txt","w")        
line = f.readline()

outFile.write("################ NODE ################\n")
#########################################Read node#########################################
while line:
    line = f.readline()
    if (line.find("*NODE")):
        pass
    else:
        node = f.readline()
        a = node.split(",")
        outFile.write("node "+a[0]+" coords 3 "+a[1]+a[2]+a[3])
        while node:
            node = f.readline()
            if ("**HWCOLOR" in node): break
            a = node.split(",")
            outFile.write("node "+a[0]+" coords 3 "+a[1]+a[2]+a[3])

f.close()
outFile.write("################ ELEMENT ################\n")
#########################################Read elem#########################################
f = open(hypermeshFile)   
line = f.readline()  
while line:
    line = f.readline()
    if (line.find("*ELEM")):
        pass
    else:
        elem = f.readline()
        a = elem.split(",")
        outFile.write("lspace"+a[0]+"  nodes  8 "+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+"\n")
        while elem:
            elem = f.readline()
            if ("*NSET" in elem): break
            a = elem.split(",")
            outFile.write("lspace"+a[0]+"  nodes  8 "+a[1]+a[2]+a[3]+a[4]+a[5]+a[6]+a[7]+"\n")


f.close()
# outFile.write("################ NSET ################")
# #########################################Read nset#########################################
# f = open(hypermeshFile)  
# nset = f.readline()
# while nset:
#     nset = f.readline()
#     if ("*NSET," in nset):
#         nset = f.readline()
#         outFile.write("\nSet "+" nodes  8 "+nset[:-2].replace(","," "))
#         while (("*NSET," not in nset)):
#             nset = f.readline()
#             if ("*NSET," in nset): break
#             if ("**,"  in nset): break
#             outFile.write(nset[:-2].replace(","," "))


# f.close()
outFile.close()
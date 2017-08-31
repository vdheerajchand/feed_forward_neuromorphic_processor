#################################
# This is a Python script created to verify the results of the Processor "Viplava"
# Edit the Below variables to get the expected results.
# Thanks for using "Viplava" a neuromorphic processor

##################################


##### change these values to get the desired output########
input_data=[1,1,0,1]
weights_1=[[-1,0,1,1],[0,1,-1,-1],[-1,-1,0,1],[0,1,-1,1]]
weights_2=[[-1,1,0,1],[0,1,-1,-1],[-1,-1,0,1],[1,1,-1,0]]

############################################################

print"input values are " ,input_data

h2=[]
h3=[]
h4=[]
h1=[]
o1=[]
o2=[]
o3=[]
o4=[]
for i in range (4):
    
    h1.append((input_data[i])*(weights_1[i][0]))
#print" result",h1
for i in range (4):
    
    h2.append((input_data[i])*(weights_1[i][1]))
#print" result",h2

for i in range (4):
    
    h3.append((input_data[i])*(weights_1[i][2]))
#print" result",h3

for i in range (4):
    
    h4.append((input_data[i])*(weights_1[i][3]))
#print" result",h4

h1_i=sum(h1)
h2_i=sum(h2)
h3_i=sum(h3)
h4_i=sum(h4)

if(h1_i>=0):
    h1_i=1
else:
    h1_i=0

if(h2_i>=0):
    h2_i=1
else:
    h2_i=0
    
if(h3_i>=0):
    h3_i=1
else:
    h3_i=0

if(h4_i>=0):
    h4_i=1
else:
    h4_i=0

print"hidden network values are ",h1_i,h2_i,h3_i,h4_i


hidden_ip=[h1_i,h2_i,h3_i,h4_i]
#hidden_ip.append(h1_i,h2_i,h3_i,h4_i)
#hidden_ip.extend((h1_i,h2_i,h3_i,h4_i))

#print hidden_ip
for i in range (4):
    
    o1.append((hidden_ip[i])*(weights_2[i][0]))
#print" result",o1
for i in range (4):
    
    o2.append((hidden_ip[i])*(weights_2[i][1]))
#print" result",o2

for i in range (4):
    
    o3.append((hidden_ip[i])*(weights_2[i][2]))
#print " result",o3


for i in range (4):
    
    o4.append((hidden_ip[i])*(weights_2[i][3]))
#print" result",o4

y1_i=sum(o1)
y2_i=sum(o2)
y3_i=sum(o3)
y4_i=sum(o4)

if(y1_i>=0):
    y1=1
else:
    y1=0

if(y2_i>=0):
    y2=1
else:
    y2=0
    
if(y3_i>=0):
    y3=1
else:
    y3=0

if(y4_i>=0):
    y4=1
else:
    y4=0
print "final output by the neural network is ",y1,y2,y3,y4

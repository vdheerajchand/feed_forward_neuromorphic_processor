###############################################################################
#Module: Viplava -- A neuromorphic processor
#file name: Project_viplava.py
#date: 6/1/2016
#Authors: Dheeraj chand Vummidi, venkata SaiMohan kammila
#code Type: Python
#description: This file can simulate the Assembly code implementing 4-Input neuron network

###############################################################################

##**********************   Initializations *******************#################
global clock_count    # global clock
import sys
sys.setrecursionlimit(100000)
import linecache
import binascii
import binhex
clk_counter=0
trace=open("trace.txt",'w')
global clock
dummy_mem_out=[]                ## Opcode initialization
opcode_val={
    '001':"LOAD",
    '010':"STORE",
    '011':"NADD",
    '100':"NMUL",
    '101':"NOOP",
    '111':"HALT",

}
#### Register file initialisation
reg_list=[]
temp_dest_reg=[]
temp_dest_reg_add=[]
temp_source_reg_1=[]
temp_source_reg_2=[]
value_array=[]
int_value_array=[]
hidden_layer_value=[]
### register Encoding
registers= {
'0000000': "R0",
'0000001': "R1",
'0000010': "R2",
'0000011': "R3",
'0000100': "R4",
'0000101': "R5",
'0000110': "R6",
'0000111': "R7",
'0001000': "R8",
'0001001': "R9",
'0001010': "R10",
'0001011': "R11",
'0001100': "R12",
'0001101': "R13",
'0001110': "R14",
'0001111': "R15",
'0010000': "R16",
'0010001': "R17",
'0010010': "R18",
'0010011': "R19",
'0010100': "R20",
'0010101': "R21",
'0010110': "R22",
'0010111': "R23",
'0011000': "R24",
'0011001': "R25",
'0011010': "R26",
'0011011': "R27",
'0011100': "R28",
'0011101': "R29",
'0011110': "R30",
'0011111': "R31",
'0100000': "R32",
}
###### function for write back stage
def inst_write_back():
    if(opcode=="100"):
        reg_list[int_dest_reg]=temp_dest_reg
    if(opcode=="011"):
        reg_list[int_dest_reg]=temp_dest_reg_ex
        trace.write("clock cycles taken is "+str(clock_count)+"\n")
    if(opcode =="101"):
        trace.write("clock cycles taken is "+str(clock_count)+"\n")
########function for Memory stage
def inst_mem(int_dest_reg):
    global temp_dest_reg_ex
    temp_dest_reg_ex=int_dest_reg
    if(opcode=="100" or opcode== "011"):

        inst_write_back()
    if(opcode=="001"):
        reg_list[int_dest_reg] = linecache.getline("Memory_in.txt", (int_immidiate_value/4)+1)
        reg_list[int_dest_reg]="{0:04b}".format(int(reg_list[int_dest_reg],16)).zfill(32)
        #print " data is loaded in the memory stage" + "  " + "  " + reg_list[int_dest_reg]
        #print int_dest_reg
        #print "R1 reg value is ", reg_list[1]
        #print "r2 reg is ", reg_list[2]
        trace.write("moving to write back!"+"\n")
        inst_write_back()
    if(opcode=="010"):
        trace.write("simlating store"+"\n")
        f=open("Memory_out.txt",'r')
        dummy_mem_out=f.readlines()
        #print"memory copy is", dummy_mem_out
        f.close()
        #print "int dest is ",int_dest_reg
        #print"actual result is ",reg_list[int_dest_reg]
        tline =reg_list[int_dest_reg]
        a_hex = hex(int(tline[0:4], 2))[2:]
        b_hex = hex(int(tline[4:8], 2))[2:]
        c_hex = hex(int(tline[8:12], 2))[2:]
        d_hex = hex(int(tline[12:16], 2))[2:]
        e_hex = hex(int(tline[16:20], 2))[2:]
        f_hex = hex(int(tline[20:24], 2))[2:]
        g_hex = hex(int(tline[24:28], 2))[2:]
        h_hex = hex(int((tline[28:32]), 2))[2:]
        final = a_hex + b_hex + c_hex + d_hex + e_hex + f_hex + g_hex + h_hex
        #print "value should be stored is ",final#hex(int(reg_list[int_dest_reg],2))[2:]
        dummy_mem_out[int_immidiate_value-1]=final+"\n"#hex(int(reg_list[int_dest_reg],2))[2:]+"\n"
       # print "modified memory copy is ",dummy_mem_out
        f=open("Memory_out.txt",'w')               ##### creating output memory image
        for i in range(len(dummy_mem_out)):
            f.write(dummy_mem_out[i])
        trace.write("store is done"+"\n")
        inst_write_back()





#####Function for execution stage

def inst_execution(int_dest_reg):
    global opcode_int
    global source_reg_1_value
    global registers
    #clock_count=clock_count+1
    global int_source_reg_1
    global source_reg_2_value
    global int_source_reg_1
    global int_source_reg_2
    global source_reg_1
    global source_reg_2
    if(opcode== "001"):
        trace.write("Moving to Memory stage"+"\n")
        inst_mem(int_dest_reg)
    if (opcode == "010"):
        trace.write("Moving to Memory stage"+"\n")
        inst_mem(int_dest_reg)


###### function for execution stage
def inst_ex_function():
    #temp_dest_reg_ex
    #clock_count=clock_count+1
    ############################################### This piece of code splits the value given in the instruction to perfrom multiplication############
    if(opcode=="100"):
        source_reg_1_value = reg_list[int_source_reg_1]#"{0:04b}".format(int(reg_list[int_source_reg_1],16)).zfill(32)
        #print"source 1 is in mul stage ",source_reg_1_value
        #print "source 1 is ", source_reg_1_value
        for i in range(0, 32):
            temp_source_reg_1[i]=source_reg_1_value[i]
        #print("splitted source 1 reg value", temp_source_reg_1)
        source_reg_2_value = reg_list[int_source_reg_2]#"{0:04b}".format(int(reg_list[int_source_reg_2],16)).zfill(32)
        for i in range(0, 32):
            temp_source_reg_2[i]=source_reg_2_value[i]
        #print("splitted source 2 reg value", temp_source_reg_2)

        if(int(temp_source_reg_1[0])==0 and int(temp_source_reg_1[1])==1):
            temp_dest_reg[0:8]=temp_source_reg_2[0:8]
        elif(int(temp_source_reg_1[0])==0 and int(temp_source_reg_1[1])==0):
            temp_dest_reg[0:8]='0','0','0','0','0','0','0','0'
        else:
            trace.write("input 1 error"+"\n")

        if (int(temp_source_reg_1[2]) == 0 and int(temp_source_reg_1[3]) == 1):
            temp_dest_reg[8:16] = temp_source_reg_2[8:16]
        elif (int(temp_source_reg_1[2]) == 0 and int(temp_source_reg_1[3]) == 0):
            temp_dest_reg[8:16] = '0', '0', '0', '0', '0', '0', '0','0'
        else:
            trace.write("input 2 error"+"\n")
        if (int(temp_source_reg_1[4]) == 0 and int(temp_source_reg_1[5]) == 1):
            temp_dest_reg[16:24] = temp_source_reg_2[16:24]
        elif (int(temp_source_reg_1[4]) == 0 and int(temp_source_reg_1[5]) == 0):
            temp_dest_reg[16:24] = '0', '0', '0', '0', '0', '0', '0', '0'
        else:
            trace.write("input 3 error"+"\n")
        if (int(temp_source_reg_1[6]) == 0 and int(temp_source_reg_1[7]) == 1):
            temp_dest_reg[24:32] = temp_source_reg_2[24:32]
        elif (int(temp_source_reg_1[6]) == 0 and int(temp_source_reg_1[7]) == 0):
            temp_dest_reg[24:32] = '0', '0', '0', '0', '0', '0', '0', '0'
        else:
            trace.write("input 4 error"+"\n")
        #print "NMul Result is ",temp_dest_reg
        inst_mem(1)
        reg_list[int_dest_reg]=temp_dest_reg
    elif(opcode=="011"):

        #print "source 1 reg value in add stage",int_source_reg_1
        source_reg_1_value = reg_list[int_source_reg_1]
        #print "source 1 is ", source_reg_1_value
        for i in range(0, 32):
            temp_source_reg_1[i]=source_reg_1_value[i]

        #print("splitted source 1 reg value", temp_source_reg_1)
        trace.write("Doing addition now"+"\n")
        j=0
        value_array=0
        value_array=temp_source_reg_1
        #print "here"
       #print "value array is",value_array
###############converting the inputs to the custom encoding format#########
        for i in range(0, 32):
            value_array[i] = value_array[j:j + 2]
            j=j+2
        #print value_array[1]
        #print value_array
        for i in range(0,32):
            if value_array[i] == ['0', '1']:
                int_value_array[i] = 1
                #print"array 1"
            elif(value_array[i] == ['0', '0']):
                int_value_array[i] = 0
                #print"array 0"
            elif(value_array[i] == ['1', '1']):
                int_value_array[i] = -1
                #print"array -1"
            #else:
             #   print "check value array"


        #print "entire ints are ", int_value_array
########################Doing  the Addition##################################33
        h1_add = int_value_array[0] + int_value_array[4] + int_value_array[8] + int_value_array[12]
        h2_add = int_value_array[1] + int_value_array[5] + int_value_array[9] + int_value_array[13]
        h3_add = int_value_array[2] + int_value_array[6] + int_value_array[10] + int_value_array[14]
        h4_add = int_value_array[3] + int_value_array[7] + int_value_array[11] + int_value_array[15]
        #print"added result at h1 is ", h1_add
        #print"added result at h2 is ", h2_add
        #print"added result at h3 is ", h3_add
        #print"added result at h4 is ", h4_add
        ####################### doing the comparision on the added values###############
        if h1_add >= 0:
            h1 = 1
        else:
            h1 = 0
        if h2_add >= 0:
            h2 = 1
        else:
            h2 = 0
        if h3_add >= 0:
            h3 = 1
        else:
            h3 = 0
        if h4_add >= 0:
            h4 = 1
        else:
            h4 = 0
        if h1==0:
            hidden_layer_value[0]="0"
            hidden_layer_value[1]="0"
        else:
            hidden_layer_value[0]="0"
            hidden_layer_value[1]="1"
        if h2 == 0:
            hidden_layer_value[2] = "0"
            hidden_layer_value[3] = "0"
        else:
            hidden_layer_value[2] = "0"
            hidden_layer_value[3] = "1"
        if h3 == 0:
            hidden_layer_value[4] = "0"
            hidden_layer_value[5] = "0"
        else:
            hidden_layer_value[4] = "0"
            hidden_layer_value[5] = "1"
        if h4 == 0:
            hidden_layer_value[6] = "0"
            hidden_layer_value[7] = "0"
        else:
            hidden_layer_value[6] = "0"
            hidden_layer_value[7] = "1"
        hidden_layer_value_final=''.join(map(str,hidden_layer_value))
        temp_dest_reg_ex=4*hidden_layer_value_final
        #print "temp is ",temp_dest_reg_ex
        reg_list[int_dest_reg]=temp_dest_reg_ex
        #print "register is"+reg_list[int_dest_reg]
        inst_mem(temp_dest_reg_ex)
        trace.write( "final correctly formatted hidden layer value is "+str(hidden_layer_value_final)+"\n")
        trace.write("final H1 is "+str(h1)+"\n")
        trace.write("final H2 is "+str(h2)+"\n")
        trace.write("final H3 is "+str(h3)+"\n")
        trace.write("final H4 is "+str(h4)+"\n")

####################### instruction fetch function #########################################3
clock=0

current_PC=0
def inst_fetch(code_file):
    global current_PC
    global next_PC
    global clock_count
    global clock
    global opcode
  #  global j
    opcode=0
    clock=1
    f = open(code_file, "rb")
    if clock==True:
        current_inst1=linecache.getline(code_file,((current_PC)/4+1))
        current_inst=bin(int(current_inst1,16))[2:]
        f.close()
        if current_PC==0:
            #for i in range(0, 32):
               # temp_dest_reg.append(0)
                #temp_source_reg_1.append(0)
                #temp_source_reg_2.append(0)
            for i in range(0,32):
                value_array.append(0)
                int_value_array.append(0)
                temp_source_reg_1.append(0)
                temp_source_reg_2.append(0)
            for i in range(0,8):
                hidden_layer_value.append(2)
            for i in range(0,128):
                reg_list.append(0)
            #trace=open("trace.txt",'w')
            trace.write("Processor started !!"+"\n")
            temp_dest_reg_ex=0
            int_dest_reg=0
            source_reg_1_value = 0
            source_reg_2_value = 0
            int_source_reg_1 = 0
            int_source_reg_2 = 0
            int_dest_reg=0
            clock_count=0
        trace.write("Current address(PC_value) is"+str(current_PC)+"\n")
        #print "Current instruction is  ",current_inst
        clock_count=clock_count+1
        current_inst_bin = "{0:04b}".format(int(current_inst, 2)).zfill(32)
        opcode = current_inst_bin[0:3]
        if opcode== ("111"):
            trace.write("clock cycles taken is " + str (clock_count+1) +"\n")
        else:
            trace.write("clock cycles taken is " + str(clock_count) +"\n")

        #current_PC=current_PC+1
        current_inst_bin="{0:04b}".format(int(current_inst,2)).zfill(32)
        opcode=current_inst_bin[0:3]
        #print" instruction in Binary format is",current_inst_bin
        if opcode ==("111"):
            print "####################################################" + "\n"
            print"Halt encountered, check trace file for the details "   +"\n"
            print "####################################################"
            trace.write("Halt encountered"+"\n")


            return 1
        else:
            inst_decode(current_inst_bin)
            ########3 incrementing the PC value
            current_PC = current_PC +4
            inst_fetch("Assembly_code.txt")
    elif clock== False:
        trace.write("clock zero"+"\n")


######## instruction decode stage##########################
def inst_decode(instruction):
    #clock_count=clock_count+1
    global opcode_int
    global int_source_reg_1
    global registers
    global int_source_reg_2
    global target_register
    global destination_register_value
    global destination_register_value
    global int_immidiate_value
    global source_reg_1
    global source_reg_2
    global int_dest_reg
    opcode=instruction[0:3]
    trace.write("OPCODE is"+str(opcode)+"\n")

    if opcode =="001" or opcode=="010":
        trace.write("Memory access detected"+"\n")
        dest_reg=instruction[3:10]
        trace.write("destination Reg is "+str(dest_reg)+"\n")
        int_dest_reg=int(dest_reg,2)
        #print int_dest_reg
        immidiate_value=instruction[10:33]
        int_immidiate_value=int(immidiate_value,2)
        trace.write("Given Instruction is "+str(opcode_val[opcode]) + "  "+ str(registers[dest_reg])+"  "+str(int_immidiate_value)+"\n")
        #print"trasnfer to execution load stage"
        inst_execution(int_dest_reg)
        #print source_reg_1,dest_reg,source_reg_2,unused_bit
    elif( opcode=="100" or opcode=="110"):
        dest_reg = instruction[3:10]
        int_dest_reg=int(dest_reg,2)
        source_reg_1 = instruction[10:17]
        int_source_reg_1=int(source_reg_1,2)
        #print "int source 1 value is ",int_source_reg_1
        source_reg_2 = instruction[17:24]
        int_source_reg_2 = int(source_reg_2, 2)
        unused_bit = instruction[24:33]
        trace.write("R type instruction"+"\n")
        trace.write(opcode_val[opcode]+"  "+str(registers[dest_reg])+"  "+str(registers[source_reg_1])+"  "+str(registers[source_reg_2])+"\n")
        inst_ex_function()
    elif(opcode=="011"):
        dest_reg = instruction[3:10]
        int_dest_reg = int(dest_reg, 2)
        source_reg_1 = instruction[10:17]
        int_source_reg_1 = int(source_reg_1, 2)
        unused_bit = instruction[17:32]
        trace.write("R type ADD instruction"+"\n")
        trace.write(opcode_val[opcode] + "  " +str( registers[dest_reg] )+ "  " + str(registers[source_reg_1])+"\n")
        inst_ex_function()
    elif(opcode=="000"):
        trace.write("opcode is invalid "+str(opcode)+"\n")
    elif opcode == ("101"):
        trace.write("NO OP detected"+"\n")
        inst_execution(0)
    else:
        trace.write("HALT detected"+"\n")

inst_fetch("Assembly_code.txt")   ### calling fetch stage



























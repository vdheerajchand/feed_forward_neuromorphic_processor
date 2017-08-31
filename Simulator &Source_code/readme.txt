##########
READ ME 
##########

Hello, welcome to the Project 'Viplava'


 In order to setup and run 'viplava' you need to follow the below steps

1. First find the file "Viplava_neuromorphic.py".This is the main simulator based on python programming.
2. Make sure you can see "Assembly_code.txt" and "Memory_in.txt" in the same directory.
    these two files are processor assembly code and input memory image respectively. Our simulator takes the assembly code,inputs and weights from these files.
    Create a new text file with file name "Memory_out.txt" and open that file, Hold "Enter" key for 25 seconds. This will create few empty lines in the text file,
    these will be used as "Memory rows" for the simulation.
3. Open and run the python file "Viplava_neuromorphic.py"
4. wait until program displays "Halt encountered, check trace file" message in the transcript.
5. This simulator creates a trace file called "trace.txt" after completing the execution. This will have all the information related to the 'Execution'
6. "Cross_check_script.py" can be used to cross check the output of the processor. Just open this file and make changes to the pre defned inputs and weights.
7. Run the "Cross_check_script.py"  to see the expected output for the given inputs and weight combination.

	
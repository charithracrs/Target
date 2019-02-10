# Target
Target is a python module with allows the user to get information about how long it is until the next bus on “BUS ROUTE” leaving from “BUS STOP NAME” going “DIRECTION” using the api defined at http://svc.metrotransit.org/


# Prerequisites
Linux VM with python2.7 or python2.6
or
Python IDLE - 3.7 on Windows


# Execution Steps

## For PYTHON2.7/PYTHON2.6 - LinuxVM
  1. Download the file target_final.py
  2. Run the file with the following example command ( $python target_final.py {Route} {Stop} {Direction} ). 
  ##### Example : $python target_final.py 'METRO Blue Line' 'Target Field Station Platform 1' 'south'
  3. Result is the Time Duration or Time of the next available bus on route from the mentioned station. 
  ##### Example output :5:44 (or) 8mins
    
## For PYTHON3.7 - Windows
 1. Download the file target.py
 2. Open the file with Python3.7 IDLE interactive shell, run the file using "F5".
 3. This will prompt the inputs for arguments as given in the below example.
##### Route = METRO Blue Line
##### Stop = Target Field Station Platform 1
##### Direction = south
 4. Result is the Time Duration or Time of the next available bus on route from the mentioned station. 
##### 6:41
 5. Invalid input and output
##### $python main.py 'METRO ' 'Target Field Station Platform 1' 'south'
##### Route invalid or Direction invalid or Stop invalid or No available bus


# UDT and Alarm List #
## Pre-requisite ##
PLCnext Engineer 2025.0.2 

Simulator for AXC F 2152 FW 2023.0.0 

## Description ##
This project contains three columns where all alarms are displayed - three columns: time (String), Status (String) and Description (String).
![image002](https://github.com/user-attachments/assets/2cd3420e-a350-4b8b-83a0-d23cd5987654)

The entry boxes help to create alarms manually, and those will be registered once "Create Entry" button is pressed. As per below:
![image007](https://github.com/user-attachments/assets/cd25b544-5381-47c2-bf37-67e20dba63b8)

![image008](https://github.com/user-attachments/assets/c991420c-d101-46cc-9627-bac2afdffab3)

Alarms are registered in a array of struct with 255 size.
![image009](https://github.com/user-attachments/assets/576e712c-1197-4bcf-85c8-21fcbf395fc8)

In HMI > a Symbol is created with the next specs:
![image010](https://github.com/user-attachments/assets/1aba1879-59b2-4fe2-a79b-76bf2936d3bb)

And using Symbol List >> you can create and display the list of alarms (you can enable the scroll bar to display all elements in Alarm array).
![image011](https://github.com/user-attachments/assets/e5cbcf09-f95e-4ba2-bd73-59553d856c32)

![image012](https://github.com/user-attachments/assets/d73b68f7-30ca-48c6-bcda-2e73bd579e73)


## Running the project ##
To run this project, please Open PLCnext Engineer >> Create new Project >> Search the AXC F 2152 and select the FW on the device >> Drag and drop the controller under Project (panel on the left hand side)
![image013](https://github.com/user-attachments/assets/a4079250-66b4-470c-934a-1335df13bbc8)

Once the controller is attached to the project, Click on File >> Import >> Import from Another Project >> Search for the project
<img width="390" alt="image014" src="https://github.com/user-attachments/assets/c425c858-b83b-4126-9ddf-11a29217c6ec" />

Make sure all components are selected >> Click on Ok
![image015](https://github.com/user-attachments/assets/27a307c7-254a-4c72-ace5-937f81540b0e)

Set main page as Startup >> Right click on HMI Web Server >> Application >> main >> Set as startup.

![unnamed](https://github.com/user-attachments/assets/068c7e89-9fec-4db7-bc34-11366bf1b9d4)

Create a task called 'maintask' under PLCnext
![image017](https://github.com/user-attachments/assets/3a74eedb-016d-4a19-9f7b-58dd1c911545)

Create HMI tags for executeWin and RTC:
![image019](https://github.com/user-attachments/assets/b3211879-3f37-4f4f-bec1-efde85731ee0)

Double click on IEC 61131-3 >> Data List >> Right click on popWindow variable, add HMI tag. Do the same for RTC variable

<img width="333" alt="image018" src="https://github.com/user-attachments/assets/5d662369-ebf8-4431-9a88-59c224cc8939" />

Once created, the name might not be same as project, change name under HMI Web Server, and click on the HMI tag to change name:
![unnamed (1)](https://github.com/user-attachments/assets/7aa9ba8b-fcfc-41d6-ad6b-cdbe3600a266)

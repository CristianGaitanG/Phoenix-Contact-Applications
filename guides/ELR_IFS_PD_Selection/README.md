# 🧰 Process Data Selection tool #
This is a tool developed in Python, to help selecting the number of motor starters (ELR IFS) connected to a gateway accordingly to the process data selected.
---
## 🛠️ Instructions ##
This app was created to help customers in the design process about how many motor starters can be used with a single gateway according to the process data. 

The App folder contains four files:
- 2x Images related to the app
- 1x Excel spreadsheet which contains all IFS hybrid motor starters and Gateways (this is used to select the correct PN according to customer’s application)
- 1x PxC_Motor_App.py (this file is the Python app).

This application is divided in two parts: Part number selection (specify the comm protocol and the type of hybrid motor starter – number of functions and current), and the second part is dedicated to the process data available per motor starter.

![image003](https://github.com/user-attachments/assets/d00f9e62-305d-434f-9066-f24825c09b31)

To use the app the customer needs to enter the mandatory information in both sides of the screen (current, functions, comm protocol, and process data).
Steps to execute the app:
1. Choose the communication protocol
2. Specify the function for the hybrid motor starter.
3. Specify motor current – hybrid motor starter current.
4. Press “Find” button – It will give you the PNs that meet the criteria.
5. Process data – Choose one of the two mandatory data (one for control and one for status).
6. Process data – Chose any optional process data
7. Press “Verify” button – It will give you the number of hybrid motor starters that can be connected to the gateway, validating the max. number of devices per gateway (32), the max. number of process data per motor starter (16), and the max. number of process data per gateway (64).
 

![test1](https://github.com/user-attachments/assets/6fcfec86-dcf1-490b-9d42-1a38e929490b)



This application only works with IFS motor starters, and it does not include IO-Link motor starters.

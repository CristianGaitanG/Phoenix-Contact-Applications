# Retain Data Usage!

## Description
This application allows to save and load the retaining data specified in the FB ‘PBCL_ParamBackup’.
This FB is contained in the library PLCnext Base available in PLCnext Store - PLCnext Store | PLCnextBase

## Application Structure
The app is divided in three parts:
1. Library initialisation - This function block is used to set up the service environment on the target device as a system component. If the service was not started yet or has an incompatible version it is required to restart the system.
2. Check if folder exists – if it does not, the app will create the folder automatically and then create the file. If it does, the app will only create the file where data is stored. This file is xml format.
3. Saving and loading FB – the FB for management needs to be activated, and then save or load the data.

<img width="389" height="457" alt="image001" src="https://github.com/user-attachments/assets/cfd936e1-3624-466c-b381-4743d1baefd1" />

## Pre-requisites:

* PLCnext Engineer 2025.0.2
* PLCnext Base Library 1.6.4.2
* AXC F 2152 FW 2023.0

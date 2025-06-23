# HMI Templates #

## Pre-Requisites to run the example: ##
PLCnext Engineer 2025.0.2
Simulator for AXC F 2152 FW 2023.0.0
To run this project, please Open PLCnext Engineer >> Create new Project >> Search the AXC F 2152 and select the FW on the device >> Drag and drop the controller under Project (panel on the left hand side).

Once the controller is attached to the project, Click on File >> Import >> Import from Another Project >> Search for the project >> Make sure all components are selected >> Click on Ok

 
## Working with HMI Templates ##

There are two ways to create templates and to add actions to the buttons for navigating between pages.
### Option A: ###

You can create an HMI template, and add an 'Action on Click' - Action Navigate Home, or Navigate Left, or Navigate Right.
![image001](https://github.com/user-attachments/assets/0f6be8bd-0f32-42a1-9634-48374e639b46)
![image002](https://github.com/user-attachments/assets/3f9c4405-142f-4a28-8f1e-8ace6581ab02)

And using the Navigation tool for HMI, set the way to 'Navigate' between pages. To access this tool, please double click on HMI Web Server >> Application.

Then select Navigation Tab, and drag and drop the pages as per the actions configured before.

In this example,

- when click on the button with Home icon, it will go to home page.

- when click on the button with Right arrow icon, it will go to the page configured on the right side of the home page - in this case Page2

<img width="337" alt="image007" src="https://github.com/user-attachments/assets/48bbe9b6-aab1-4f27-b4e7-258ada821381" />

 
### Option B: ###
You can design an HMI page (with buttons and actions), and create a template from it >> You can rename it and save the project.
<img width="697" alt="image008" src="https://github.com/user-attachments/assets/60fa1092-ac1d-4a88-9b89-956c1438a938" />


Do not change the Dynamic actions for the new template. Create a new HMI page and change the Background page template and select the created one.

![image009](https://github.com/user-attachments/assets/1c6d6fb7-d456-47a2-b06b-fb7219732a6f)


 If you would like to add more buttons in the template, navigating between the pages are not available. This option requires to have the Page design with the button and actions before creating the template.

 
## 2. Dialog window when clicking on Symbol ##
I have created a Symbol with four different elements: Text, Line, Button, and Ellipse.
If a dialog window needs to be opened when clicking on the Symbol, you can do the next:

### Using button ###
- Add a Parameter with Page type
- In HMI symbol, add Action on click function >> Open Dialog >> Select the parameter created (in this case page)
![image010](https://github.com/user-attachments/assets/c9359697-ce83-4537-b597-55636d6651ea)
 
- Assign the Dialog window for the Page parameter in the Symbol from where it is used >> popUpWindow will be executed when clicking on Test button
![image011](https://github.com/user-attachments/assets/b6bbf1e8-a0ab-4bf5-bb53-fe7cb0c8daff)

### Using any element in Symbol ###
If you want to open the window when clicking any other element in the Symbol, please select the Symbol and add Action on Click >> Open Dialog >> Select the page.
![image012](https://github.com/user-attachments/assets/8b445623-21e9-42ec-914a-dc1f14a34ecf)


## Results: ##
### Template Option A ###
![image013](https://github.com/user-attachments/assets/537d801e-11d4-41c6-b4c7-2df3fd4731fd)

### Template Option B ###
![image014](https://github.com/user-attachments/assets/af8d45b2-0918-4d4a-bb6f-5051ef7cd75d)

### Open Dialog when clicking symbol ###
![image015](https://github.com/user-attachments/assets/0da09062-9dff-497b-a6cc-77d42d3920c9)

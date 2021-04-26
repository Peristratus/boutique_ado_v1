## Medistart Hospital Web app
![Project Image](/static/images/botique.png)

--------

### Table of Content

-  [Description](#description)
 - [User-stories](#user-stories)
 - [User-Acceptance-Testing](#User-Acceptance-Testing)
 - [Technologies](#technologies)
 - [Deployment](#Deployment)
 - [References](#References)
 - [Licenses](#licenses)
 - [Author](#author)

------------------------
 ## Description

 This Final milestone project is part of my on going Full Stack Software Developer course at Canadian Business college in collaboration with the Code Instititute.
 The website/ Web app is based on a fictional E-commerce site called Boutique Ado , the app's theme is based on an online store and their services to the general public.The user(s) will be able to 
 interact with the web app, navigate through the site, register as a user and have a user profile page. Buy products and items as a registered or non registered user, the information will be submitted into django database. 
 The user will also be able to interact with an Artificial Intelligent chat bot that speaks to the user(s), assist the user in navigating through the web app using voice commmands, suggest items to buy, inform the user 
 about sale offers. The AI is able to have a meaningful conversation with the user and interact in small talk not related to the shopping experience . The site is fully functional with Stripe payment API and Webhooks 
 incorporated with the Stripe payment system. The Web app is a fully integrated front-end and backend django web app. 
 
 Disclaimer: The use of brand names and images are purely for educational purposes and will not be used for a real e-commerce web app at this dispensation .
 
----------------------------
 ## User-stories

 ### Requirement Gathering
 
 The table below will breifly describe the user stories for the functional and non-functional requirements, the user stories decribed in
 **Table 1.0 Requirement Traceability Catalog** will be Independent, Negotiable, Valuable, Estimable, Smart and Testable, **INVEST** in nature and composition.

 *Table 1.0 Requirement Traceability Catalog*

HLR   |  HLR Ref# |    HLR Description    |                              User Stories                                                    |                                                      Acceptance criteria                                                                                        |                                MoSCoW                                                                                                                |
------|---------- |-----------------------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------| 
Botique Ado  | H-1.0 | Gain access to botique Ado website   | **As a** user **I want** to access the web page  **so that** I can gain access to the site content.| **Given** that the user is on the Boutique home page, **When** they click on the Nav links Home **then** the system will take the user to the home section of the web page. |     M   |
All Product drop down menu | APM-2.0| Gain access to botique Ado website  | **As a** user **I want** to access the all product nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the All product nav link **then** the system will display a drop down menu |    M   |
By Price | BP-2.1| Gain access to botique Ado website | **As a** user **I want** to access by price nav link  **so that** I can have access to the by price page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu by price nav link **then** the system will take the user to the by price web page |    M   |
By Rating | BR-2.2| Gain access to botique Ado website | **As a** user **I want** to access by Rating nav link  **so that** I can have access to the by Rating page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu by Rating nav link **then** the system will take the user to the by Rating web page |    M   |
By Category | BC-2.3| Gain access to botique Ado website | **As a** user **I want** to access by Category nav link  **so that** I can have access to the by Category page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu by Category nav link **then** the system will take the user to the by Category web page |    M   |
All Products | AP-2.4| Gain access to botique Ado website | **As a** user **I want** to access all product  nav link  **so that** I can have access to the all product page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu all product nav link **then** the system will take the user to the all product  web page |    M   |
Clothing drop down menu | CLM-3.0| Gain access to botique Ado website  | **As a** user **I want** to access the Clothing nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the Clothing nav link **then** the system will display a drop down menu |    M   |
Active & Essential wear | AE-3.1| Gain access to botique Ado website | **As a** user **I want** to access Active & Essential nav link  **so that** I can have access to the Active & Essential wear page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Active & Essential wear nav link **then** the system will take the user to the Active & Essential wear web page |    M   |
Jeans | JEN-3.2| Gain access to botique Ado website | **As a** user **I want** to the Jeans nav link  **so that** I can have access to the Jeans page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Jeans nav link **then** the system will take the user to the Jeans wear web page |    M   |
Shirt | SH-3.3| Gain access to botique Ado website | **As a** user **I want** to access the Shirt nav link  **so that** I can have access to the Shirt page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Shirt nav link **then** the system will take the user to the Shirt web page |    M   |
All Clothing | AC-3.4| Gain access to botique Ado website | **As a** user **I want** to access all Clothing nav link  **so that** I can have access to the all clothing page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu all clothing nav link **then** the system will take the user to the all clothing  web page |    M   |
Homeware drop down menu | HWM-4.0| Gain access to botique Ado website  | **As a** user **I want** to access the Homeware nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the Homeware nav link **then** the system will display a drop down menu |    M   |
Bed & Baths | BB-4.1| Gain access to botique Ado website | **As a** user **I want** to access Bed & Bath nav link  **so that** I can have access to the Bed & Bath page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Bed & Bath nav link **then** the system will take the user to the Bed & Bath web page |    M   |
Kitchen & Dining | KD-4.2| Gain access to botique Ado website | **As a** user **I want** to the Kitchen & Dining nav link  **so that** I can have access to the Kitchen & Dining page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu the Kitchen & Dining nav link **then** the system will take the user to the Kitchen & Dining web page |    M   |
All Homeware | HW-4.3| Gain access to botique Ado website | **As a** user **I want** to access all Homeware nav link  **so that** I can have access to the all Homeware page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu all Homeware nav link **then** the system will take the user to the all Homeware  web page |    M   |
Special Offer drop down menu | SOM-5.0| Gain access to botique Ado website  | **As a** user **I want** to access the All Specials nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the All special nav link **then** the system will display a drop down menu |    M   |
New Arrivals | NA-5.1| Gain access to botique Ado website | **As a** user **I want** to access to the New Arrivals nav link  **so that** I can have access to the New Arrivals page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu New Arrivals nav link **then** the system will take the user to the New Arrivals web page |    M   |
Deals | JEN-5.2| Gain access to botique Ado website | **As a** user **I want** to the Jeans nav link  **so that** I can have access to the Jeans page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Jeans nav link **then** the system will take the user to the Jeans wear web page |    M   |
Clearance | CLR-5.3| Gain access to botique Ado website | **As a** user **I want** to access the Clearance nav link  **so that** I can have access to the Clearance page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Clearance nav link **then** the system will take the user to the Clearance web page |    M   |
All Specials | AC-5.4| Gain access to botique Ado website | **As a** user **I want** to access all Specials nav link  **so that** I can have access to the all special page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu all specials nav link **then** the system will take the user to the all special web page |    M   |
Shop Now Btn | SNB-6.0| Gain access to botique Ado website | **As a** user **I want** to access the Shop now BTN  **so that** I can have access to the all Product page.| **Given**  that the user is on botique Ado home page, **When** they click on the shop now BTN  **then** the system will take the user to the all Product web page |    M   |
New arrival pop-up | NAP-7.1| Gain access to botique Ado website | **As a** user **I want** to access the pop-up new arrival widget  **so that** I can have access to the all products web page.| **Given**  that the user is on botique Ado home page, **When** they click on the pop up widget **then** the system will take the user to the all product web page |    M   |
Search engine | SE-8.1| Gain access to botique Ado website | **As a** user **I want** to access the search input box  **so that** I can search for products and item.| **Given**  that the user is on botique Ado home page, **When** they input an item or product in the search input box **then** the system will search for the item / product and display it to the user or display 0 products to the user  |    M   |
My Account drop down meu | MAM-9.0| Gain access to botique Ado website  | **As a** user **I want** to access the My Account nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the My Account nav link **then** the system will display a drop down menu |    M   |
Login | LOG-9.1| Gain access to botique Ado website | **As a** user **I want** to access the Login nav link  **so that** I can have access to the Login page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Login nav link **then** the system will take the user to the Login web page |    M   |
Register | REG-9.2| Gain access to botique Ado website | **As a** user **I want** to access the Register nav link  **so that** I can have access to the Register page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Register nav link **then** the system will take the user to the Register web page |    M   |
Add to Bag btn | ATB-10.0| Gain access to botique Ado website | **As a** user **I want** to access the Add to Bag Btn  **so that** I can buy the item.| **Given**  that the user is on botique Ado home page, **When** they click on the add to bag Btn **then** the system will display a toast message with the item and the go to secured check-out btn |    M   |
Secured to Check-out Btn | STC-10.1| Gain access to botique Ado website | **As a** user **I want** to access the secured to check-out Btn  **so that** I can proceed to the check-out.| **Given**  that the user is on botique Ado home page, **When** they click on the go to secured check-out Btn **then** the system will display the secured check out page |    M   |
Secured Check-out Btn  | SC-10.2| Gain access to botique Ado website | **As a** user **I want** to access the Check out form  **so that** I can fill in my details and credit card information.| **Given**  that the user is on botique Ado home page, **When** they click on the secured check-out Btn **then** the system will display the Check-out form |    M   |
Complete order Btn | CO-10.3| Gain access to botique Ado website | **As a** user **I want** to access the Complete order Btn  **so that** I can purchase my item or product.| **Given**  that the user is on botique Ado home page, **When** they click on the complete to order Btn **then** the system will accept the order through STRIPE api payment platform or decline my purchase |    M   |
Alan AI Btn | AI-11.0| Gain access to botique Ado website | **As a** user **I want** to access Alan AI Btn  **so that** I can talk, ask question about sales, suggestions on what to buy, be able to have a converstaion and navigate the site through voice command.| **Given**  that the user is on botique Ado home page, **When** they click on the Alan AI Btn **then** Alan AI will be able to have a meaningful conversation with the user and obey their commands or decline to obey their commands. |    M   |




## User-Acceptance-Testing

The UAT will define the criteria by which the website is considered to be "working",high, medium or low defects will be identified and cataloged for further improvements or regression testing.
The UAT critreria and results will confirm if the website can handle required task in a real-world scenarios, according to the Requirements Traceability Catalog Table 1.0.

*Table 2.0 User Acceptance Testing (UAT)*


 Test#    | User stories Ref# |        Description of task        |               Steps to evaluate    |                        Expected Result                                                                                                                                                                                                                               |            Pass / Fail / Comments                               |  
--------  |-------------------|-----------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------| 
APT-H-1.0  | H-1.0               | Home nav link                  | APT-H-1.0.0:   Click home nav link | The link should be funtional and take the user to the home page section displaying the page and information .                                                                                                                                                          |                     Pass                                      |
APT-GS-1.1  | GS-1.1             | Get started btn                | APT-GA-1.1.0:  Click Get Started Btn| The btn should be funtional and take the user to the login/register page.                                                                                                                                                                                            |                     Pass                                      | 
APT-CU-1.2  | CU-1.2             |Contact us btn                  | APT-CU-1.2.0:  Click Contact us Btn| The btn should be funtional and take the user to the contact us page.                                                                                                                                                                                                 |                     Pass                                      | 
APT-RM-1.3  | RM-1.3             |Read More btn                   | APT-RM-1.3.0:  Click Read more  Btn| The btn should be funtional and take the user to the Blog section.                                                                                                                                                                                                    |                     Pass                                      | 
APT-PB-1.4  | PB-1.4             |Play Btn                        | APT-bbt-1.4.0: Click Play Btn |The button should be functional and allow the user to a view the Medstar promotional Video.                                                                                                                                                                                |                     Pass                                      |                                                                                     
APT-CF-1.5   | CF-1.5            |contact floating btn            | APT-PP-1.5.0: Click Contact floating btn| The button should be functional and once it is clicked, it should pop-up a phone, whatsapp and chat icon when the chat icon is clicked it should take the user to the a AI chat page                                                                            |                     Pass                                      |
APT-AI-1.5.1  | AI-1.5            |AI Chat btn                    | APT-PP-1.5.1.1: Click chat btn| The button should be functional and once it is clicked, it should pop-up a phone, whatsapp and chat icon when the chat icon.                                                                                                                                              |                     Pass                                      |
APT-AI-1.5.2  | AI-1.5            |AI Activate btn                    | APT-PP-1.5.1.2: Click Activate btn| The button should be functional and once it is clicked, the user should be able to speak with the AI,have a meaningful discussion between bot and Human, AI should be able to book appointments and asisst during emergencies for registed users.                 |                     Pass as functional able to make meaningful conversation , but cannot book appointments or asisst during  emergencies, phase two devlopment should introduce these features.|
APT-SM-1.6  | SM-1.6           | social media btn                 | APT-PP-1.6.0: Click on the social media icon | The icon should be functional and once it is clicked , the user should be able to have a meaningful conversation, book appointments and asisst users during emergencies.                                                                                    |                     Pass                                      |                                                                        
APT-S-2.0 | S-2.0               | services nav Link               | APT-S-2.0.0:  Click the service nav link | The link should be funtional and take the user to the service page section displaying the page and information.                                                                                                                                                 |                     Pass                                      |
APT-SH-2.1  | SH-2.1            | service hover effect            | APT-SH-2.1.0: Hover over the service nav link  | When the user is on the service page and they hover over the Service nav link a drop down menu of services is displayed for the user to select.                                                                                                          |                     Pass                                      |                                                                
APT-GS-2.2  | GS-2.2            | Get started btn                 | APT-GS-2.2.0: Click Get Started Btn| The btn should be funtional and take the user to the login/register page.                                                                                                                                                                                            |                     Pass                                      |
APT-CF-2.3  |CF-2.3            | Contact Floating btn             | APT-CF-2.3.0: Click Contact floating btn| The button should be functional and once it is clicked, it should pop-up a phone, whatsapp and chat icon when the chat icon is clicked it should take the user to the a AI chat page                                                                             |                     Pass                                      |
APT-SM-2.4  | SM-2.4            | Social media icon               | APT-SM-2.4.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                    |                     Pass                                      |
APT-DP-3.0  | DP-3.0            | Department nav link             | APT-RB-3.0.0: Click Department nav link | The link should be funtional and take the user to the department page section displaying the page and information.                                                                                                                                              |                     Pass                                      |
APT-CU-3.1  | CU-3.1          | Contact us btn                    | APT-CU-3.1.0: Click Contact us Btn| The btn should be funtional and take the user to the contact us page.                                                                                                                                                                                                 |                     Pass                                      |
APT-SM-3.2 | SM-3.2         | Social media icon                   | APT-SM-3.2.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                   |                     Pass                                      |
APT-RM-3.3 | RM-3.3         | Read more btn                       | APT-RM-3.3.0: Click Read more  Btn| The btn should be funtional and take the user to the Blog section.                                                                                                                                                                                                    |                     Pass                                      |
APT-AU-4.0 | AU-4.0         | About us                            | APT-AU-4.0.0: Click about us nav link | The link should be funtional and take the user to the about us  page section displaying the page and information .                                                                                                                                                |                     Pass                                      |
APT-GS-4.1  | GS-4.1        | Get started btn                     | APT-GA-4.1.0: Click Get Started Btn| The btn should be funtional and take the user to the login/register page.                                                                                                                                                                                            |                     Pass                                      | 
APT-RM-4.2  | RM-4.2        |Read More btn                        | APT-RM-4.2.0: Click Read more  Btn| The btn should be funtional and take the user to the Blog section.                                                                                                                                                                                                    |                     Pass                                      | 
APT-PB-4.3  | PB-4.3        |Play Btn                             | APT-PB-4.3.0: Click Play Btn |The button should be functional and allow the user to a view the Medstar promotional Video.                                                                                                                                                                                 |                     Pass                                      |   
APT-SM-4.4  | SM-4.4         | Social media icon                  | APT-SM-4.4.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                   |                     Pass                                      | 
APT-BL-5.0  | BL-5.0         | Blog                               | APT-BL-5.0.0: Click Blog nav link | The link should be funtional and take the user to the blog page section displaying the page and information .                                                                                                                                                        |                     Pass                                      |
APT-SM-5.1  | SM-5.1         | Social media icon                  | APT-SM-5.1.0: Click on the social media icon | The icon should be functional and once it is clicked , it should take the user to the relevant medstar socia media page                                                                                                                                   |                     Pass                                      | 
APT-CU-6.0  | CU-6.0         | Contact Us                         | APT-CU-6.0.0: Click contact nav link | The link should be funtional and take the user to the contact page section displaying the page and information .                                                                                                                                                  |                     Pass                                      |
APT-SM-6.1  | SM-6.1         | Submit Btn                         | APT-SM-6.1.0: Click submit btn  | The btn should be functional and once it is clicked , it should validate the form and then submit the contact form information to Emailjs for client review.                                                                                                                                      |                     Pass                                      | 
APT-RS-6.2  | RS-6.2         | Reset Btn                          | APT-RS-6.2.0: Click Rest btn  | The btn should be functional and once it is clicked , it should Reset the contact form and clear all fields.                                                                                                                                                             |                     Pass                                      |                                                                                                                                   
APT-SM-6.3  | SM-6.3        | Social media Icon                   | APT-SM-6.3.0: Click Social media icon  | The icon should be functional and once it is clicked , it should link the user with the Medstar social media page.                                                                                                                                              |                     Pass                                      | 
APT-UL-7.0  | UL-7.0         | User login                        | APT-SM-7.0.0: Click login btn  | The btn should be functional and once it is clicked , it should validate and then decline or submit the login information to mongodb, granting access to the user.                                                                                                      |                     Pass                                      | 
APT-ULP-7.1  |LP-7.1         | Login Profile                     | APT-LP-7.1.0: Click Profile nav Link  | The Nav link should be functional and once it is clicked , it should display the profile page .                                                                                                                                                                  |                     Pass                                      | 
APT-LP-7.2  | Lh-7.2         | Login home                        | APT-LP-7.2.0:Click home nav link  | The nav link should be functional and once it is clicked , it should  display the task and message between user and doctor.                                                                                                                                          |                     Pass                                      | 
APT-NT-7.3  | NT-7.3         | New Task                          | APT-NT-7.3.0:Click new task nav link  | The nav link should be functional and once it is clicked , it should display the new task page with a form to fill by the user to enable user to communicate with their doctor .                                                                                 |                     Pass                                      | 
APT-ET-7.4  | ET-7.4         | Edit Task                         | APT-LP-7.4.0:Click edit task btn  | The btn should be functional and once it is clicked , it should allow the task  form to be edited by the user.                                                                                                                                                       |                     Pass                                      | 
APT-DT-7.5  | DT-7.5        |  Done Task                         | APT-LP-7.5.0:Click done task btn  | The btn should be functional and once it is clicked , it should delete the done task from the task list.                                                                                                                                                             |                     Pass                                      | 
APT-LO-7.6  | LO-7.6         | Login out                        | APT-L0-7.6.0:  Click  logout btn  | The btn should be functional and once it is clicked , it should log the user out of their account.                                                                                                                                                                    |                     Pass                                      | 
APT-R-7.7 | R-8.0           | Register                              | APT-R-8.0.0:  Click Register btn  | The btn should be functional and once it is clicked , it should validate the input fields and then register the user.                                                                                                                                            |                     Pass                                      | 
APT-DL-9.0  | DL-9.0         | Doctor login                        | APT-SM-9.0.0: Click login btn  | The btn should be functional and once it is clicked , it should validate and then decline or submit the login information to mongodb, granting access to the user.                                                                                                   |                     Pass                                      | 
APT-DLP-9.1  |DLP-9.1         | Doctor Login Profile              | APT-LP-9.1.0: Click Profile nav Link  | The Nav link should be functional and once it is clicked , it should display the profile page .                                                                                                                                                                |                     Pass                                      | 
APT-LP-9.2  | Lh-9.2         | Login home                        | APT-LP-9.2.0:Click home nav link  | The nav link should be functional and once it is clicked , it should  display the task and message between doctor and user.                                                                                                                                         |                     Pass                                      | 
APT-NT-9.3  | NT-9.3         | New Task                          | APT-NT-9.3.0:Click new task nav link  | The nav link should be functional and once it is clicked , it should display the new task page with a form to fill by the doctor to enable doctor to communicate with his patient(user) .                                                                       |                     Pass                                      | 
APT-ET-9.3.1  | ET-9.3.1        | Edit Task                         | APT-LP-9.3.1.0:Click edit task btn  | The btn should be functional and once it is clicked , it should allow the task  form to be edited by the doctor.                                                                                                                                               |                     Pass                                      | 
APT-DT-9.3.2  | DT-9.3.2        |  Done Task                         | APT-LP-9.3.2.0:Click done task btn  | The btn should be functional and once it is clicked , it should delete the done task from the task list.                                                                                                                                                      |                     Pass                                      |
APT-LW-9.4 | LW-9.4        | LabWork                              | APT-LW-9.4.0:  Click labwork navlink  | The navlink should be functional and once it is clicked , it should display the lab work form for the doctor to fill. The form should validate the inputs and then submit to the mongodb database.                                                             |                     Pass                                      | 
APT-PR-9.5 | PR-9.5        | Prescription                          | APT-PR-9.5.0:  Click  Prescription navlink |The navlink should be functional and once it is clicked , it should display the prescription form for the doctor to fill. The form should validate the inputs and then submit to the mongodb database.                                                    |                     Pass                                      | 
APT-PRO-9.6 | PRO-9.6        | Procedure                            | APT-PR0-9.6.0:  Click  Procedure navlink  | The navlink should be functional and once it is clicked , it should display the procedure form for the doctor to fill. The form should validate the inputs and then submit to the mongodb database                                                       |                     Pass                                      | 
APT-AID-9.7 | AID-9.7        | AI Diagnostic                         | APT-L0-9.7.0:  Click AI Diagnostic navlink   | The navlink should be functional and once it is clicked , it should display the AI diagnostic suit for the doctor's interacrtion.                                                                                                                    |                     Pass                                      | 
APT-AID-9.7.1 | AID 9.7       | AI Diagnostic                         | APT-L0-9.7.1.1:  Click AI Diagnostic suit/center   | The streamlit page should be functional and once the drop box is selected , it should dispaly a choice between diabetes or heart disease diagnosis, once the choice is made and the slidres are selected for their respective inputs the result for diabetes detection ratio should be between 0 negative & 1 positive while the heart disease detection is a ratio of >40 positive & <40 negative.  |                     Pass                                      | 
APT-MC-9.8 | MC-9.8        | Manage Categories                          | APT-L0-9.8.0:  Click  manage categories navlink  | The navlink should be functional and once it is clicked , it should display the manage categories page, the doctor should be able to delete and edit categories for his patients.                                                             |                     Pass                                      |  
APT-DLO-9.9 | DLO-9.9        | Login out                                | APT-L0-9.9.0:  Click  logout nav link  | The navlink should be functional and once it is clicked , it should log the doctor out of their account.                                                                                                                                                       |                     Pass                                      | 
APT-AL-10.0   | AL-10.0       | Admin login                             | APT-AL-10.0.0: Click login btn  | The btn should be functional and once it is clicked , it should validate and then decline or submit the login information to mongodb, granting access to the user.                                                                                             |                     Pass                                      |                                                                     
APT-AL0-10.1  | ALO-10.1        | Admin login-out                       | APT-ALO-10.1.0: Click login nav link  | The nav link should be functional and once it is clicked , it should logout the the user.                                                                                                                                                                |                     Pass                                      | 
APT-MR-11.0  | MR-11.0         | Medstar Register                        | APT-MR-11.0.0: Click Register link  | The btn should be functional and once it is clicked , it should validate and then decline or submit the information to mongodb.                                                                                                                           |                     Pass                                      | 
APT-SR-12.0  | SR-12.0        | Search Btn                               | APT-SR-12.0.0: Click search btn | The btn should be functional and once it is clicked , it should validate the user input and search the task db in mongodb for tasks_name, tasks_description and created_by and display the required searched entry or display No Result found if search field does not exit.   |                     Pass                                      | 
APT-SR-12.1  | SR-12.1         | Reset Btn                              | APT-SR-12.1.0: Click Reset btn | The btn should be functional and once it is clicked , it should reset the search field and display the complete list of tasks.                                                                                                                                  |                     Pass                                      | 


## Technologies 

The technologies employed to develop this web application was based on the principles of Design for X (DFX) also know as Design for excellence, the basis of this methodology is based
on cost to quality, making effective use of resources to minimize cost and relay more on innovation and technical knowledge to meet the users expectations.The software's used are mostly free 
and meet the **Requirements Traceability Catalog Table 1.0** to develop this website, innovation and technical knowledge was based on my recently aquired skills based on my journey so 
far with Code institute and the Canadian Business College.

Technologies deployed on this project:

 1. Languages deployed on project HTML,CSS,JavaScript and python.
 2. Frame work utilized on project [django](https://docs.djangoproject.com/en/3.2/) and [Jinja](https://jinja.palletsprojects.com/en/2.11.x/).
 3. django [database](https://docs.djangoproject.com/en/3.2/ref/databases/)
 4. Webapp live deployment with [Heroku](https://www.heroku.com/)
 5. Libaries utilized on project in requirements.txt
 6. For coding enviroment /IDE github [GitHub](http://github.com)
 7. Bootstrap cnd 4.4.1 [Bootstrap](https://getbootstrap.com/)
 8. Bootstrap Jquery 3.3.1 [Bootstrap](https://getbootstrap.com/)
 9. Bootstrap cnd font awesome [Bootstrap](https://www.bootstrapcdn.com/fontawesome/)
 10. AI Shopping Assistance-API [Alan-AI](https://alan.app/)
 11. Payment Platform-API [STRIPE](https://stripe.com/en-ca)
 12. Pop-up Widget-API [elfsight](https://elfsight.com/popup-widget/?utm_source=websites&utm_medium=clients&utm_content=popup&utm_term=8000-azure-octopus-najpf05z.ws-us03.gitpod.io&utm_campaign=free-widget)
 13. Google [font](https://fonts.google.com/)
 14. For README.md file image and website images editing and styling Canva software [Canva](https://www.canva.com/)
  

---------------------------------------------

 ## Deployment 

 After my User Acceptance Testing (UAT) I pushed the final version of my code to git hub , in my commit message I cataloged each change before my final push, the steps I took 
 can be seen below. 

 1. Complete the User UAT evaluation and made sure that all codes are funtional and operational.
 2. Used git commit -m to catalog all my changes in line with UAT requirement.
 3. Used git push to push my final version to my git hub repository. 
 

 Before my final push on github I had already deployed my project on Herouku to check connectivity and I clicked on the automatic deploy from master to ensure that all changes on github are reflected on heroku.
 Steps for deployment can be seen below, my project is now live on Heroku [Boutique-ado](https://boutique-ado-cbc.herokuapp.com/)
 

 1. Installed libaries and logged them in requitements.txt
 2. Create the PROCFILE
 3. Login to Heroku 
 4. Click on create new app
 5. Choose app name
 6. Choose country USA
 7. Click on Navlink Deploy
 8. Connect github Peristratus respository to Heroku
 9. Click on reveal config vars insert AWS access ID and keys, Database urls, Email host pass/ user, and the STRIPE secret key values, save them.
 10. Click on Automatic deploy master branch 
 11. Click on Deploy branch and wait for Heroku to build the logs and deploy the webapp.
 

-----------------------------------------------

## References

I would like to make references to certain educational Youtube tutorials and certain articles that have helped with my webdesign develop my skills as a Fullstack developer.


1. Online tutorials ALan AI [Web-DevSimplified](https://voice.alan.app/WebDevSimplified)
2. HTML/CSS security by sqreen online article [sqreen](https://www.sqreen.com/checklists/html-css-security-checklist)
3. Input patterns online article [HTML.com](https://html.com/attributes/input-pattern/)

-----------------------------------------------

## Licenses

All icons,logos and videos used on my website are only for educational purposes and will not be used for the commercial version:

1. Free random images from [google](https://www.google.com/) search engine.

-----------------------------------------------

## Author 

*Name: Olaorebikan Roy Abdallah*\
*Institute: Canadaian Business College (code Institute).*\
*Designation: Student.*\
*Course: Fullstack Developer.*

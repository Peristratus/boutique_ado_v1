## Boutique Ado E-Commerce Web app
![Project Image](/static/image/botique.png)

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
All Homeware | AH-4.3| Gain access to botique Ado website | **As a** user **I want** to access all Homeware nav link  **so that** I can have access to the all Homeware page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu all Homeware nav link **then** the system will take the user to the all Homeware  web page |    M   |
Special Offer drop down menu | SOM-5.0| Gain access to botique Ado website  | **As a** user **I want** to access the All Specials nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the All special nav link **then** the system will display a drop down menu |    M   |
New Arrivals | NA-5.1| Gain access to botique Ado website | **As a** user **I want** to access to the New Arrivals nav link  **so that** I can have access to the New Arrivals page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu New Arrivals nav link **then** the system will take the user to the New Arrivals web page |    M   |
Deals | DE-5.2| Gain access to botique Ado website | **As a** user **I want** to the Jeans nav link  **so that** I can have access to the Jeans page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Jeans nav link **then** the system will take the user to the Jeans wear web page |    M   |
Clearance | CLR-5.3| Gain access to botique Ado website | **As a** user **I want** to access the Clearance nav link  **so that** I can have access to the Clearance page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Clearance nav link **then** the system will take the user to the Clearance web page |    M   |
All Specials | AS-5.4| Gain access to botique Ado website | **As a** user **I want** to access all Specials nav link  **so that** I can have access to the all special page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu all specials nav link **then** the system will take the user to the all special web page |    M   |
Shop Now Btn | SNB-6.0| Gain access to botique Ado website | **As a** user **I want** to access the Shop now BTN  **so that** I can have access to the all Product page.| **Given**  that the user is on botique Ado home page, **When** they click on the shop now BTN  **then** the system will take the user to the all Product web page |    M   |
New arrival pop-up | NAP-7.0| Gain access to botique Ado website | **As a** user **I want** to access the pop-up new arrival widget  **so that** I can have access to the all products web page.| **Given**  that the user is on botique Ado home page, **When** they click on the pop up widget **then** the system will take the user to the all product web page |    M   |
Search engine | SE-8.0| Gain access to botique Ado website | **As a** user **I want** to access the search input box  **so that** I can search for products and item.| **Given**  that the user is on botique Ado home page, **When** they input an item or product in the search input box **then** the system will search for the item / product and display it to the user or display 0 products to the user  |    M   |
My Account drop down meu | MAM-9.0| Gain access to botique Ado website  | **As a** user **I want** to access the My Account nav link  **so that** I can have access the drop down menu.| **Given**  that the user is on the botique Ado home page home page, **When** they click on the My Account nav link **then** the system will display a drop down menu |    M   |
Login | LOG-9.0| Gain access to botique Ado website | **As a** user **I want** to access the Login nav link  **so that** I can have access to the Login page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Login nav link **then** the system will take the user to the Login web page |    M   |
Register | REG-9.1| Gain access to botique Ado website | **As a** user **I want** to access the Register nav link  **so that** I can have access to the Register page.| **Given**  that the user is on botique Ado home page, **When** they click on the drop down menu Register nav link **then** the system will take the user to the Register web page |    M   |
Add to Bag btn | ATB-10.0| Gain access to botique Ado website | **As a** user **I want** to access the Add to Bag Btn  **so that** I can buy the item.| **Given**  that the user is on botique Ado home page, **When** they click on the add to bag Btn **then** the system will display a toast message with the item and the go to secured check-out btn |    M   |
Shopping Bag Icon | SBI-10.1| Gain access to botique Ado website | **As a** user **I want** to access the shopping Bag Icon  **so that** I can see what is in my shopping bag.| **Given**  that the user is on botique Ado home page, **When** they click on the Shooping bag Icon **then** the system will display the users shoppping bag items giving them the option to add item, delet item countinue shopping Btn or Click the secured Check-out btn  |    M   |
Keep Shopping Btn | KSB-10.2| Gain access to botique Ado website | **As a** user **I want** to access the continue Keep Shopping Btn  **so that** I can Keep shooping to add more items to my shopping bag.| **Given**  that the user is on botique Ado home page, **When** they click on the Keep shopping Btn  **then** the system will display the All product page  |    M   |
Go to secured Check-out Btn | GSTC-10.3| Gain access to botique Ado website | **As a** user **I want** to access the secured to check-out Btn  **so that** I can proceed to the check-out.| **Given**  that the user is on botique Ado home page, **When** they click on the go to secured check-out Btn **then** the system will display the secured check out page |    M   |
Secured Check-out Btn  | SC-10.4| Gain access to botique Ado website | **As a** user **I want** to access the Check out form  **so that** I can fill in my details and credit card information.| **Given**  that the user is on botique Ado home page, **When** they click on the secured check-out Btn **then** the system will display the Check-out form |    M   |
Complete order Btn | CO-10.5| Gain access to botique Ado website | **As a** user **I want** to access the Complete order Btn  **so that** I can purchase my item or product.| **Given**  that the user is on botique Ado home page, **When** they click on the complete to order Btn **then** the system will accept the order through STRIPE api payment platform or decline my purchase |    M   |
Alan AI Btn | AI-11.0| Gain access to botique Ado website | **As a** user **I want** to access Alan AI Btn  **so that** I can talk, ask question about sales, suggestions on what to buy, be able to have a converstaion and navigate the site through voice command.| **Given**  that the user is on botique Ado home page, **When** they click on the Alan AI Btn **then** Alan AI will be able to have a meaningful conversation with the user and obey their commands or decline to obey their commands. |    M   |




## User-Acceptance-Testing

The UAT will define the criteria by which the website is considered to be "working",high, medium or low defects will be identified and cataloged for further improvements or regression testing.
The UAT critreria and results will confirm if the website can handle required task in a real-world scenarios, according to the Requirements Traceability Catalog Table 1.0.

*Table 2.0 User Acceptance Testing (UAT)*


 Test#    | User stories Ref# |        Description of task        |               Steps to evaluate    |                        Expected Result                                                                                                                                                                                                                               |            Pass / Fail / Comments                               |  
--------  |-------------------|-----------------------------------|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------| 
APT-H-1.0  | H-1.0               | Boutique ado nav link          | APT-H-1.0.0:   Click nav Link | The link should be funtional and take the user to the home page section displaying the page and information .                                                                                                                                                             |                     Pass                                      |
APT-APM-2.0  | APM-2.0           | Drop down menu                 | APT-APM-2.0.0:  Click the All Products Nav Link| The Link should be functional and display a dropdown menu with other links for the user to click on.                                                                                                                                                     |                     Pass                                      | 
APT-BP-2.1  | BP-2.1             | by price menu nav link              | APT-BP-2.1.0:  Click the by price Nav Link | The Link should be funtional and take the user to the by price page.                                                                                                                                                                                         |                     Pass                                      | 
APT-BR-2.2  | BR-2.2             | by rating menu nav link             | APT-BR-2.2.0:  Click the by rating Nav Link | The Link should be funtional and take the user to the by ratings page.                                                                                                                                                                                      |                     Pass                                      | 
APT-BC-2.3  | BC-2.3             | by category menu nav link           | APT-BC-2.3.0: Click the by category Link |The Link should be functional and allow the user to a have access to the by category page.                                                                                                                                                                      |                     Pass                                      |                                                                                     
APT-AP-2.4   | AP-2.4            |All Products menu nav link           | APT-AP-2.4.0: Click the all products Link | The Link should be functional and allow the user to have access to the All Products page.                                                                                                                                                                      |                     Pass                                      |
APT-CLM-3.0  | CLM-3.0           | Drop down menu                 | APT-CLM-3.0.0:  Click the clothing Nav Link| The Link should be functional and display a dropdown menu with other links for the user to click on.                                                                                                                                                     |                     Pass                                      | 
APT-AE-3.1  | AE-3.1             | Active & Essential wear menu nav link  | APT-AE-3.1.0:  Click the Active & Essential wear Nav Link | The Link should be funtional and take the user to the Active & Essential wear page.                                                                                                                                                                                         |                     Pass                                      | 
APT-JEN-3.2  | JEN-3.2           | Jeans menu nav link             | APT-JEN-3.2.0:  Click the jeans Nav Link | The Link should be funtional and take the user to the Jeans page.                                                                                                                                                                                      |                     Pass                                      | 
APT-SH-3.3  | SH-3.3             | Shirt menu nav link           | APT-SH-3.3.0: Click the by shirt Link |The Link should be functional and allow the user to a have access to the by shirt page.                                                                                                                                                                      |                     Pass                                      |                                                                                     
APT-CL-3.4   | CL-3.4           |clothing menu nav link           | APT-CL-3.4.0: Click the clothing Link | The Link should be functional and allow the user to have access to the clothing page.                                                                                                                                                                      |                     Pass                                      |                                                                
APT-HWM-4.0  | HWM-4.0           | Drop down menu                 | APT-CLM-3.0.0:  Click the homeware Nav Link| The Link should be functional and display a dropdown menu with other links for the user to click on.                                                                                                                                                     |                     Pass                                      | 
APT-BB-4.1  | BB-4.1             | Bed & Bath menu nav link  | APT-AE-4.1.0:  Click the Bed & Bath Nav Link | The Link should be funtional and take the user to the Bed & Bath page.                                                                                                                                                                                         |                     Pass                                      | 
APT-KD-4.2  | KD-4.2           | Kitchen & Dining menu nav link    | APT-KD-4.2.0:  Click the Kitchen & Dining Nav Link | The Link should be funtional and take the user to the Kitchen & Dining page.                                                                                                                                                                                      |                     Pass                                      | 
APT-AH-4.3  | AH-4.3             | ALL Homeware menu nav link      | APT-AH-4.3.0: Click the aLL Homeware Link |The Link should be functional and allow the user to a have access to the all Homeware page.                                                                                                                                                                      |                     Pass                                      |                   
APT-SOM-5.0  | SOM-5.0           | Drop down menu                 | APT-SOM-5.0.0:  Click the clothing Nav Link| The Link should be functional and display a dropdown menu with other links for the user to click on.                                                                                                                                                     |                     Pass                                      | 
APT-NA-5.1  | NA-5.1             | New Arrivals menu nav link  | APT-NA-5.1.0:  Click the New Arrivals Nav Link | The Link should be funtional and take the user to the New Arrivals page.                                                                                                                                                                                         |                     Pass                                      | 
APT-DE-5.2  | DE-5.2           | Deals menu nav link             | APT-DE-5.2.0:  Click the deals Nav Link | The Link should be funtional and take the user to the deals page.                                                                                                                                                                                      |                     Pass                                      | 
APT-CLR-5.3  |CLR-5.3             | Clearance menu nav link       | APT-CLR-5.3.0: Click the by Clearance  Link |The Link should be functional and allow the user to a have access to the Clearance  page.                                                                                                                                                                      |                     Pass                                      |                                                                                     
APT-AS-5.4   | AS-5.4           |All specials menu nav link           | APT-AS-5.4.0: Click all specials Link | The Link should be functional and allow the user to have access to the all specials page.                                                                                                                                                                      |                     Pass                                      |                                                                
APT-SNB-6.0 | SNB-6.0       |Shop Now btn                        | APT-SNB-6.0.0: Click Shop Now btn | The btn should be funtional and take the user to the all product page.                                                                                                                                                                                                    |                     Pass                                      | 
APT-NAP-7.0  | NAP-7.0        | New Arrival Pop-up widget advert  | APT-NAP-7.0.0: Click New Arrival btn |The button should be functional and allow the user to view the current page they are browsing through.                                                                                                                                                                                 |                     Pass                                      |   
APT-SE-8.0  | SE-8.0         | Search Engine                      | APT-SE-8.0.0: Input the item or product to search.  | The input box should be functional, take the users input, when the user clicks on the magnifying glass icon , the system should display the item/product or inform the user that the item/ product dose not exist.                                                                                                                                  |                     Pass                                      | 
APT-MAM-9.0  | MAM-9.0         | My Account drop down Menu        |APT-BL-9.0.0: Click my account nav link | The link should be funtional and display a drop down menu to the user with a selection of login or registetr .                                                                                                                                                        |                     Pass                                      |
APT-LOG-9.1  | LOG-9.1         | Login                            | APT-lOG-9.1.0: Click on the menu Login Link | The Link should be functional, once it is clicked , it should display the login form and validte the users credentials.                                                                                                                                   |                     Pass                                      | 
APT-RG-9.2  | REG-9.0         | Register                         | APT-RG-9.2.0: Click on the menu Register Link | The link should be funtional, once it is clicked, it should display the Sign-up form, validte the users credentials and send a confirmation email to the user to enable account activation.                                                                                                                                                |                     Pass                                      |
APT-ATB-10.0  | ATB-10.0      | Add to Bag                         | APT-ATB-10.0.0: Click on Add to bag btn  | The btn should be functional, once it is clicked , it should add the item to the users bag and display a toast with the image of the item(s), the total amout and a go to secured check-out Btn.                                                                                                                                     |                     Pass                                      | 
APT-SB-10.1  | SB-10.1         | Shopping Bag Icon                 | APT-SB-10.1.0: Click Shopping bag icon  | The icon should be functional, once it is clicked , it should should display the shopping bag items, update and remove buttons, secured check-out and Keep shopping btn.                                                                                                                                                             |                     Pass                                      |                                                                                                                                   
APT-KSB-10.2  | KSB-10.2        | Keep shopping Btn               | APT-KSB-10.2.0: Click Keep Shopping Btn  | The btn should be functional and once it is clicked , it should display the all products page to the user.                                                                                                                                              |                     Pass                                      | 
APT-GSTC-10.3  | GSTC-10.3    | Go to secured Check-out Btn         | APT-GSTC-10.3.0: Click the Go to secured Check-out Btn | The btn should be functional and once it is clicked , it should display the shopping bag items, update and remove buttons, secured check-out and Keep shopping btn.                                                                                                       |                     Pass                                      | 
APT-SC-10.4  |SC-10.4         | Secured check out-btn               | APT-SC-10.4.0: Click the secured check out Btn | The btn should be functional and once it is clicked , it should display the check-out form and complete order Btn .                                                                                                                                                                  |                     Pass                                      | 
APT-CO-10.5  | CO-10.5         | Complete order btn                 | APT-LP-10.5.0:Click order complete btn  | The Btn should be functional and once it is clicked , it should validate the check-out form and Credit/Debt card details,complete the payment through Stripe payment platform and send a confirmation email to the buyer.                                                                                                                                          |                     Pass                                      | 
APT-WH-10.5.1  | CO-10.5         | Web Hooks                        | APT-WH-10.5.1.0: Click order Complete  | The Btn should be functional and once it is clicked , if the user accedentaily shuts down the window while processing payment, the payment should go through and a confirmation email sent the buyer.                                                                                 |                     Pass                                      | 
APT-AI-11.0  | AI-11.0             | Alan AI                        | APT-AI-11.0.0: Click the Alan AI btn  | The btn should be functional and once it is clicked , the user, should be able to speak with Alan AI, Navigate the site via voice command, ask questions about items to buy, new arrivals, sales, suggestions on what to buy and have a meaningful  converstaion  with the user.                                                                                                                                                  |                     Pass                                      | 



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

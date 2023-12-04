# Team Project - D.7 Verification and Validation

**Team:** 8 - StudentDiscountz

## Description
StudentDiscountz is a website for students trying to save some money with designated scholarly discounts. The website's key feature centralizes student-specific discounts, enabling users to locate items they need for a cheaper price. The home page allows users to have a more general sense of discounts offered and even split some discounts by category. This allows deals like technology and dorm supplies to be separated for ease of use for the user. On top of that, they are also able to locate major specific discounts if the discount they want falls outside the general categories that the home page offers. The login and signup functionalities also allow users to come back and visit the discounts they had previously seen as well. Overall, StudentDiscountz simplifies the student shopping experience with centralized discounts, convenient discount categories, and a user-friendly login feature for personalized preferences. 

## Verification

As with deliverable 6, we used Django's built-in test framework, which is based on Python's unittest.
Apart from hardcoded API requests to fetch specific discounts, our site only uses the registration and login endpoints of our API, so that's what we've focused our tests on.

All of our automated tests can be found [Here.](https://github.com/aaronr7734/team-8-project/tree/main/code/server/discountz_app/automated_tests)
The example we'll be showcasing for this deliverable primarily tests a function-based view, but it also indirectly tests our custom register serializer class which can be found [here.](https://github.com/aaronr7734/team-8-project/blob/main/code/server/discountz_app/serializer.py#L48)
The function-based view tested was  our register_view, which can be found [here.](https://github.com/aaronr7734/team-8-project/blob/main/code/server/discountz_app/views.py#L41)
The test itself can be found [here.](https://github.com/aaronr7734/team-8-project/blob/main/code/server/discountz_app/automated_tests/mock_object_tests.py#L46)

```bash
python manage.py test discountz_app.automated_tests.mock_object_tests                                                                                 
Found 2 test(s).                                                                                                                                                                  
Creating test database for alias 'default'...                                                                                                                                     
Destroying old test database for alias 'default'...                                                                                                                               
System check identified no issues (0 silenced).                                                                                                                                   
..                                                                                                                                                                                
----------------------------------------------------------------------                                                                                                            
Ran 2 tests in 0.251s                                                                                                                                                             
                                                                                                                                                                                  
OK                                                                                                                                                                                
Destroying test database for alias 'default'...


## Acceptance Test (Elizabeth, Chase, Ceanna)

For the acceptance testing process of our website, we decided to use the Selenium framework utilizing Python, which also required us to download specific web
drivers for the different browsers that we each use. We have five automated tests in total, that each test different aspects of our website, which include
logging in, signing in, navigating to our GitHub through the Contact Us page, clicking on the different majors through the dropdown and clicking on their 
'View Deal' buttons and navigating through the different deal tabs on our homepage. 

1. Logging in
   Link to test: [login_test.py](./acceptance_tests/login_test.py)
   
   Link to video: [Login test video](https://youtu.be/rIVr9KscdE4)

   The user would go to our website, navigate to the login in page and put in their email and password and click on the submit button.
   They should then see a little pop up that welcomes them back and it redirects them to the homepage.

2. Signing up
   Link to test: [signup_test.py](./acceptance_tests/signup_test.py)
   
   Link to video: [Sign up video](https://youtu.be/RUQAT3N2LYg)
   
   This test shows the user navigating to our website and to the sign up page where they encouraged to provide their name, email, and to create a new
   password that is within our requirements. When they sign up, the user should be able to see a little pop up that states that they signed up.
   
3. Navigating home page
   Link to test: [Homepage_test.py](./acceptance_tests/Homepage_test.py)
   
   Link to video: [Home page video](https://youtu.be/KVUEtqRV2_k)

   For this test, we decided to demonstrate the functionality of the homepage by navigating to the different deal tabs and utilizing the dropdown to the
   different majors. This test also clicks on the login and sign up page from the home page to show that going from page to page is possible.

4. Clicking on the deals
   Link to test: [clickonDeal_test.py](./acceptance_tests/clickonDeal_test.py)

   Link to video: [clickonDeal test](https://youtu.be/MGeH8dHiC1E)

   Another test we created involves demonstrating one of the main functionalities of this website, to be able to click on the "View Deal" button for a
   certain discount and be redirected to the direct link of the discount. This test clicks on one discount per page or tab in order to show that the website
   is working.

5. Contact Us page
   Link to test: [ContactUs_test.py](./acceptance_tests/ContactUs_test.py)

   Link to video: [Contact Us video](https://youtu.be/N2RIetVRgg0)

   This final test was to make sure that the contact us page was reachable through the link on the footer on the homepage. This way, if any user that
   interacts wants to contribute to our project, they will have a way to contribute directly through our GitHub. 
   
## Validation

The user evaluations were split into three main individual tasks. Each of these tasks hit a major portion of the website's features. They were split into Authentication, Navigation, and Satisfaction.

## Authentication
The first task of “Authentication” included the users testing the Signing up and Logging in functionalities of the website. The main objective is to test the ability to locate the designated pages, the ease of use of the process, and the functionality of sending the data to the API.

### General Process ###
1. Visit the website’s homepage
2. Locate the designated sign-up page and sign up
3. Locate the login page and log in
4. Check if user data is available to the API

### Questions ###
1. How would you rate the navigation of our website? (Scale: Very Difficult - Very Easy)
2. Were you satisfied with the confirmation or welcome messages after signing up?
3. Would you reuse the system in the current state it is in right now or would improvements make it feel better?

### Data Collected ### 
1. “Very easy like I said before everything is visible and everything runs smooth”
2. “Yes, this just reassured me that the process worked instead of just being redirected”
3. “If there is anything to improve on it would be a larger library of options.”

## Navigation 
The next task of “Navigation” included the users testing the actual pages and discounts offered. This included not only the main pages but also the tabs leading to the different areas of interest and the discounts the links may redirect the user to. The main objective of this task is to evaluate the user’s experience with the selections and products offered, and whether the system provides an adequate capability for user handling. 

### General Process ###
1. Once redirected to the homepage, browse the deals located on the page
2. Explore the options specific to “Dorms”, “Books”, etc on the home page
3. Locate the major tab
4. Locate major of interest (if applicable) and browse discounts

### Questions ### 
1. The general idea of this website is to allow users to have a friendly user interface in order to find the discounts they may need. Do you feel as though you were able to find your major of interest? 
2. Does the homepage feel welcoming enough to keep looking at different areas of the website? 
3. If applicable, which specific pages did you find most useful or engaging?
4. Did the website’s design enhance or hinder your experience?
Were there any pages that you found confusing or less helpful? 

### Data Collected ### 
1. “Yes, I was able to find my major but this is nowhere near the whole lot that users may want to find discounts for.”
2. “It looks very approachable and professional and looks like a safe space to operate”
3. “I would say the majors of study because you really dive in on what’s available”
4. “Made it simple to navigate and everything was on display”
5. “To my knowledge no there wasn’t.”

## Satisfaction: 
The final task of “Satisfaction” included an overall evaluation of the user's experience of the website in general. This not only included the visual appearance of the website's pages but also their functionality and overall usability of the website. The main objective was to see if this was a website and product that they would consider using again in the future or if not, what improvements would they like to see to consider visiting again. 

### General Process: ###
1. Ask the user to reflect on their overall experience while browsing the website. 
2. Record results 

### Questions: ###
1. What are your thoughts on the visual appeal of our website?
2. Are there any additional features or content you would like to see on our website?
3. Were all the website features and functionalities easy to use?
4. On a scale of 1 to 10, how would you rate your overall experience with our website?
5. How likely are you to recommend our website to a fellow student?

### Data Collected: ###
1. “Gives me a modern feel to today's websites which are up to date”
2. “Perhaps maybe professional promotional videos to show off the site.”
3. “Yes, there were no issues while I was navigating through the website”
4. “Personally, I would give the website an 8. It has a very clean look and there were no major issues while I was going through the whole process of logging in and signing up”
5. “As of right now, it is less likely until more discounts are added and more majors are added as well, but I am very likely to share the idea of the website because it’s great”


## Reflection:
The observations recorded from the user experience and interactions were both positive and constructive. The overall navigation of the website was great between the three users tested. They made note that everything was well laid out and easy to navigate. However, the website did seem to lack a lot of information and looked to be in the too early stages for some users to visit the website again. Rather than changing the website, adding more information and creating a more interactive service for users would enhance the overall experience. The learning curve of the system is relatively low, there were no issues with functionalities and navigation. The tasks the users were given were all performed with no issues and they seemed to do everything with ease. The users seemed to like the layout of the website the best which is great but in the future, if we do decide to add more discounts, that should be the main emphasis and generally what the user focuses on more. Though the layout of the website is fantastic, there was some major dissatisfaction with the amount of discounts which is what our value proposition is heavily focused on. The main focus was centralizing student-specific discounts which is what we are slowly accomplishing. 



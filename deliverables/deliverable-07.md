# Team Project - D.7 Verification and Validation

**Team:** 8 - StudentDiscountz

## Description 

## Verification

## Acceptance Test (Elizabeth, Chase, Ceanna)

For the acceptance testing process of our website, we decided to use the Selenium framework utilizing Python, which also required us to download specific web
drivers for the different browsers that we each use. We have five automated tests in total, that each test different aspects of our website, which include
logging in, signing in, navigating to our GitHub through the Contact Us page, clicking on the different majors through the dropdown and clicking on their 
'View Deal' buttons and navigating through the different deal tabs on our homepage. 

1. Logging in
   Link to test: [login_test.py](./acceptance_tests/login_test.py)
   
   Link to video:
   
   The user would go to our website, navigate to the login in page and put in their email and password and click on the submit button.
   They should then see a little pop up that welcomes them back and it redirects them to the homepage.

2. Signing up
   Link to test: [signup_test.py](./acceptance_tests/signup_test.py)
   
   Link to video:
   
   This test shows the user navigating to our website and to the sign up page where they encouraged to provide their name, email, and to create a new
   password that is within our requirements. When they sign up, the user should be able to see a little pop up that states that they signed up.
   
3. Navigating home page
   Link to test: [Homepage_test.py](./acceptance_tests/Homepage_test.py)
   
   Link to video:

   For this test, we decided to demonstrate the functionality of the homepage by navigating to the different deal tabs and utilizing the dropdown to the
   different majors. This test also clicks on the login and sign up page from the home page to show that going from page to page is possible.

4. Clicking on the deals
   Link to test: [clickonDeal_test.py](./acceptance_tests/clickonDeal_test.py)

   Link to video:

   Another test we created involves demonstrating one of the main functionalities of this website, to be able to click on the "View Deal" button for a
   certain discount and be redirected to the direct link of the discount. This test clicks on one discount per page or tab in order to show that the website
   is working.

5. Contact Us page
   Link to test: [ContactUs_test.py](./acceptance_tests/ContactUs_test.py)

   Link to video:

   This final test was to make sure that the contact us page was reachable through the link on the footer on the homepage. This way, if any user that
   interacts wants to contribute to our project, they will have a way to contribute directly through our GitHub. 
   
## Validation

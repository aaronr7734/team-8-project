## Team Project – D.2 Requirements


### 1. Positioning 


#### Problem statement

The problem of finding scattered and unreliable student discounts affects college students and service providers alike; the impact of which is wasted time and missed opportunities for students to save money and for businesses to engage a valuable customer base. For college students who want to save money and have Major-Specific Deals, CollegeDiscountz is a web-based discount aggregator. That provides a one-stop platform for student-specific discounts on a range of goods and services.


#### Product Position Statement

Unlike Unidays, Our product focuses on local and small businesses, expanding the range of discounts available and supporting businesses that call Flagstaff home.


#### Value proposition and customer segment

***Value Proposition***: CollegeDiscountz is a web-based discount aggregator for college students, making it easier to save money by centralizing student-specific discounts, especially from small local businesses.

### 2. Stakeholders

***College Students*** - Since they are interested in finding discounts and deals that the website would provide.

***College/University*** - Universities could take an interest in promoting the website for student to use and improve a student's experience Businesses - Whether it be local or on a worldwide level, they would also be a stakeholder since they are the ones providing the deals for the students to use. 

***Parents*** - They would have an interest in the website so they can share deals with loved ones that are in college. 

***Teachers*** - Especially when certain teachers require certain supplies this would take an interest in them so that it can benefit the students can get the material and at a cheaper price. Competitors - They would take an interest since we plan on doing some elements different compared to them that they might take an interest in. Developers - Where they are the ones that are maintaining the website and taking an interest in the website itself.


### 3. Functional requirements  

1. Search Functionality: For students to quickly find discounts they're looking for.
2. Student Verification: So students can use us to verify their student status
3. Category filters: So students can filter by books, tech, major, etc.
4. Location Services: So students can find local deals.
5. Favorites and Bookmarks: So students can save their favorite discounts and be notified if they change.
6. Merchant Dashboard: So businesses can log in and post their own deals students might be interested in.
7. Email Notifications: To alert students when new deals in their favorite categories are available.

### 4. Non-functional requirements 

1. **Usability Aspect**, we want to focus on making sure that it is easy to read the different categories for students to decide what they are looking for on the website. The website should be user-friendly and students should understand what they are looking for on the home page alone.

2. **Security Aspect**: if we do decide to go the route of using a student’s college information like email to confirm they are a college student. Our goal would be to conduct regular security sweeps so information will not be stolen and leaked.

3. **Compliance**: It helps to make sure that our product stays within legal requirements, like data protection laws.
Objective Goal/Measurements: Regularly updating the website to make sure that it doesn’t violate relevant laws and regulations.

5. **Reliability**: Ensures that the website is accessible and operational when the users need it.
Objective Goal/Measurements: 85% uptime over a period of a semester. 

5. In the search bar you will need to be able to look for discounts and discounts that are locoal. The gaol is for  people to have a sreach bar. That they will not get lost when looking for a discount.

6. The next one would be a feature on the account. If you have an account with the website. You would be able to save discounts to your account. The goal is to be able to save the discount for later. And that it would not get lost

7. **Performance Efficiency - Time Behavior**:Fast load times improve user experience and can contribute to higher user retention rates and the **Verifiability** aspect includes performance metrics that should indicate that search result loading time is under 2000 milliseconds.


### 5. Minimum Viable Product 

Our MVP aims to display a manually populated list of student discounts and allows admins to add new discounts through a simple backend interface. The site will have:

- A homepage that outlines the site's purpose.
- One or more static pages for listing discounts by category.
- A basic admin interface to add new discounts to the list.

**Validation**:
- Homepage clarity will be gauged through user feedback.
- The understandability of the  static discount pages will be validated by surveying the clients we've previously interviewed.
- The admin interface will be validated by successfully adding new discounts.

**Search and Filters**: 
- Feature: implements search engine and filter options to help students to find discounts that they want.
- Testing Approach: Implementation
- Validation: Have users test the search and filter options and give feedback

**Student Verification**:
- Feature: Develop and implement a system that would help verify that a user is a student at a university/college.
- Testing Approach: Prototyping
- Validation: Create a verification prototype and conduct tests that display its accuracy and user-friendliness.

**Category Clicking**: 
- Feature: clicking on a category like food so it will load the page to show all the discounts relating to food. We would use the implementation method because we would need the button labeled as food and implement if the transaction would show the discounts relating to food. Students would save time on the website by having discounts organized by category.

**Account Creation**: 
- Feature: letting students create an account, just the account alone so they can personalize their experience down the line. We would use the prototype method so we can try to create the process of letting the students create an account. Students can eventually favorite certain companies they have an interest in but the main goal would be for them to have an account.


### 6. Use cases 

***Use Case***: Browsing Onto Website\
***Actor***: User (College Student)\
***Trigger***: User Decides to click website link\
***Pre-condition:*** User must be aware of website\
***Post-condition:*** User is browsing website\
***Success Scenario:***
1. They are looking for discounted item\
2. They look for discounted items on search engine\
3. They find a link to website\ 

Diagram: 

![User Case 1](userCase1.png "User Case 1 Diagram")

**Use Case**: Creating an Account\
**Actor**: User (College Student)\
**Trigger**: Want to be able to leave reviews\
**Pre-condition**: User must have found a discount they liked\
Post-condition: User is able to log in and promote other discounts\
Success Scenario: 
User uses website and likes a discount
1. They want to promote it to show validity but they must leave a comment to do that
2. In order to leave a comment, they must create an account
3. The account is created 

Diagram: 

![User Case 2](userCase2.png "User Case 2 Diagram")


**Use Case** : Logging user into system\
**Actor**: User\
**Trigger**: User decides to log into the system\
**Pre-condition**: user must be in the system\
Post-Condition: User is logged into the system\
Success Scenario:
1. Username is taken by the system
2. The password is taken by the system
3. The user is logged into the system

Diagram: 

![User Case 3](userCase3.png "User Case 3 Diagram")


**Use Case**: Acquiring the discount\
**Actor**:: User (College Student)\
**Trigger**: User Decides to click discount link\
**Pre-condition**: User must look for that discount link\
Post-condition: User must want that discount\
Success Scenario: 
1. They must want the discount
2. The user is taken to the other website
3. User found a discount they like

Diagram: 

![User Case 4](userCase4.png "User Case 4 Diagram")

**Use Case**: Checking the system\
**Actor**:: Admin system\
**Trigger**: The admin system makes sure the discounts are up to date\
Pre-condition: The website is still working\
Post-condition: Admin makes sure that the discount that is wrong is taken down.\
Success Scenario:
1. The website is still running
2. Outdated discounts are taken down
3. Admin make sure everything is okay

Diagram: 

![User Case 5](userCase5.png "User Case 5 Diagram")

**Use Case**: Verifying your a college students\
**Actor**: User (College Student)\
**Trigger**: User makes sure that are college students\
**Pre-condition**: User must be college\
Post-condition: User logs in a college student beginning\
Success Scenario: 
1. Get college discounts
2. Putting their college email address
3. Verifies that they go that school

Diagram: 

![User Case 6](userCase6.png "User Case 6 Diagram")



### 7. User stories 

1. As a freshman college student, I want to be able to find easy discounts, so that I can have an easy transition into college

- Priority: Medium
- Estimated Poker Planning: 13

2. As a college student who is on a scholarship, I want to be able to find discounts, so that I can use my grant money in an affordable way.
- Priority Level: High 
- Estimated Poker Planning: 13 

3. As a low-income college student, I want to be able to get the best discounts so that I can save money
- Priority: High 
- Estimated Poker Planning: 8

4. As a parent of a college student, I want my kid to have their wanted necessities at the lowest price so that I am not financially struggling
-Priority: High 
- Esitmated Poker Planning: 13

5. As a registered user, I want to be able to verify that I’m a student by providing my school email and university name so that I can access the discounts
- Prority: High 
- Estimated Poker Planning: 8 

6. As a student, I would like to save the companies that provide the products I like the most so that I can access these discounts later
- Priority: Low
- Estimated Poker Planning: 8

7. As a computer science student, I rely heavily on my laptop for assignments and projects. Having a website that shows discounts on electronics would allow me to maintain a reliable academic tool without straining my limited budget
- Priority: Medium 
- Estimated Poker Planning: 3

8. As a health-conscious college student, a website that shows discounts on nutritious food items and kitchen essentials would make it more feasible to afford healthy choices within my financial constraints
- Priority: Low
- Estimated Poker Planning: 8

9. As a student that frequently goes shopping, I want to receive notifications when new discounts become available
- Priority: Medium 
- Estimated Poker Planning: 13

10. As a small business owner, I want a place to promote the discounts for students I offer
- Priority: Low
- Estimated Poker Planning: 13

11. As a student, I want to be able to find discounts that I can favorite so that I can know when they are having specials or deals that I would want to participate in
- Priority: Low 
- Estimated Poker Planning: 3

12. As a teacher, I want to be able to provide my students with resources especially something like materials for my course so that students can benefit from having a cheaper price and still get the materials they need for my course
- Priority: Medium
- Estimated Poker Planning: 13


### 8. Issue Tracker 

[Issue Tracker Link](https://github.com/aaronr7734/team-8-project/issues)\
![Issue Tracker Image](issueTracker.png "Issue Tracker Image")




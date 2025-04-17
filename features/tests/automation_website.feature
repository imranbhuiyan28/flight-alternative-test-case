
Feature: Automation Website Test Case


@automation
  Scenario: Register User
    Given  Open the main page
    Then   Verify that home page is visible successfully
    Then   Click on Signup / Login button
    When   Verify New User Signup! is visible
    And    Enter name and email address
    And    Verify that ENTER ACCOUNT INFORMATION is visible
    Then   Fill details: Title, Name, Email, Password, Date of birth
    When   Select checkbox Sign up for our newsletter
    Then   Select checkbox offer
    And   Fill the address information
    Then   Verify that ACCOUNT CREATED is visible


@test
  Scenario: Register User with existing email
    Given Open the main page
    Then  Click on Signup / Login button
    When  Verify New User Signup! is visible
    When  Enter name and email address
    And   Verify error Email Address already exist is visible
@test
  Scenario: Login User with correct email and password
    Given Open the main page
    Then  Click on Signup / Login button
    And   Verify Login to your account is visible
    Then  Enter correct email address and password
    And   Click login button
    When  Verify that Logged in  is visible


@test
  Scenario: Logout User button is working
    Given Open the main page
    Then  Click on Signup / Login button
    And   Verify Login to your account is visible
    Then  Enter correct email address and password
    And   Click login button
    Then  click on logout button
    And   Verify navigate to Login to your account page


@test
  Scenario: Contact Us Form
    Given Open the main page
    Then  Click on Contact Us button
    And   Verify GET IN TOUCH is visible
    When  Enter information and message
    Then  Upload file
    And   Click Submit button
    Then  Click OK button
    Then  Verify success message is visible

@test
  Scenario: Verify All Products and product detail page
    Given Open the main page
    Then  Verify that home page is visible successfully
    When  Click on Products button
    And   Verify user is navigated to ALL PRODUCTS page successfully
    When  Click on View Product of first product
    And   Verify that detail


@test
  Scenario:Add Products in Cart
    Given Open the main page
    When  Click on Products button
    Then  Hover over first product and click Add to cart


@test
  Scenario: Verify Scroll Up using 'Arrow' button and Scroll Down functionality
    Given Open the main page
    Then  Verify that home page is visible successfully
    And   Scroll down page to bottom
    Then  Verify SUBSCRIPTION is visible
    When  move upward
    Then  Verify that page is scrolled up and Full-Fledged practice website for Automation text is visible on screen


@test
  Scenario: Verify Product quantity in Cart
    Given Open the main page
    When  Click on View Product of first product
    Then  Increase quantity to 4
    And   Click Add to cart button
    Then  Click View Cart button
    Then  Verify that product is displayed in cart page with exact quantity



























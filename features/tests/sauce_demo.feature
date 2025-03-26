
Feature: Saucedemo website test



#------------login page------------------------
  Scenario: verify login page
    Given  open website page
    Then   login the page
    And    verify page open
    Then   sort page low to high




  Scenario: verify cart page
    Given  open website page
    Then   login the page
    Then   sort page low to high
    And    pick 2 item to the cart
    Then   click on cart icon
    When  fill up the information
    Then   verify the page
    And    click finish

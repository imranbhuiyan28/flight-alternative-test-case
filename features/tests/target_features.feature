
Feature: Test Case Project



  Scenario: Open the Target Page and Verify 10 cells

    Given   open target circle page
    Then    verify the 18 cells


  Scenario: open target and verify product

    Given   Open target main page
    When    Search for pencil
    Then    verify search result pencil in url

  @smoke
  Scenario: User can add a product to cart

    Given  Open target main page
    When   Search for pencil
    And    Click on cart
    And    store product name
    Then   Confirm add to cart from side nav
    Then   open cart page
    And    verify car has 1 items
    Then   verify correct product name


  Scenario: open any product

    Given open target main page
    When  search for pen
    Then  Verify every product has name and image




  @smoke
  Scenario: hover cursor to fav
    Given   Open target main page
    When    search for pen
    And     hover to favourite icon
    Then    favourite icon shown




  Scenario: User is able to open Privacy Policy

    Given Open target app
    And   Store original window
    When  Click Privacy Policy link
    Then  Switch to new window
    Then  Verify Privacy Policy page opened
    And   Close current page
    And   Return to original window

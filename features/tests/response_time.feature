Feature: Page Load and Performance
@smoke
  Scenario: Homepage loads within acceptable time
    Given I measure the homepage load time
    Then it should load in under 3 seconds
@smoke
  Scenario: Search results respond quickly
    Given open website
    When I search from Boston to Chicago
    Then the results should appear within five seconds

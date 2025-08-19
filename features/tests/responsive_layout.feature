Feature: Responsive Design
@mobileview
  Scenario: Mobile layout collapses menu
    Given I open the site in mobile view
    Then the menu should collapse into a hamburger icon

  Scenario: Desktop layout renders correctly
    Given I open the flight website
    Then there should be no horizontal scroll

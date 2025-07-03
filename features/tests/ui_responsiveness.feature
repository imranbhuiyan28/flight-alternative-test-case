Feature: UI Responsiveness

  @smoke @mobileview
  Scenario: Validate mobile view layout
    Given open website
    Then the menu should collapse into a hamburger icon
    And the layout should not overflow or break
  @smoke
  Scenario: Validate desktop layout
    Given open website
    Then all elements should align properly without horizontal scroll

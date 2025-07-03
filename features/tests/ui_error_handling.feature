Feature: UX - Error Feedback
@smoke
  Scenario: Search with empty fields
    Given open website
    When I click the Search button without filling any field
    Then an error message or warning should be displayed

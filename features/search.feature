Feature: Search Functionality
  @implemented
  Scenario: Search for a valid product
    Given I got navigated to Home page
    When I enter valid product like HP into the search box field
    And I click on Search button
    Then Valid product should get displayed in search results

  @implemented
  Scenario: Search for an invalid product
    Given I got navigated to Home page
    When I enter invalid product like Honda into the Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results

  @implemented
  Scenario: Search without entering any product
    Given I got navigated to Home page
    When I dont enter anything into Search box field
    And I click on Search button
    Then Proper message should be displayed in Search results
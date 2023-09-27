Feature: Login
  @completed
  Scenario Outline: Login with valid credentials
    Given I navigate to login page
    When I enter valid <email> and valid <password> into the fields
    And I click on login button
    Then I should get logged in
    Examples:
    |email| password|
    |firtest1@gmail.com| testpassword|

  @completed
  Scenario: Login with invalid email and valid password
    Given I navigate to login page
    When I enter invalid email and valid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @completed
  Scenario: Login valid email and invalid password into the fields
    Given I navigate to login page
    When I enter valid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @completed
  Scenario: Login with Invalid credentials
    Given I navigate to login page
    When I enter invalid email and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @completed
  Scenario: Login without entering any credentials
    Given I navigate to login page
    When I dont enter anything into email and password fields
    And I click on login button
    Then I should get a proper warning message


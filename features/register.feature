Feature: Register
  @register
  Scenario: Register with mandatory fields
    Given I navigate to Register page
    When I enter below mandatory fields
    |first_name | last_name| telephone| password| confirm_password|
    |abc        |def       | 1234567890| abcd1234| abcd1234       |
    And I click on continue button
    Then Account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to Register page
    When I enter all fields
    |first_name | last_name| telephone| password| confirm_password|
    |abc        |def       | 1234567890| abcd1234| abcd1234       |
    And I click on continue button
    Then Account should get created

  @register
  Scenario: Register with a duplicate email address
    Given I navigate to Register page
    When I enter all fields with existing email
    |first_name | last_name| email| telephone| password| confirm_password|
    |abc        |def       | firtest1@gmail.com| 1234567890| abcd1234| abcd1234       |
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to Register page
    When I dont enter any details
    And I click on continue button
    Then Proper warning messages for every mandatory fields should be display
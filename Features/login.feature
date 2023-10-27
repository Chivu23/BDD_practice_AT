Feature: Check the functionality of login page
  #Scenario 1: correct username + correct pass
  #Scenario 2: incorrect username + correct pass
  #Scenario 3: incorrect username + incorrect pass
  #Scenario 4: correct username + incorrect pass

  Scenario: Success login
    Given I am on the ebay login page
    When I insert the correct username and password
    And I click login button
    Then I can login in the application

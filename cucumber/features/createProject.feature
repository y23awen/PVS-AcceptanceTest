Feature: Create Project

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    @browser
    Scenario: Create a github project
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <react> 
          And I fill url as <https://github.com/facebook/react>
          And I click the create button
         Then I should see the project I just created
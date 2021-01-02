Feature: Create Project

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario: Create a project with github repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <react> 
          And I fill github url as <https://github.com/facebook/react>
          And I click the create button
         Then I should see the project name as <react> I just created

    Scenario: Create a project with wrong github repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <react> 
          And I fill github url as <https://github>
          And I click the create button
         Then I should see the alert with message <github error> and I accept it   
          
    Scenario: Create a project with sonarqube repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <timelog> 
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=ssl.ois%3Atimelog_api>
          And I click the create button
         Then I should see the project name as <timelog> I just created

    Scenario: Create a project with wrong sonarqube repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <pvs_front_end> 
          And I fill sonarqube url as <http://140.124.181>
          And I click the create button
         Then I should see the alert with message <sonar error> and I accept it   
         
    Scenario: Create a project with github and sonarqube repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <PVS_web> 
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
         Then I should see the project name as <PVS_web> I just created


    Scenario: Create a project with right github and wrong sonarqube repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <PVS_web> 
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I fill sonarqube url as <http://140.124.181>
          And I click the create button
         Then I should see the alert with message <sonar error> and I accept it   

    Scenario: Create a project with wrong github and right sonarqube repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <PVS_web> 
          And I fill github url as <https://github>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
         Then I should see the alert with message <github error> and I accept it   

    Scenario: Create a project with wrong github and wrong sonarqube repository
        Given I'm on the select project page
         When I click the create project card
          And I fill project name as <PVS_web> 
          And I fill github url as <https://github>
          And I fill sonarqube url as <http://140.124>
          And I click the create button
         Then I should see the alert and I accept it   
          And I should see the alert and I accept it   

          
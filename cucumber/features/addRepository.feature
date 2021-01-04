Feature: Add Repository

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario: Add a repository with sonarqube repository
        Given I click the create project card
          And I fill project name as <PVS_react_1>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
         When I click the add repository icon on <PVS_react_1> project card
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react> to add repository
          And I click the add repository create button
         Then I should see the sonar icon on <PVS_react_1> project card        
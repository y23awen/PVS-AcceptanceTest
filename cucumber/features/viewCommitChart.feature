Feature: View Commit Chart

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario: User view project introduction
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
         When I enter the dashboard page of the <PVS_react> project
         Then I see project name with <PVS_react>

        # Examples:
        #     | ProjectName   | githubUrl                                       |
        #     | PVS-react     |https://github.com/imper0502/pvs-web       |
        #     | PVS-springboot|https://github.com/imper0502/pvs-springboot|

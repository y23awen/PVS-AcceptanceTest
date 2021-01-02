Feature: View Commit Chart

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario Outline: User view project introduction
        Given I have added a project <ProjectName> with github repository url <url>
         When I enter the commit page of the <ProjectName> project
         Then I see a loading animation
         Then the loading animation disappear
         Then I see project name with <ProjectName>

        Examples:
            | ProjectName   | url                                       |
            | PVS-react     |https://github.com/imper0502/pvs-web       |
            | PVS-springboot|https://github.com/imper0502/pvs-springboot|

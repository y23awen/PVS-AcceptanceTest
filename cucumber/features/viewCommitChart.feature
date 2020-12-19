Feature: View Commit Chart

    Scenario Outline: User view project introduction
        Given I have added a project <ProjectName> with github repository url <url>
         When I enter the commit page of the <ProjectName> project
         Then I see project name with <ProjectName>
        Examples:
            | ProjectName   | url                                       |
            | PVS-react     |https://github.com/imper0502/pvs-web       |
            | PVS-springboot|https://github.com/imper0502/pvs-springboot|

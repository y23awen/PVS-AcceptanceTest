Feature: demo

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario: Whole system acceptance test
        Given I click the create project card
          And I fill project name as <PVS_demo>
          And I fill github url as <https://github.com/imper0502/pvs-spring-boot>
          And I click the create button
          And I click the add repository icon on <PVS_demo> project card
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-springboot> to add repository
          And I click the add repository create button
          And I should see the sonar icon on <PVS_demo> project card
         When I click the <PVS_demo> project card
         Then I see a <GitHub> button in the sidebar
          And I see a <Commits> button in the sidebar
          And I see a <Issues> button in the sidebar
          And I see a <Code Base> button in the sidebar
          And I see a <SonarQube> button in the sidebar
          And I see a <Code Coverage> button in the sidebar
          And I see a <Code Smells> button in the sidebar
          And I see a <Duplications> button in the sidebar
         When I click the <Commits> button in the sidebar
         Then I see a loading animation
          And The loading animation disappear
          And I see project name with <PVS_demo>
          And I see a <commit> chart with title <Team>
          And I see a <commit> chart with title <Member>
          And I see a dropdown with default value <5>
         When I click the <Issues> button in the sidebar
         Then I see a loading animation
          And The loading animation disappear
          And I see project name with <PVS_demo>
          And I see a <issue> chart with title <Team>
         When I click the <Code Base> button in the sidebar
         Then I see a loading animation
          And The loading animation disappear
          And I see project name with <PVS_demo>
          And I see a <codebase> chart with title <Team>
         When I click the <Code Coverage> button in the sidebar
         Then I see project name with <PVS_demo>
          And I see the chart title <Code Coverage>, the number of SonarQube type, and the <Code Coverage> chart
         When I click the <Bugs> button in the sidebar
         Then I see project name with <PVS_demo>
          And I see the chart title <Bugs>, the number of SonarQube type, and the <Bugs> chart
         When I click the <Code Smells> button in the sidebar
         Then I see project name with <PVS_demo>
          And I see the chart title <Code Smells>, the number of SonarQube type, and the <Code Smells> chart
         When I click the <Duplications> button in the sidebar
         Then I see project name with <PVS_demo>
          And I see the chart title <Duplications>, the number of SonarQube type, and the <Duplications> chart



    


    
    
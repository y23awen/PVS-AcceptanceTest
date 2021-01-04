Feature: View Project With Only SonarQube Repository

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario: User view project introduction
        Given I click the create project card
          And I fill project name as <PVS_react_1>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
         When I click the <PVS_react_1> project card
         Then I see project name with <PVS_react_1>

    Scenario: User view sidebar
        Given I click the create project card
          And I fill project name as <PVS_springboot_1>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-springboot>
          And I click the create button
         When I click the <PVS_springboot_1> project card
         Then I see a <SonarQube> button in the sidebar
          And I see a <Code Coverage> button in the sidebar
          And I see a <Code Smells> button in the sidebar
          And I see a <Duplications> button in the sidebar

    Scenario: User view sidebar and SonarQube button is foldable
        Given I click the create project card
          And I fill project name as <timelog_1>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=ssl.ois%3Atimelog_api>
          And I click the create button
          And I click the <timelog_1> project card
         When I click the <SonarQube> button in the sidebar
         Then I cannot see a <CodeCoverage> button in the sidebar
          And I cannot see a <CodeSmells> button in the sidebar
          And I cannot see a <Duplications> button in the sidebar

    Scenario: User view SonarQube CodeCoverage Information
        Given I click the create project card
          And I fill project name as <PVS_react_2>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
          And I click the <PVS_react_2> project card
         When I click the <Code Coverage> button in the sidebar
         Then I see project name with <PVS_react_2>
          And I see the chart title <Code Coverage>, the number of SonarQube type, and the <Code Coverage> chart

    Scenario: User view SonarQube Bugs Information
        Given I click the create project card
          And I fill project name as <PVS_react_2>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
          And I click the <PVS_react_2> project card
         When I click the <Bugs> button in the sidebar
         Then I see project name with <PVS_react_2>
          And I see the chart title <Bugs>, the number of SonarQube type, and the <Bugs> chart

    Scenario: User view Github Code Smells chart
        Given I click the create project card
          And I fill project name as <PVS_react_2>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
          And I click the <PVS_react_2> project card
         When I click the <Code Smells> button in the sidebar
         Then I see project name with <PVS_react_2>
          And I see the chart title <Code Smells>, the number of SonarQube type, and the <Code Smells> chart

    Scenario: User view Github Duplications chart
        Given I click the create project card
          And I fill project name as <PVS_react_2>
          And I fill sonarqube url as <http://140.124.181.143:9000/dashboard?id=pvs-react>
          And I click the create button
          And I click the <PVS_react_2> project card
         When I click the <Duplications> button in the sidebar
         Then I see project name with <PVS_react_2>
          And I see the chart title <Duplications>, the number of SonarQube type, and the <Duplications> chart
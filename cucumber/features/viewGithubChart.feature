Feature: View Project With Only Github Repository

    Background: User log in to PVS
        Given I open the browser
          And I go to PVS
          And I log in

    Scenario: User view project introduction
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
         When I click the <PVS_react> project card
         Then I see project name with <PVS_react>

    Scenario: User view sidebar
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
         When I click the <PVS_react> project card
         Then I see a <GitHub> button in the sidebar
          And I see a <Commits> button in the sidebar
          And I see a <Issues> button in the sidebar
          And I see a <Code Base> button in the sidebar

    Scenario: User view sidebar and Github button is foldable
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
          And I click the <PVS_react> project card
         When I click the <GitHub> button in the sidebar
         Then I cannot see a <Commits> button in the sidebar
          And I cannot see a <Issues> button in the sidebar
          And I cannot see a <Code Base> button in the sidebar

    Scenario: User view Github commit chart
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
          And I click the <PVS_react> project card
         When I click the <Commits> button in the sidebar
         Then I see a loading animation
          And The loading animation disappear
          And I see project name with <PVS_react>
          And I see a <commit> chart with title <Team>
          And I see a <commit> chart with title <Member>
          And I see a dropdown with default value <5>

    Scenario: User view Github issue chart
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
          And I click the <PVS_react> project card
         When I click the <Issues> button in the sidebar
         Then I see a loading animation
          And The loading animation disappear
          And I see project name with <PVS_react>
          And I see a <issue> chart with title <Team>

    Scenario: User view Github codebase chart
        Given I click the create project card
          And I fill project name as <PVS_react>
          And I fill github url as <https://github.com/imper0502/pvs-web>
          And I click the create button
          And I click the <PVS_react> project card
         When I click the <Code Base> button in the sidebar
         Then I see a loading animation
          And The loading animation disappear
          And I see project name with <PVS_react>
          And I see a <codebase> chart with title <Team>

    
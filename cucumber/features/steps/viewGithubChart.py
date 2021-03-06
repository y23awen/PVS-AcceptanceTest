from behave import given, when, then
from time import sleep

@given(u'I click the create project card')
def step_impl(context):
    context.browser.clickCreateProjectCard()

@given(u'I fill project name as <{projectName}>')
def step_impl(context, projectName):
    context.browser.inputProjectName(projectName)


@given(u'I fill github url as <{githubUrl}>')
def step_impl(context, githubUrl):
    context.browser.inputGithubRepositoryUrl(githubUrl)


@given(u'I fill sonarqube url as <{sonarUrl}>')
def step_impl(context, sonarUrl):
    context.browser.inputSonarRepositoryUrl(sonarUrl)

@given(u'I click the create button')
def step_impl(context):
    context.browser.clickCreateProjectButton()

@given(u'I have added a project {projectName} with github repository url {url}')
def step_impl_add(context, projectName, url):
    context.browser.addProject(projectName, url)
    # raise NotImplementedError(u'I have added a project {projectName} with github repository url {url}')

@given(u'I click the <{projectName}> project card')
@when(u'I click the <{projectName}> project card')
def step_impl_enter(context, projectName):
    context.browser.clickProjectCard(projectName)
    # raise NotImplementedError(u'STEP: When I enter the commit page of the PVS-springboot project')

@then(u'I see project name with <{projectName}>')
def step_impl_(context, projectName):
    assert context.browser.getEnteredProjectName(projectName) is not None

@then(u'I see a <{buttonName}> button in the sidebar')
def step_impl_(context, buttonName):
    assert context.browser.getSidebarItem(buttonName) is not None


@when(u'I click the <{buttonName}> button in the sidebar')
def step_impl_(context, buttonName):
    sidebarItem = context.browser.getSidebarItem(buttonName)
    sidebarItem.click()

@then(u'I cannot see a <{buttonName}> button in the sidebar')
def step_impl_(context, buttonName):
    sleep(2)
    assert context.browser.isSidebarItemExist(buttonName) is False


@then(u'I see a loading animation')
def step_impl(context):
    assert context.browser.isLoadingAnimationShowing() is True
    # raise NotImplementedError(u'STEP: Then I see a chart with title <Team>')

@then(u'The loading animation disappear')
def step_impl(context):
    assert context.browser.isLoadingAnimationDisappear() is True

@then(u'I see a <{chartType}> chart with title <{title}>')
def step_impl(context, chartType, title):
    assert context.browser.isGithubChartExist(chartType, title) is True

@then(u'I see a dropdown with default value <{value}>')
def step_impl(context, value):
    assert context.browser.isDropdownWithValueExist(value) is True
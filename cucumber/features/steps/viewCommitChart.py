from behave import given, when, then


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


@when(u'I enter the dashboard page of the <{projectName}> project')
def step_impl_enter(context, projectName):
    context.browser.enterProjectDashboardPage(projectName)
    # raise NotImplementedError(u'STEP: When I enter the commit page of the PVS-springboot project')

@then(u'I see a loading animation')
def step_impl(context):
    assert context.browser.isLoadingAnimationShowing is True
    # raise NotImplementedError(u'STEP: Then I see a loading animation')


@then(u'the loading animation disappear')
def step_impl(context):
    assert context.browser.isLoadingAnimationShowing is False
    # raise NotImplementedError(u'STEP: Then the loading animation disappear')

@then(u'I see project name with <{projectName}>')
def step_impl_(context, projectName):
    assert context.browser.getProjectCard(projectName) is not None

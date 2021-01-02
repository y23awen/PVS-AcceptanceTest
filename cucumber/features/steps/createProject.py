from behave import given, when, then

@given(u'I\'m on the select project page')
def step_impl(context):
    pass


@when(u'I click the create project card')
def step_impl(context):
    context.browser.clickCreateProjectCard()

@when(u'I fill project name as <{projectName}>')
def step_impl(context, projectName):
    context.browser.inputProjectName(projectName)


@when(u'I fill github url as <{githubUrl}>')
def step_impl(context, githubUrl):
    context.browser.inputGithubRepositoryUrl(githubUrl)


@when(u'I fill sonarqube url as <{sonarUrl}>')
def step_impl(context, sonarUrl):
    context.browser.inputSonarRepositoryUrl(sonarUrl)



@when(u'I click the create button')
def step_impl(context):
    context.browser.clickCreateProjectButton()


@then(u'I should see the project name as <{projectName}> I just created')
def step_impl(context, projectName):
    assert context.browser.getProjectCard(projectName) is not None

@then(u'I should see the alert with message <{errorMessage}> and I accept it')
def step_impl(context, errorMessage):
    context.browser.acceptInputErrorAlert(errorMessage)
  

@then(u'I should see the alert and I accept it')
def step_impl(context):
    context.browser.acceptInputErrorAlertWithoutCheckingMessage()
  
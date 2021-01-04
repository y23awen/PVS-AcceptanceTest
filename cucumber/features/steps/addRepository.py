from behave import given, when, then

@given(u'I click the add repository icon on <{projectName}> project card')
@when(u'I click the add repository icon on <{projectName}> project card')
def step_impl(context, projectName):
    context.browser.clickAddRepositoryButton(projectName)

@given(u'I fill sonarqube url as <{repositoryUrl}> to add repository')
@when(u'I fill sonarqube url as <{repositoryUrl}> to add repository')
def step_impl(context, repositoryUrl):
    context.browser.fillAddRepositoryUrl(repositoryUrl)

@given(u'I click the add repository create button')
@when(u'I click the add repository create button')
def step_impl(context):
    context.browser.clickAddRepositoryCreateButton()    

@given(u'I should see the sonar icon on <{projectName}> project card')
@then(u'I should see the sonar icon on <{projectName}> project card')
def step_impl(context, projectName):
    assert context.browser.isSonarIconExist(projectName) is True
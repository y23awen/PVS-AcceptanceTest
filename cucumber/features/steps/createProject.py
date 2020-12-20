from behave import given, when, then

@given(u'I\'m on the select project page')
def step_impl(context):
    pass
    # context.browser.enterSelectProjectPage()
    # raise NotImplementedError(u'STEP: Given I\'m on the select project page')


@when(u'I click the create project card')
def step_impl(context):
    context.browser.clickCreateProjectCard()
    # raise NotImplementedError(u'STEP: When I click the add project card')


@when(u'I fill project name as <{projectName}>')
def step_impl(context, projectName):
    context.browser.inputProjectName(projectName)
    # raise NotImplementedError(u'STEP: When I fill project name as <projectName>')


@when(u'I fill url as <{url}>')
def step_impl(context, url):
    context.browser.inputProjectUrl(url)
    # raise NotImplementedError(u'STEP: When I fill url as <url>')


@when(u'I click the create button')
def step_impl(context):
    context.browser.clickCreateProjectButton()
    # raise NotImplementedError(u'STEP: When I click the create button')


@then(u'I should see the project I just created')
def step_impl(context):
    assert context.browser.getProjectCard('react') is not None
    # raise NotImplementedError(u'STEP: Then I should see the project I just created')
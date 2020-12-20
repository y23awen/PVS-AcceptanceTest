from behave import given, when, then

@given(u'I have added a project {projectName} with github repository url {url}')
def step_impl_add(context, projectName, url):
    context.browser.addProject(projectName, url)
    # raise NotImplementedError(u'I have added a project {projectName} with github repository url {url}')


@when(u'I enter the commit page of the {projectName} project')
def step_impl_enter(context, projectName):
    context.browser.enterProject(projectName)
    # raise NotImplementedError(u'STEP: When I enter the commit page of the PVS-springboot project')

@then(u'I see a loading animation')
def step_impl(context):
    assert context.browser.isLoadingAnimationShowing is True
    # raise NotImplementedError(u'STEP: Then I see a loading animation')


@then(u'the loading animation disappear')
def step_impl(context):
    assert context.browser.isLoadingAnimationShowing is False
    # raise NotImplementedError(u'STEP: Then the loading animation disappear')

@then(u'I see project name with {projectName}')
def step_impl_(context, projectName):
    raise NotImplementedError(u'STEP: Then I see project name with PVS-react')


from behave import given, when, then
from viewCommitChartImpl import ViewCommitChartImpl


@given(u'I open the browser')
def step_impl(context):
    context.browser = ViewCommitChartImpl()
    # raise NotImplementedError(u'STEP: Given I open the browser')


@given(u'I go to PVS')
def step_impl(context):
    context.browser.openPVS()
    # raise NotImplementedError(u'STEP: Given I go to PVS')


@given(u'I log in')
def step_impl(context):
    print('log in')
    # raise NotImplementedError(u'STEP: Given I log in')

@given(u'I have added a project {projectName} with github repository url {url}')
def step_impl_add(context, projectName, url):
    # controller = ViewCommitChartImpl()
    # controller.openPVS()
    # controller.addProject(projectName, url)
    # viewCommitChartImpl.addProject(projectName, url)
    # context.browser.openPVS()
    context.browser.addProject(projectName, url)

@when(u'I enter the commit page of the {projectName} project')
def step_impl_enter(context, projectName):
    raise NotImplementedError(u'STEP: When I enter the commit page of the PVS-springboot project')

@then(u'I see project name with {projectName}')
def step_impl_(context, projectName):
    raise NotImplementedError(u'STEP: Then I see project name with PVS-react')


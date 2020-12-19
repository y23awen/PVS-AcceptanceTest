from behave import given, when, then
from viewCommitChartImpl import viewCommitChartImpl


@given(u'I have added a project {projectName} with github repository url {url}')
def step_impl_add(context, projectName, url):
    viewCommitChartImpl.addProject(projectName, url)

@when(u'I enter the commit page of the {projectName} project')
def step_impl_enter(context, projectName):
    raise NotImplementedError(u'STEP: When I enter the commit page of the PVS-springboot project')

@then(u'I see project name with {projectName}')
def step_impl_(context, projectName):
    raise NotImplementedError(u'STEP: Then I see project name with PVS-react')


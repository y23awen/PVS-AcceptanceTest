from behave import given, when, then
from time import sleep

@then(u'I see the chart title <{title}>, the number of SonarQube type, and the <{chartType}> chart')
def step_impl(context, title, chartType):
    assert context.browser.isSonarChartExist(chartType, title) is True
    assert context.browser.isNumberExist() is True

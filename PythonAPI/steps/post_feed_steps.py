from behave import given, when, then



@given(u'I am on the Login Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the Login Page')
    context.driver.get(url)



@when(u'I type in my Username')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I type in my Username')
    context.post_feed_home.get username.send_keys(string)


@when(u'I enter my Password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my Password')


@when(u'I click Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Login')


@when(u'I am redirected to my Profile Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I am redirected to my Profile Page')


@when(u'I accept the alert')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I accept the alert')


@then(u'I can view the Post Feed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can view the Post Feed')


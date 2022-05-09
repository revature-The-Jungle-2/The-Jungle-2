from behave import given, when, then


@given(u'I am on the Login Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the Login Page')


@when(u'I enter my Username')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my Username')


@when(u'I enter my Password')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I enter my Password')


@when(u'I click Login')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Login')


@then(u'I can see posts in my feed')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can see posts in my feed')


@given(u'I am on the Visit Profile Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the Profile Page')


@when(u'I click on the "Search for Friends" button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the "Search for Friends" button')


@then(u'I can view the Post Feed for my friends')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I can view the Post Feed for my friends')


@given(u'I am on the Profile Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the Profile Page')


@when(u'I input post id')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input post id')


@when(u'I click Delete Post')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Delete Post')


@then(u'My post id deleted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then My post id deleted')

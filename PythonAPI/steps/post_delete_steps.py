from behave import given, when, then

@given(u'I am on the Profile Page')
def step_impl(context):
    raise NotImplementedError(u'STEP: I am on the Profile Page')

@when(u'I input post id')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I input post id')


@when(u'I click Delete Post')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click Delete Post')


@then(u'My post id is deleted')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then My post id deleted')

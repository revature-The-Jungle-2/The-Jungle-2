from behave import given, when, then




@when(u'click on the Groups on the side bar')
def step_impl(context):
    context.join_group.groups().click()



@when(u'I select the group I want to join')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I select the group I want to join')


@when(u'I get into the individual group page')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I get into the individual group page')


@when(u'I click on the join group button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I click on the join group button')


@then(u'I get a message joined the group successfully')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I get a message joined the group successfully')
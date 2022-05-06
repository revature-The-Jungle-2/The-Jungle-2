




@given(u'I am on the Visit Profile Page')
def step_impl(context):
  context.driver.get(C:\Users\skinn\OneDrive\Desktop\The-Jungle-2\FrontEnd\visitprofilepage\visit-profile-page.html)


@when(u'I click on the "Search for Friends" button')
def step_impl(context):
    context.view_profile_page(searchInputBox).click()


@then(u'I should be re-directed to the View Post Feed webpage')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then I should be re-directed to the View Post Feed webpage')



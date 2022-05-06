# Branching
- From Main, there are two branches - Java Master (Java) and Python Master (pythonMaster).
- Project roles will parallel the branching structure
- For each language a team lead/scrum master will delegate modules to individual team members and have them develop each layer of tests to get the full stack experience for each feature/module
- Main should only be committed to for documentation edits or during the final merging for the presentation. 
- Team members branch from and merge to their respective Master branch to ensure that there are no merge conflicts with each individual language before merging into Main. 
- It should be clear at a glance either A) who is working on that branch and/or B) what feature the branch is for.
- Each branch will have a devoted pipeline to try and isolate defects by languages and allow for each language to independently perform the entire testing lifecycle for each module.  These pipelines will be set up by the co-leads for the entire organization/repository who will work with the specific team leads/scrum masters to outline acceptance criteria and pass along the appropriate pipeline specific details (database credentials for unit testing or port information for the respective ec2 instance for example) needed to standup the overall application.
- Each member will merge to their respective language branch and will have their respective branch merged to main during the daily standup.

# General Links
Link to Working RTM : https://docs.google.com/spreadsheets/d/11Wd62-HARALNNptBiyKsMwXIYKXT7Z_LJ7mNnJBOjFo/edit?usp=sharing
- When the code is frozen, the RTM will be downloaded and added to the in-repo documentation.

# Best Practices

- Development should be test driven:
- Each module in each tier should have a separate suite of unit tests consisting of at least:
	- Data layer methods:
	one positive test
	- Service layer methods:
	one positive test
	all business logic must have negative tests (error catching)
	mocking and stubbing should be used where appropriate
	- API methods:
	must all have a positive test using Postman
	must have negative tests for all possible errors for each type of request
    - End to end testing:
    We used Cucumber with JUnit and Selenium to execute our end-to-end tests.
    These tests should follow acceptance criteria outlined in a test plan and should include a "happy" path and a "sad" path.

The usual.
Get some sleep.
Take breaks.
Communicate with your teammates.
Pet cats and touch grass.

- Make sure to commit your branches before logging off so nothing is lost!
- If you have merge conflicts that you cannot figure out, reach out ASAP.



from locust import HttpLocust, TaskSet, task, between
from locustio.jira_http_actions import *
from util.conf import JIRA_SETTINGS

init_logger()


class JiraBehavior(TaskSet):

    def on_start(self):
        login_and_view_dashboard(self)

    def login_and_view_dashboard(self):
        login_and_view_dashboard(self)

    @task(1)
    def create_issue(self):
        create_issue(self)

    @task(3)
    def search_jql(self):
        search_jql(self)

    @task(9)
    def view_issue(self):
        view_issue(self)

    @task(1)
    def view_project_sumamry(self):
        view_project_summary(self)

    # view_dashboard

    @task(1)
    def edit_issue(self):
        edit_issue(self)

    # add comment
    # browse projects
    # view_kanban_boards
    # view_scrum_boards
    # view_backlog
    # browse_boards


class JiraUser(HttpLocust):
    host = JIRA_SETTINGS.server_url
    task_set = JiraBehavior
    wait_time = between(2, 5)

from pypom import Page
from .locators import ProjectsPageLocators


class ProjectsListPage(Page):
    URL_TEMPLATE = '/admin/projects/'

    def should_be_projects_url(self):
        assert self.driver.is_element_present_by_css(ProjectsPageLocators.PROJECTS_GRID_CSS, wait_time=5), \
            'Should be header, but not'
        assert 'projects' in self.driver.url, 'Should be projects url, but not'

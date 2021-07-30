from .base_page import BasePage
from .locators import ProjectsPageLocators


class ProjectsListPage(BasePage):
    URL_TEMPLATE = '/admin/projects/'

    def should_be_projects_url(self):
        assert self.driver.is_element_present_by_css(ProjectsPageLocators.PROJECTS_GRID_CSS, 5), \
            'Should be header, but not'
        assert 'projects' in self.driver.url, 'Should be projects url, but not'

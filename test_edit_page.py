def test_changed_manager_name(pr_edit_page):
    pr_edit_page.should_be_changed_manager_name()


def test_changed_project_manager_name(pr_edit_page):
    pr_edit_page.should_be_changed_project_manager_name()


def test_changed_url_template(pr_edit_page, config):
    pr_edit_page.should_be_changed_url_template(config['pr']['template_url'])


def test_changed_inner_name(pr_edit_page):
    pr_edit_page.should_be_changed_inner_name()


def test_changed_name(pr_edit_page):
    pr_edit_page.should_be_changed_name()


def test_changed_type(pr_edit_page):
    pr_edit_page.should_be_changed_type()


def test_changed_sync(pr_edit_page):
    pr_edit_page.should_be_changed_sync()


def test_changed_description(pr_edit_page):
    pr_edit_page.should_be_changed_description()


def test_changed_comments(pr_edit_page):
    pr_edit_page.should_be_changed_comments()


def test_changed_device_type(pr_edit_page):
    pr_edit_page.should_be_changed_device_type()


def test_changed_device_type_show(pr_edit_page):
    pr_edit_page.should_be_changed_device_type_show()


def test_changed_multilink(pr_edit_page):
    pr_edit_page.should_be_changed_multilink()


def test_changed_category(pr_edit_page):
    pr_edit_page.should_be_changed_category()

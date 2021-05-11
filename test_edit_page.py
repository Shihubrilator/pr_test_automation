def test_changed_manager_name(pr_edit_page, config):
    pr_edit_page.should_be_changed_manager_name(config)


def test_changed_project_manager_name(pr_edit_page, config):
    pr_edit_page.should_be_changed_project_manager_name(config)


def test_changed_url_template(pr_edit_page, config):
    pr_edit_page.should_be_changed_url_template(config)


def test_changed_inner_name(pr_edit_page, config):
    pr_edit_page.should_be_changed_inner_name(config)


def test_changed_name(pr_edit_page, config):
    pr_edit_page.should_be_changed_name(config)


def test_changed_type(pr_edit_page, config):
    pr_edit_page.should_be_changed_type(config)


def test_changed_sync(pr_edit_page, config):
    pr_edit_page.should_be_changed_sync(config)


def test_changed_description(pr_edit_page, config):
    pr_edit_page.should_be_changed_description(config)


def test_changed_comments(pr_edit_page, config):
    pr_edit_page.should_be_changed_comments(config)


def test_changed_device_type(pr_edit_page, config):
    pr_edit_page.should_be_changed_device_type(config)


def test_changed_device_type_show(pr_edit_page, config):
    pr_edit_page.should_be_changed_device_type_show(config)


def test_changed_multilink(pr_edit_page, config):
    pr_edit_page.should_be_changed_multilink(config)


def test_changed_category(pr_edit_page, config):
    pr_edit_page.should_be_changed_category(config)


def test_cancel_status_changes(pr_edit_page, config):
    pr_edit_page.should_be_not_changed_status_time(config)

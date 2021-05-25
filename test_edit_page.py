def test_changed_manager_name(pr_edit_page, config):
    pr_edit_page.change_manager(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_manager_name(config)


def test_changed_project_manager_name(pr_edit_page, config):
    pr_edit_page.change_project_manager(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_project_manager_name(config)


def test_changed_url_template(pr_edit_page, config):
    pr_edit_page.change_template_url(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_url_template(config)


def test_changed_inner_name(pr_edit_page, config):
    pr_edit_page.change_inner_name(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_inner_name(config)


def test_changed_name(pr_edit_page, config):
    pr_edit_page.change_name(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_name(config)


def test_changed_type(pr_edit_page, config):
    pr_edit_page.change_type(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_type(config)


def test_changed_sync(pr_edit_page, config):
    pr_edit_page.change_sync(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_sync(config)


def test_changed_description(pr_edit_page, config):
    pr_edit_page.change_description(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_description(config)


def test_changed_comments(pr_edit_page, config):
    pr_edit_page.change_comments(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_comments(config)


def test_changed_device_type(pr_edit_page, config):
    pr_edit_page.change_device_type(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_device_type(config)


def test_changed_device_type_show(pr_edit_page, config):
    pr_edit_page.change_device_type_show(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_device_type_show(config)


def test_changed_multilink(pr_edit_page, config):
    pr_edit_page.change_multilinks(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_multilink(config)


def test_changed_category(pr_edit_page, config):
    pr_edit_page.change_category(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_category(config)


def test_cancel_status_changes(pr_edit_page, config):
    pr_edit_page.change_status_time_and_cancel(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_not_changed_status_time(config)


def test_status_changes(pr_edit_page, config):
    pr_edit_page.change_status_time(config)
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_status_time(config)


def test_create_collector_template(pr_edit_page, config):
    pr_edit_page.add_collector_template(config)
    pr_edit_page.should_be_collector_template_url()

def test_changed_manager(pr_edit_page, config):
    pr_edit_page.change_manager(4, config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_manager_name(config['pr']['default_settings']['manager'],
                                                config['pr']['xpctd_settings']['manager'],
                                                config['pr']['wait_time'])


def test_changed_project_manager(pr_edit_page, config):
    pr_edit_page.change_project_manager(4, config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_project_manager_name(config['pr']['default_settings']['project_manager'],
                                                        config['pr']['xpctd_settings']['project_manager'],
                                                        config['pr']['wait_time'])


def test_changed_url_template(pr_edit_page, config):
    pr_edit_page.change_template_url(config['pr']['xpctd_settings']['url_template'], config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_url_template(config['pr']['xpctd_settings']['url_template'],
                                                config['pr']['wait_time'])


def test_changed_inner_name(pr_edit_page, config):
    pr_edit_page.change_inner_name(config['pr']['xpctd_settings']['inner_name'], config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_inner_name(config['pr']['xpctd_settings']['inner_name'], config['pr']['wait_time'])


def test_changed_name(pr_edit_page, config):
    pr_edit_page.change_name(config['pr']['xpctd_settings']['name'], config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_name(config['pr']['xpctd_settings']['name'], config['pr']['wait_time'])


def test_changed_type(pr_edit_page, config):
    pr_edit_page.change_type(2, config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_type(config['pr']['xpctd_settings']['type'], config['pr']['wait_time'])


def test_changed_sync(pr_edit_page, config):
    pr_edit_page.change_sync(config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_sync(config['pr']['wait_time'])


def test_changed_description(pr_edit_page, config):
    pr_edit_page.change_description(config['pr']['xpctd_settings']['description'], config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_description(config['pr']['xpctd_settings']['description'], config['pr']['wait_time'])


def test_changed_comments(pr_edit_page, config):
    pr_edit_page.change_comments(config['pr']['xpctd_settings']['note'], config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_comments(config['pr']['xpctd_settings']['note'], config['pr']['wait_time'])


def test_changed_device_type(pr_edit_page, config):
    pr_edit_page.change_device_type(1, config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_device_type(config['pr']['default_settings']['device_type_text'],
                                               config['pr']['xpctd_settings']['device_type_text'],
                                               config['pr']['wait_time'])


def test_changed_device_type_show(pr_edit_page, config):
    pr_edit_page.change_device_type_show(2, config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_device_type_show(config['pr']['default_settings']['device_type_show_text'],
                                                    config['pr']['xpctd_settings']['device_type_show_text'],
                                                    config['pr']['wait_time'])


def test_changed_multilink(pr_edit_page, config):
    pr_edit_page.change_multilinks(config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_multilink(config['pr']['wait_time'])


def test_changed_category(pr_edit_page, config):
    pr_edit_page.change_category(config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_category(config['pr']['xpctd_settings']['category'], config['pr']['wait_time'])


def test_cancel_status_changes(pr_edit_page, config):
    pr_edit_page.change_status_time_and_cancel('20', config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_not_be_changed_status_time('10', config['pr']['wait_time'])


def test_status_changes(pr_edit_page, config):
    pr_edit_page.change_status_time('20', config['pr']['wait_time'])
    pr_edit_page.save_project_changes()
    pr_edit_page.reload()
    pr_edit_page.should_be_changed_status_time('20', config['pr']['wait_time'])


def test_create_collector_template(pr_edit_page, config):
    pr_edit_page.add_collector_template(config['pr']['xpctd_c_tmplt_settings']['name'], config['pr']['wait_time'])
    pr_edit_page.should_be_collector_template_url()

def test_change_collector_template_name(pr_collector_template_page, config):
    pr_collector_template_page.change_name(config['pr']['xpctd_c_tmplt_settings']['name'], config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_name(config['pr']['xpctd_c_tmplt_settings']['name'],
                                                      config['pr']['wait_time'])


def test_change_collector_template_panel(pr_collector_template_page, config, pr_headers):
    pr_collector_template_page.change_panel(4, config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_panel(config['pr']['default_c_template_settings']['panel'],
                                                       config['pr']['xpctd_c_tmplt_settings']['panel'],
                                                       config['pr']['wait_time'])
    pr_collector_template_page.set_default_c_template_settings(pr_headers, config)
    pr_collector_template_page.reload()


def test_change_collector_template_invitation(pr_collector_template_page, config):
    pr_collector_template_page.change_invitation(1, config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_invitation(config['pr']['default_c_template_settings']['invitation'],
                                                            config['pr']['xpctd_c_tmplt_settings']['invitation'],
                                                            config['pr']['wait_time'])


def test_change_collector_template_reminder(pr_collector_template_page, config):
    pr_collector_template_page.change_reminder(1, config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_reminder(config['pr']['default_c_template_settings']['reminder'],
                                                          config['pr']['xpctd_c_tmplt_settings']['reminder'],
                                                          config['pr']['wait_time'])


def test_change_collector_template_autofill(pr_collector_template_page, config):
    pr_collector_template_page.change_autofill(1, config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_autofill(config['pr']['default_c_template_settings']['autofill'],
                                                          config['pr']['xpctd_c_tmplt_settings']['autofill'],
                                                          config['pr']['wait_time'])


def test_change_collector_template_captcha(pr_collector_template_page, config):
    pr_collector_template_page.change_captcha(1, config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_captcha(config['pr']['default_c_template_settings']['captcha'],
                                                         config['pr']['xpctd_c_tmplt_settings']['captcha'],
                                                         config['pr']['wait_time'])


def test_change_collector_template_allowduplicate(pr_collector_template_page, config):
    pr_collector_template_page.change_allowduplicate(config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_allowduplicates(config['pr']['wait_time'])


def test_change_collector_template_reward(pr_collector_template_page, config):
    pr_collector_template_page.change_reward(config['pr']['xpctd_c_tmplt_settings']['reward'],
                                             config['pr']['wait_time'])
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_reward(config['pr']['xpctd_c_tmplt_settings']['reward'],
                                                        config['pr']['wait_time'])

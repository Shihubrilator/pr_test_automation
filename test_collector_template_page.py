def test_change_collector_template_name(pr_collector_template_page, config):
    pr_collector_template_page.change_name(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_name(config)


def test_change_collector_template_panel(pr_collector_template_page, config, pr_headers):
    pr_collector_template_page.change_panel(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_panel(config)
    pr_collector_template_page.set_default_c_template_settings(pr_headers, config)
    pr_collector_template_page.reload()


def test_change_collector_template_invitation(pr_collector_template_page, config):
    pr_collector_template_page.change_invitation(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_invitation(config)


def test_change_collector_template_reminder(pr_collector_template_page, config):
    pr_collector_template_page.change_reminder(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_reminder(config)


def test_change_collector_template_autofill(pr_collector_template_page, config):
    pr_collector_template_page.change_autofill(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_autofill(config)


def test_change_collector_template_captcha(pr_collector_template_page, config):
    pr_collector_template_page.change_captcha(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_captcha(config)


def test_change_collector_template_allowduplicate(pr_collector_template_page, config):
    pr_collector_template_page.change_allowduplicate(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_allowduplicates(config)


def test_change_collector_template_reward(pr_collector_template_page, config):
    pr_collector_template_page.change_reward(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_reward(config)

def test_change_collector_template_name(pr_collector_template_page, config):
    pr_collector_template_page.change_name(config)
    pr_collector_template_page.save_changes()
    pr_collector_template_page.reload()
    pr_collector_template_page.should_be_changed_name(config)

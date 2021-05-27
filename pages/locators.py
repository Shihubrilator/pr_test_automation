class LoginPageLocators:
    LOGIN_EMAIL_ID = "LoginEmail"
    LOGIN_PASSWORD_ID = "LoginPassword"
    LOGIN_BUTTON_CSS = ".btn-success"


class ProjectsPageLocators:
    PROJECTS_GRID_CSS = "div .k-grid"


class EditPageLocators:
    MANAGER_INPUT = "#rw_3_input .rw-widget-input"
    MANAGER_LIST_ITEM = "#rw_3_input li.rw-list-option"
    PROJECT_MANAGER_INPUT = "#rw_4_input .rw-widget-input"
    PROJECT_MANAGER_LIST_ITEM = "#rw_4_input li.rw-list-option"
    DEVICE_TYPE_INPUT = "#rw_5_input .rw-widget-input"
    DEVICE_TYPE_LIST_ITEM = "#rw_5_listbox li.rw-list-option"
    DEVICE_TYPE_SHOW_INPUT = "#rw_6_input .rw-widget-input"
    DEVICE_TYPE_SHOW_LIST_ITEM = "#rw_6_listbox li.rw-list-option"
    URL_TEMPLATE_INPUT = 'textarea[name="SurveyEngineTemplateUrl"]'
    INNER_NAME_INPUT = 'input[name="InnerName"]'
    NAME_INPUT = 'input[name="Name"]'
    TYPE_INPUT = '.form-group:nth-child(5) .inplace-editor .dropdown-toggle'
    TYPE_LIST_ITEM = '.form-group:nth-child(5) .dropdown-menu li'
    SYNC_TOGGLE = '.form-group:nth-child(7) .react-toggle'
    MULTILINKS_TOGGLE = '.form-group:nth-child(14) .react-toggle'
    DESCRIPTION_INPUT = 'textarea[name="SurveyDescription"]'
    COMMENTS_INPUT = 'textarea[name="Notes"]'
    CATEGORY_LIST = '.rw-multiselect button.rw-multiselect-tag-btn'
    CATEGORY_LIST_ITEM = '.rw-multiselect li'
    CATEGORY_LIST_ITEM_SELECTED = '.rw-multiselect li.rw-multiselect-tag'
    COMPLETE_AVERAGE_TIME_CELL = 'div.row.space div.col-md-6:nth-of-type(2) > div > div > h3~div tbody tr:nth-of-type(5) td:nth-of-type(5)'
    COMPLETE_AVERAGE_TIME_INPUT_SHOW = 'div.row.space div.col-md-6:nth-of-type(2) > div > div > h3~div tbody tr:nth-of-type(5) td:nth-of-type(5) span span'
    COMPLETE_AVERAGE_TIME_INPUT = 'div.row.space div.col-md-6:nth-of-type(2) > div > div > h3~div tbody tr:nth-of-type(5) td:nth-of-type(5) input[name=AverageTime]'
    SCREENOUT_AVERAGE_TIME_CELL = 'div.row.space div.col-md-6:nth-of-type(2) > div > div > h3~div tbody tr:nth-of-type(4) td:nth-of-type(5)'
    SCREENOUT_AVERAGE_TIME_INPUT_SHOW = 'div.row.space div.col-md-6:nth-of-type(2) > div > div > h3~div tbody tr:nth-of-type(4) td:nth-of-type(5) span span'
    SCREENOUT_AVERAGE_TIME_INPUT = 'div.row.space div.col-md-6:nth-of-type(2) > div > div > h3~div tbody tr:nth-of-type(4) td:nth-of-type(5) input[name=AverageTime]'
    STATUS_CANCEL_CHANGES = '.js-kendo-button-cancel'
    STATUS_SAVE_CHANGES = '.js-kendo-button-update'
    ADD_COLLECTOR_TEMPLATE_BUTTON = 'h3 + div.btn'
    COLLECTOR_TEMPLATE_NAME_INPUT = 'div.modal-body input'
    COLLECTOR_TEMPLATE_NAME_CONFIRM_BUTTON = 'div.modal-body button.btn-primary'


class CollectorTemplatePageLocators:
    TEMPLATE_NAME_INPUT = '.col-lg-8 input.form-control'
    TEMPLATE_PANEL = 'div#rw_1_input div.rw-input'
    TEMPLATE_PANEL_LIST_ITEM = 'div#rw_1_input li.rw-list-option'
    TEMPLATE_INVITATION = 'div#rw_4_input div.rw-input'
    TEMPLATE_INVITATION_LIST_ITEM = 'div#rw_4_input li.rw-list-option'
    TEMPLATE_REMINDER = 'div#rw_5_input div.rw-input'
    TEMPLATE_REMINDER_LIST_ITEM = 'div#rw_5_input li.rw-list-option'
    TEMPLATE_AUTOFILL = 'div#rw_2_input div.rw-input'
    TEMPLATE_AUTOFILL_LIST_ITEM = 'div#rw_2_input li.rw-list-option'
    TEMPLATE_CAPTCHA = 'div#rw_3_input div.rw-input'
    TEMPLATE_CAPTCHA_LIST_ITEM = 'div#rw_3_input li.rw-list-option'
    TEMPLATE_ALLOWDUPLICATES = 'input[name="AllowDuplicates"]'

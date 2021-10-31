from selenium.webdriver.common.by import By


class BasePageLocators:
    BASE_PAGE_LOADED_LOCATOR = ''


class MainPageLocators:
    LOGIN_ENTRY_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "responseHead-module-button")]')
    LOGIN_LOCATOR = (By.NAME, 'email')
    PASSWORD_LOCATOR = (By.NAME, 'password')
    SUBMIT_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "authForm-module-button")]')


class DashboardPageLocators(BasePageLocators):
    SEGMENTS_LOCATOR = (By.CSS_SELECTOR, '[href="/segments"]')
    DASHBOARD_LOCATOR = (By.CSS_SELECTOR, '[href="/dashboard"]')
    CREATE_COMPANY_LOCATOR = (By.CSS_SELECTOR, '[href="/campaign/new"]')
    CREATE_COMPANY_BUTTON_LOCATOR = (By.XPATH, '//div[contains(@class, "dashboard-module-createButtonWrap")]')
    COMPANY_TITLE_LOCATOR = (By.XPATH, '//a[@title="{}"]')


class CompanyPageLocators(BasePageLocators):
    TRAFFIC_LOCATOR = (By.CLASS_NAME, '_traffic')
    ADD_URL_LOCATOR = (By.CSS_SELECTOR, '[data-gtm-id="ad_url_text"]')
    COMPANY_NAME_LOCATOR = (By.CSS_SELECTOR, '.input_campaign-name input')
    BANNER_LOCATOR = (By.ID, 'patterns_banner_4')
    IMAGE_LOCATOR = (By.CSS_SELECTOR, '[data-test="image_240x400"]')
    IMAGE_SAVE_BUTTON_LOCATOR = (By.CLASS_NAME, 'image-cropper__save')
    CREATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, '.footer__controls-wrap button')


class AudiencePageLocators(BasePageLocators):
    NEW_SEGMENT_LOCATOR = (By.CSS_SELECTOR, '[href="/segments/segments_list/new/"]')
    NEW_SEGMENT_BUTTON_LOCATOR = (By.CLASS_NAME, 'button_submit')
    SEGMENT_TITLE_LOCATOR = (By.XPATH, '//a[@title="{}"]')
    SEGMENT_CROSS_LOCATOR = (By.XPATH, '//a[@title="{}"]/../../following-sibling::div[4]/span')
    SEGMENT_DELETE_LOCATOR = (By.CLASS_NAME, 'button_confirm-remove')


class NewSegmentPageLocators(BasePageLocators):
    SEGMENT_CHECKBOX_LOCATOR = (By.CLASS_NAME, 'adding-segments-source__checkbox')
    SEGMENT_SUBMIT_2_LOCATOR = (By.CSS_SELECTOR, '.adding-segments-modal [data-class-name="Submit"]')
    SEGMENT_INPUT_LOCATOR = (By.CSS_SELECTOR, '.input_create-segment-form input')
    SEGMENT_SUBMIT_1_LOCATOR = (By.CSS_SELECTOR, '.create-segment-form__btn-wrap button')

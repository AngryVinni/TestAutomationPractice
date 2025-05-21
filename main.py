import pytest
from playwright.sync_api import Page, expect, sync_playwright
import time

enter_text_field = '//input[@class ="textinput textInput form-control"]'

def test_enter_text():
         with sync_playwright() as p:
                browser = p.chromium.launch(headless=False)
                page = browser.new_page()
                page.goto("https://www.qa-practice.com/elements/input/simple")
                # You can add more actions/assertions here
                page.fill(enter_text_field, 'Hello, World!')
                # Verify the text was entered   
                expect(page.locator(enter_text_field)).to_have_value('Hello, World!')
                page.locator().click
                
                browser.close()
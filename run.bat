@echo off
behave --tags search --format allure_behave.formatter:AllureFormatter -o Reports/allure-results-search

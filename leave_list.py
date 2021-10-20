from source.pages.base_page import *


driver=launch()


def navigate_leave():
    driver.find_element_by_xpath('//*[@id="menu_leave_viewLeaveModule"]/b').click()
    driver.find_element_by_xpath('//*[@id="calFromDate"]').click()
    month_select=Select(driver.find_element_by_xpath('/html/body/div[3]/div/div/select[1]'))
    month_select.select_by_visible_text("Mar")
    year_select=Select(driver.find_element_by_xpath('/html/body/div[3]/div/div/select[2]'))
    year_select.select_by_visible_text("2015")
    driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[4]/td[2]/a').click()

    driver.find_element_by_xpath('//*[@id="calToDate"]').click()
    month_select1=Select(driver.find_element_by_xpath('/html/body/div[3]/div/div/select[1]'))
    month_select1.select_by_visible_text("May")


    year_select=Select(driver.find_element_by_xpath('/html/body/div[3]/div/div/select[2]'))
    year_select.select_by_visible_text("2016")

    driver.find_element_by_xpath('/html/body/div[3]/table/tbody/tr[3]/td[6]/a').click()


    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[3]/div/input[1]").click()

    driver.find_element_by_id("leaveList_txtEmployee_empName").send_keys("Ananya Dash")
    drop_down=Select(driver.find_element_by_id("leaveList_cmbSubunit"))
    drop_down.select_by_index(0)

    driver.find_element_by_id("btnSearch").click()
if __name__ == "__main__":
    navigate_leave()








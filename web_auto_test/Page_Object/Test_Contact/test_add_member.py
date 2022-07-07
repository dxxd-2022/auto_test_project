from web_test.Page_Object.Po.main_page import MainPage


class TestAddMember:
    def setup_class(self):
        self.main=MainPage()
    def teardown_class(self):
        pass
    def test_add_member(self):
        result=self.main.goto_contact().click_add_member().edit_member().get_member_name()
        assert result
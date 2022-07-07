from auto_test_project.API_Test.case.tag_api import Tag


class TestTag:
    def setup_class(self):
        self.tag=Tag()
    def test_get_tag(self):#查询标签列表测试用例
        #print(json.dumps(self.tag.get_tag().json(),indent=3))#json.dumps----以json格式进行打印展示,indent代表缩进
        r=self.tag.get_tag()
        assert r.json().get("errcode")==0 #以上为一个简单的冒烟测试
    def test_add_tag(self,get_unique_name):#增加标签测试用例
        #tag_name=str(time.time())+threading.currentThread().name#获取时间戳,通过+threading.currentThread().name解决多线程的问题
        #在并行用例的时候，tag_name=time.time()代码会出现问题
        #new_tag=self.tag.add_tag(tag_name).json()
        new_tag=self.tag.add_tag(get_unique_name).json()
        assert new_tag.get('errcode') == 0
        #tag_list=self.tag.get_tag().get("taglist")
        assert self.tag.is_in_taglist(new_tag.get("tagid"))
        # assert new_tag.json().get("tagid") in tag_list
        # assert self.tag.get_tag()
    def test_delete_tag(self,get_unique_name):#删除标签用例
        new_tag=self.tag.add_tag(get_unique_name).json()
        assert self.tag.delete_tag(new_tag.get("tagid")).json().get("errcode")==0
    def test_update_tag(self,get_unique_name):#更新标签内容测试用例
        new_tag=self.tag.add_tag(get_unique_name).json()
        assert self.tag.update_tag(new_tag.get("tagid"),get_unique_name).json().get("errcode")==0



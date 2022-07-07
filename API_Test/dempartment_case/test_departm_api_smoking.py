import json
import threading
import time

import pytest

from auto_test_project.API_Test.dempartment_case.departm_api import DepartmApi

def get_random_departmname():#如果对于依赖某个接口的时候，同步执行测试类中的所有用例，部份依赖用例会报错，是因为add的时候生成的名称
    departm_name=str(time.time())+threading.currentThread().name
    return departm_name
class TestDepartmApi:
    def setup_class(self):
        self.object=DepartmApi()
    @pytest.mark.get
    def test_get_departm_list(self):
        r=self.object.get_departm_list()
        print(json.dumps(r.json(),indent=2))
    @pytest.mark.add
    def test_add_departm(self,get_unique_departmname):
        r=self.object.add_departm(get_unique_departmname)
        print(r.json())
        assert r.json().get("errcode")==0
    @pytest.mark.delete
    def test_delete_departm(self):
        new_depart=self.object.add_departm(get_random_departmname())
        new_depart_id=new_depart.json().get("id")           #删除之前新增构造删除部门数据
        #print(new_depart_id)
        r=self.object.delete_departm(new_depart_id)         #调用删除部门接口
        assert r.json().get("errcode")==0                   #断言状态码
    @pytest.mark.updata
    #def test_updata_departm(self,get_unique_departmname):
    def test_updata_departm(self):
        #这里如果更新和删除同时依赖add方法的时候且在跑整个测试类的时候，会因为删除和更新会同时调用add方法，从而导用例数据冲突
        # 解决方式：不要用fixture,直接在测试用例上面写个方法调用即可。
        new_depart = self.object.add_departm(get_random_departmname())
        new_depart_id = new_depart.json().get("id")         #更新之前新增部门数据（部门id）
        r=self.object.updata_departm(new_depart_id)
        #print(r.json())
        assert r.json().get("errmsg")=="updated"
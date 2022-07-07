import requests

from auto_test_project.API_Test.case.base_api import BaseApi


class Tag(BaseApi):#标签的增删改查接口

    """
    1、测试接口放在类中，可以让其他方法进行复用
    2、便于统一处理，重复逻辑可以提取复用
    3、建议把必填参数放到函数的参数中，非必填的参数放到kwargs中
    4、把base url封装到父类中
    """
    def add_tag(self,tagname,**kwargs):
        """
        添加标签
        :param tagname:标签名
        :param kwargs:（tagid,默认会自动生成）
        :return:
        """
        datas = {
            "tagname": tagname
            }
        datas.update(kwargs)#把其他非必填数据更新到数据中
        r = requests.post(self.BASE_URL+f"tag/create?access_token={self.token}", json=datas)  # 创建标签接口
        return r
    def delete_tag(self,tagid):
        """
        删除tag
        :param tagid: 标签id
        :return:
        """
        r=requests.get(self.BASE_URL+f"tag/delete?access_token={self.token}&tagid={tagid}")
        return r
    def update_tag(self,tagid,tagname):
        datas={
   "tagid": tagid,
   "tagname": tagname
}
        r=requests.post(self.BASE_URL+f"tag/update?access_token={self.token}",json=datas)
        return r
    def get_tag(self):
        r=requests.get(self.BASE_URL+f"tag/list?access_token={self.token}")#获取标签列表
        return r
    def is_in_taglist(self,tag_id):
        """
        判断tag_id是否在taglist中
        :param tag_id:
        :return:
        """
        tag_list=self.get_tag().json().get("taglist")
        for tag in tag_list:
            if tag_id==tag.get("tagid"):
                return True
        return False
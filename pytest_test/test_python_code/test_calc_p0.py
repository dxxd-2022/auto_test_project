import pytest
import yaml

def get_calc_datas():
    with open('./tmp_calc_datas_p0.yml')as f:
        calc_datas=yaml.safe_load(f)
        return calc_datas
def test_get_calc_datas():
    print(get_calc_datas()['add']['ids'])

class TestCalculator:
    @pytest.mark.parametrize('a,b,expect',get_calc_datas()['add']['datas'],ids=get_calc_datas()['add']['ids'])
    @pytest.mark.p0
    def test_add_p0(self,get_calc_object,a,b,expect):
        assert get_calc_object.add(a,b)==expect

    @pytest.mark.parametrize('a,b,expect', get_calc_datas()['div']['datas'], ids=get_calc_datas()['div']['ids'])
    @pytest.mark.p0
    def test_div(self, a, b, expect, get_calc_object):
        assert get_calc_object.div(a, b) == expect
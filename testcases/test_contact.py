from page.app import App
import  pytest

class TestContact:

    def setup(self):
        self.app = App()   #不太懂这里为啥可以直接用这个构造方法，App类中好像没有定义，难道是默认的？
        self.main = self.app.start().main()   #启动app并跳转到main页

    @pytest.mark.parametrize('name',["zhangsan","lishi","wangwu"])
    def test_addcontact(self,name):
        self.name = name
        self.main.goto_addresslist().add_member().addmember_by_manual().input_name(name).input_gender().input_phonenumber().click_save()


if __name__ =='__main__':
    pytest.main(["-v", "-s", "test_contact.py"])

from flask_script import Manager, Server
from main import app

manager = Manager(app)

#创建一个自定义命令绑定Server方法
manager.add_command('start', Server())

'''
make_shell_context函数会创建一个Python命令行
并在应用上下文中执行
返回的字典会告诉Flask-Script在命令行打开时进行一些默认的导入工作
'''
@manager.shell
def make_shell_context():
    return dict(app=app)

if __name__ == '__main__':
    manager.run()
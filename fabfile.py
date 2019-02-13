from fabric.api import env, run
from fabric.operations import sudo

#xxxxxx = you git repository
GIT_REPO = "xxxxxxxxx"
#xxxxxxx = you host username
env.user = 'xxxxxxx'
#xxxxxxxx = you host password
env.password = 'xxxxxxxx'

# 填写你自己的主机对应的域名
env.hosts = ['lionrock.info']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'

def deploy():
    #填写自己的项目根目录
    source_folder = '/home/tssdhj/sites/blog/LionRock'

    run('cd %s && git pull' % source_folder)
    run("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('service restart gunicorn')
    sudo('service nginx reload')
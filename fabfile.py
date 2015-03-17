from fabric.api import *

deploy_to = '/var/www/vhosts/wiki'
repository = 'https://github.com/vectorxenon/wiki.yagni.jp.git'

@task
@runs_once
def prod():
    environment = 'prod'
    env.hosts = ['yagni.jp']


@task
@runs_once
def vagrant():
    environment = 'vagrant'
    env.hosts = ['127.0.0.1']
    env.port = 2222
    env.user = 'vagrant'
    env.key_filename = '~/workspace/yagni.jp/.vagrant/machines/m1/virtualbox/private_key'


@task
@runs_once
def deploy():
    exists = run('if test -d %s/current; then echo "true"; fi' % deploy_to, quiet=True)
    with cd(deploy_to):
        if exists:
            run('cd current && git pull -p')
        else:
            run('git clone %s current' % repository)


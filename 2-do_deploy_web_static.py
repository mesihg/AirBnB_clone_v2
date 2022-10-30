#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers """

from os.path import exists
from fabric.api import put, run, env

env.hosts = ['44.210.69.40', '100.25.135.77']


def do_deploy(archive_path):
    """
    copy archive_path file from local to remote webservers
    """

    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("sudo mkdir -p /data/web_static/releases/{}".format(file_name))

        run("sudo tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
            .format(file_name, file_name))

        run('sudo rm -rf /tmp/{}.tgz'.format(file_name))

        run(('sudo mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/')
            .format(file_name, file_name))

        run('sudo rm -rf /data/web_static/releases/{}/web_static'
            .format(file_name))

        run('sudo rm -rf /data/web_static/current')

        run(('sudo ln -s /data/web_static/releases/{}/' +
            ' /data/web_static/current')
            .format(file_name))
        return True
    except Exception:
        return False

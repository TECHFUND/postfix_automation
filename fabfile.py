from fabric.api import sudo, env, run, roles, cd, put, local
from fabric.contrib import project, console
import os
import os.path

def all():
    install_postfix()
    set_postfix_mainconf()
    set_auth_daemon()
    stop_old_mailer()
    choose_postfix()
    run_postfix()
    create_info_user()
    set_mail_proxy()

def install_postfix():
    sudo("yum update -y")
    sudo("yum install postfix expect -y")

def set_postfix_mainconf():
    put("main.cf", "/etc/postfix/main.cf", use_sudo=True)
    sudo("chown -R root:root /etc/postfix/main.cf")
    sudo("chmod g-w /etc/postfix/./main.cf")

def set_auth_daemon():
    sudo("/etc/rc.d/init.d/saslauthd start")
    sudo("chkconfig saslauthd on")

def stop_old_mailer():
    sudo("/etc/rc.d/init.d/sendmail stop")
    sudo("chkconfig sendmail off")

def choose_postfix():
    put("let_use_postfix.sh", "let_use_postfix.sh", use_sudo=True)
    sudo("expect let_use_postfix.sh")

def run_postfix():
    sudo("/etc/rc.d/init.d/postfix start")
    sudo("chkconfig postfix on")

def create_info_user():
    sudo("mkdir -p /etc/skel/Maildir/{new,cur,tmp}")
    sudo("chmod -R 700 /etc/skel/Maildir/")
    sudo("useradd info", warn_only=True)
    put("set_password_to_user.sh", "set_password_to_user.sh", use_sudo=True)
    sudo("expect set_password_to_user.sh")

def set_mail_proxy():
    put("aliases", "/etc/aliases", use_sudo=True)
    sudo("chown root:root /etc/aliases")
    sudo("chmod 640 /etc/aliases")
    sudo("newaliases")

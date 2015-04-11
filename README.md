# postfix automation

1.`sudo pip install fabric`する

2.main.cfとaliasesの中身を書き換える

3.set_password_to_user.sh にubuntuのinfoユーザーのパスワードを書いてあげる

4.`fab -u ec2-user -i ~/.pem/taskall.pem -H ec2-00-00-00-00.ap-northeast-1.compute.amazonaws.com all`

5.終わったら info@hoge.com にメールを送って転送設定を確認する

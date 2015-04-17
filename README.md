# postfix automation

1.`sudo pip install fabric`する

2.main.cfとaliasesの中身を書き換える

3.set_password_to_user.sh にubuntuのinfoユーザーのパスワードを書いてあげる

4.`fab -u ec2-user -i ~/.pem/taskall.pem -H ec2-00-00-00-00.ap-northeast-1.compute.amazonaws.com all`

5.終わったら info@hoge.com にメールを送って転送設定を確認する


# メールセキュリティについて

25番ポートには`sudo tcpdump src 25`すれば分かる通り、膨大な迷惑メールが届いている
現在確認している限り、その攻撃者は「オープンリレーサーバー」を狙って自動攻撃をしている。
攻撃者は自由に転送命令を出せるサーバーにDoS的にメールを送る。
目的は不正なリンクを含んだメールをyahoo.com.twやyahoo.esに送信することで、アカウントを奪うことだ。
TECHFUNDではメーラーであるpostfixをAWSがサポートしていないメール受信→転送という機能の実現に用いる。
ストレージにもCPUにもコストをかけずに、受信したメールを即座にgmailなどの運営者のメールサーバーへ転送する。
これを許可しつつも、不正な転送を行わせない。
設定はシンプルで、ホワイトリストに載ったドメイン以外には転送をする前に排除する対策と、海外タイムゾーンのIPは二回目以降遮断する対策と、1分間に5回送信したメールアドレスは遮断する対策だ。
また、ログがストレージを圧迫しないように`/etc/log/maillog`にdailyのlogrotateを設定した。

管理者: shogochiai(shogo1104@gmail.com/@_sgtn)

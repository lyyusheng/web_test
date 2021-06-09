# 数据：账号、密码、预期 caseid
# 测试分组
# 用户分组数据：测试用例方法步骤逻辑是否发生变化

# 用户登陆成功
user_info_success = [{"username": "18300070752", "pwd": "lys123456", "expected": "木子鱼先森"}]
user_info_error = [
    {"username": "", "pwd": "", "expected": "请输入手机号"},  # 这里会出来两条提示，会定位到两个，但是却不会报错？
    {"username": "12", "pwd": "lys123456", "expected": "请输入正确的手机号"},
    #  {"username": "18300070752", "pwd": "12", "expected": "请输入密码"}  #这个是用户名或者密码错误，定位不同，写这里汇报错
]
user_info_authorize = [{"username": "18300070799", "pwd": "123", "expected": "此账号没有经过授权，请联系管理员!"},
                       {"username": "18300070752", "pwd": "123", "expected": "帐号或密码错误!"}
                       ]

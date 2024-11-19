# built in function:
# print get hget hpost
# 生命周期
# built-in event : start end
event "start"{
	print("你好！欢迎使用我们的客服机器人。");
	login();
}
event "end"{
	print("感谢你的咨询，再见！");
}
event "购买商品" {
	string itent = get("你想购买什么商品？");
	print("你想购买{itent},是吗");
}
event "查询余额" {
	float res = hget("...");
}
event "天气" {
	string res =  hget("...");
	print(res);
}
event "斐波那契数列" {
	int n = get("项数");
	int res = fbc(n);
}
fn login(){
 string acc = get("请输入账号");
 string psw = get("请输入密码");
 json data = {
	 "acc" : acc,
	 "psw" : psw
 };
 usl = "....";
 json res = hpost(url, data);
 print(res.some);
}
event "bye" {
  exit();
}
event "other" {
	# 自动输出 "无对应功能" + {相近的功能}
}
fn fbc(int n) {
	if (n== 0 || n==1) {
		return 1;
	}
	return n*fbc(n-1);
}
event "start" {
  print("欢迎来到天气查询机器人");
  menu();
}
event "天气" {
  json res = hget("http://localhost:5000/weather");
  string climate = res.climate;
  string temp  = res.temp;
  print("当前天气是${climate}， 并且温度是${temp}");
}
event "登陆" {
  string post_url = "http://127.0.0.1:5000/data";
  string name = "Alice";
  string key = "name";
  json post_data = {
    "key": key,
    "value":name
  };
  hpost(post_url,post_data);
  print("登陆成功");
}
event "查询登陆状态" {
  string get_url = "http://127.0.0.1:5000/data/name";
  json res = hget(get_url);
  print("${res}");
}
event "other" {
  print("没有这个功能(⊙o⊙)");
  menu();
}
event "退出" {
  exit();
}
fn menu() {
  print("菜单:\n");
  print("  1-天气");
  print("  2-登陆");
  print("  3-查询登陆状态");
}
event "start" {
  print("Test all data type\n");
  int a = 1;
  int b = a;
  int c = b;
  print("a:${a},b:${b},c:${c}");
  {
    float a = 1.1;
    float b = a + 0.1;
    float c = b;
    print("a:${a},b:${b},c:${c}");
  }
  # 暂不支持 json 嵌套
  json tmp = {
    "f" : 1,
    "t" : 2
  };
  json data = tmp;
  tmp.f = 3;
  print("tmp is ${tmp} \n");
  print("data is ${data} ");
}

event "退出" {
  exit();
}

event "other" {
  print("菜单:");
  print("1-退出");
}
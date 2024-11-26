# 计算斐波那契数列
event "start" {
  print("你好！欢迎使用我们的斐波那契数列计算机器人。");
  int n = get("请输入你想计算的斐波那契数列的项数：");
  int result = fbc(n);
  print("第 ${n} 项的斐波那契数列结果是：${result}");
  ask_again();
}

event "end" {
  print("感谢你的使用，再见！");
}
event "other" {
  print("无其它功能, 我们还是来算算斐波那契数列吧!");
  ask_again();
}

fn ask_again() {
  string choice = get("你想继续计算吗？(是/否)");
  if (choice == "是") {
    int n = get("请输入你想计算的斐波那契数列的项数：");
    int result = fbc(n);
    print("第 ${n} 项的斐波那契数列结果是：${result}");
    ask_again();
  } else if(choice == "否") {
    exit();
  } else {
    print("小淘气！不要乱输入哟~");
  }
}

fn fbc(int n) {
  if (n == 0 || n == 1) {
    return 1;
  }
  return fbc(n - 1) + fbc(n - 2);
}
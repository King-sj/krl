event "start" {
  print("欢迎来到年龄裁断机器人\n");
  int age = get("please input your age:\n");
  check_age(age);
}

fn check_age(int age) {
  if (age < 0) {
    print("Age cannot be negative. Please try again.");
    int new_age = get("please input your age:\n");
    check_age(new_age);
  } else if (age < 18) {
    print("You are a minor.");
  } else if (age < 65) {
    print("You are an adult.");
  } else {
    print("You are a senior.");
  }
}

event "再来一次" {
  int age = get("小馋猫, please input your age:\n");
  check_age(age);
}

event "退出" {
  exit();
}

event "other" {
  print("菜单:");
  print("1-再来一次");
  print("2-退出");
}
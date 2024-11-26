event "start" {
  int n = 1;
  print("main: ${n}");
  test();
}
fn test(){
  print("test: ${n}");
}
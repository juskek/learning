void main() {
  print('Hello World!');

  List<int> testList = List.generate(5, (index) => index);
  print(testList);
  List emptyList = List.empty(growable: true);
  print(emptyList);
  emptyList.add(1);
  print(emptyList);

  // deep vs shallow immutability

  List constList = const [0, 0, 0];
  // constList[1] = 1; // deep immutability: cannot change anything

  final List finalList = [0, 0, 0];
  finalList[1] = 1; // shallow immutability: can change values/nested objects
  // finalList = 1; // shallow immutability: cannot change variable type
}

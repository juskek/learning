// RUN SCRIPT: dart run path/to/script

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

  DateTime _roundToClosestInterval(DateTime dateTime, Duration interval) {
    /// rounds a datetime to the closest interval
    /// -1 to prevent rounding to next interval when it the dateTime is on the interval
    return DateTime.fromMillisecondsSinceEpoch(
        ((dateTime.millisecondsSinceEpoch) / interval.inMilliseconds).floor() *
            interval.inMilliseconds);
  }

  print('DateTime Rounding');
  DateTime _lastStateUpdateDateTime = DateTime(2022, 3, 10, 17, 59);
  DateTime _earliestEndTime = _roundToClosestInterval(
      _lastStateUpdateDateTime.add(Duration(minutes: 15)),
      Duration(minutes: 15));
  print('_lastStateUpdateDateTime: $_lastStateUpdateDateTime');
  print('_earliestEndTime: $_earliestEndTime');

  // if earliestStartTime is less than 7 minutes from current time, bump to next 15 minutes
  print(
      'Compared Time: ${Duration(minutes: 7).compareTo(_earliestEndTime.difference(_lastStateUpdateDateTime))}');
  if (Duration(minutes: 7)
          .compareTo(_earliestEndTime.difference(_lastStateUpdateDateTime)) >
      0) {
    _earliestEndTime = _earliestEndTime.add(Duration(minutes: 15));
  }
  print('Corrected _earliestEndTime: $_earliestEndTime');

  // latest end time is 23 hrs 45 mins
  DateTime _latestEndTime = _roundToClosestInterval(
      _lastStateUpdateDateTime.add(Duration(hours: 23, minutes: 45)),
      Duration(minutes: 15));
  print('_latestEndTime: $_latestEndTime');
}

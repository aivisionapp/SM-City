import 'package:flutter/widgets.dart';
import 'package:get/instance_manager.dart';
import 'package:sm_city/features/event/domain/models/monads.dart';

import '../../domain/use_cases/get_events_count.dart';

class EventsList extends StatelessWidget {
  final ValueNotifier<EventsCountMonad?> eventsCount = ValueNotifier(null);

  EventsList({super.key}) {
    final getEventsCount = Get.find<IGetEventsCount>();
    getEventsCount().then((value) => eventsCount.value = value);
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: ValueListenableBuilder(
        valueListenable: eventsCount,
        builder: (
          BuildContext context,
          EventsCountMonad? value,
          Widget? child,
        ) {
          if (value == null) {
            return const Text('...');
          }

          if (value.count == null) {
            return const Text('N/A');
          }

          return Text('Events count: ${value.count}');
        },
      ),
    );
  }
}

import 'package:get/instance_manager.dart';
import 'package:sm_city/features/event/domain/models/monads.dart';
import 'package:sm_city/features/event/domain/repositories/get_events_count.repo.dart';

abstract class IGetEventsCount {
  Future<EventsCountMonad> call();
}

class GetEventsCount implements IGetEventsCount {
  @override
  call() async {
    final getEventsCountRepo = Get.find<IGetEventsCountRepo>();

    EventsCountMonad monad;

    try {
      monad = EventsCountMonad(count: await getEventsCountRepo());
    } on Exception catch (e) {
      monad = EventsCountMonad(error: e.toString());
    }

    return monad;
  }
}

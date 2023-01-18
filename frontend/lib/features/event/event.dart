import 'package:get/instance_manager.dart';

import 'data/repositories/get_events_count.repo.dart';
import 'domain/repositories/get_events_count.repo.dart';
import 'domain/use_cases/get_events_count.dart';

export 'presentation/pages/summary.dart';

injectEventFeature() {
  Get.put<IGetEventsCountRepo>(GetEventsCountRepo());
  Get.put<IGetEventsCount>(GetEventsCount());
}

import 'package:flutter/material.dart';

import 'package:sm_city/features/event/event.dart';
import 'package:sm_city/pages/vehicles/vehicles.dart';
import 'package:sm_city/routing/routes.dart';

const Map<String, Widget> routesWidgets = {
  summaryDisplayPageRoute: SummaryPage(),
  vehiclesPageRoute: Vehicles(),
};

Route<dynamic> generateRoute(RouteSettings settings) {
  return _getPageRoute(routesWidgets[settings.name] ?? const SummaryPage());
}


PageRoute _getPageRoute(Widget child) {
  return MaterialPageRoute(
    builder: (context) => child,
  );
}

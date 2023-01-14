import 'package:flutter/material.dart';
import 'package:sm_city/pages/summary/summary.dart';
import 'package:sm_city/pages/vehicles/vehicles.dart';
import 'package:sm_city/routing/routes.dart';

import '../pages/authentication/authentication.dart';

Route<dynamic> generateRoute(RouteSettings settings) {

  switch(settings.name) {

    case summaryDisplayPageRoute:
      return _getPageRoute(Summary());
    case vehiclesPageRoute:
      return _getPageRoute(Vehicles());
    default:
      return _getPageRoute(Summary());

  }

}


PageRoute _getPageRoute(Widget child) {
  return MaterialPageRoute(
    builder: (context) => child,
  );
}
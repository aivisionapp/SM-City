import 'package:flutter/material.dart';

import '../constants/controllers.dart';
import '../routing/router.dart';
import '../routing/routes.dart';

Navigator localNavigator() => Navigator(
      key: navigationController.navigatorKey,
      initialRoute: summaryDisplayPageRoute,
      onGenerateRoute: generateRoute,
    );

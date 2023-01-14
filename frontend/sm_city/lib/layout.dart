import 'package:flutter/material.dart';

import 'helpers/responsive.dart';
import 'widgets/large_screen.dart';
import 'widgets/side_menu.dart';
import 'widgets/small_screen.dart';
import 'widgets/top_nav.dart';

class SiteLayout extends StatelessWidget {
  SiteLayout({super.key});

  final GlobalKey<ScaffoldState> _key = GlobalKey<ScaffoldState>();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        key: _key,
        appBar: topNavigationBar(context, _key),
        drawer: Drawer(
          child: SideMenu(),
        ),
        body: ResponsiveWidget(
            largeScreen: LargeScreen(),
            smallScreen: SmallScreen(),
            mediumScreen: LargeScreen()));
  }
}

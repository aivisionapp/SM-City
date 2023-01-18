import 'package:flutter/material.dart';
import 'package:get/get.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:google_fonts/google_fonts.dart';

import 'features/event/event.dart';
import 'controllers/menu_controller.dart';
import 'controllers/navigation_controller.dart';
import 'layout.dart';

Future<void> main() async {
  await dotenv.load(fileName: '.env');

  Get.put(MenuController());
  Get.put(NavigationController());

  Get.put<Uri>(tag: 'API_URI', Uri.parse(dotenv.env['API_URI']!));

  injectEventFeature();

  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return GetMaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Dash',
      theme: ThemeData(
        scaffoldBackgroundColor: Colors.white,
        textTheme: GoogleFonts.mulishTextTheme(
          Theme.of(context).textTheme,
        
        ).apply(
          bodyColor: Colors.black,
          displayColor: Colors.black,
        
        ) , 
        pageTransitionsTheme: const PageTransitionsTheme(
          builders: {
            TargetPlatform.windows: ZoomPageTransitionsBuilder(),
            TargetPlatform.iOS: ZoomPageTransitionsBuilder(),
          },
        ),
        primaryColor: Colors.blue
      ),
      home: SiteLayout(),
    );
  }
}

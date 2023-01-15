import 'package:flutter/material.dart';


import '../constants/style.dart';
import '../helpers/responsive.dart';
import 'custom_text.dart';

AppBar topNavigationBar(BuildContext context, GlobalKey<ScaffoldState> key) {
  return AppBar(
    leading: !ResponsiveWidget.isSmallScreen(context)!
        ? Row(
            children: [
              Container(
                padding: EdgeInsets.only(left: 10),
                child: Image.asset(
                  'assets/icons/logo.png',
                  height: 40,
                  width: 30,
                ),
              )
            ],
          )
        : IconButton(
            onPressed: () {
              key.currentState!.openDrawer();
            },
            icon: Icon(Icons.menu)),
    elevation: 0,
    title: Row(
      children: [
        Visibility(
            child: CustomText(
          text: 'Smart Eye',
          size: 20,
          color: lightGrey,
          weight: FontWeight.bold,
        )),
        Expanded(child: Container()),
        IconButton(
          onPressed: () {},
          icon: Icon(Icons.settings),
          color: dark.withOpacity(.7),
        ),
        Stack(
          children: [
            IconButton(
              onPressed: () {},
              icon: Icon(Icons.notifications),
              color: dark.withOpacity(.7),
            ),
            Positioned(
              top: 8,
              right: 8,
              child: Container(
                height: 8,
                width: 8,
                decoration: BoxDecoration(
                    color: active, borderRadius: BorderRadius.circular(30)),
              ),
            )
          ],
        ),
        Container(
          width: 1,
          height: 22,
          color: lightGrey,
        ),
        SizedBox(
          width: 24,
        ),
        CustomText(
          text: 'Abdullah Mohammed',
          color: lightGrey,
          size: 20,
          weight: FontWeight.normal,
        ),
        SizedBox(
          width: 16,
        ),
        Container(
          decoration: BoxDecoration(
              color: Colors.white, borderRadius: BorderRadius.circular(30)),
          child: Container(
            padding: EdgeInsets.all(2),
            margin: EdgeInsets.all(2),
            child: CircleAvatar(
              backgroundImage: AssetImage('assets/icons/avatar.png'),
              backgroundColor: light,
            ),
          ),
        )
      ],
    ),
    backgroundColor: light,
    iconTheme: IconThemeData(color: dark),
  );
}

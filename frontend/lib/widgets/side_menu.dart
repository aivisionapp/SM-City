import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../constants/controllers.dart';
import '../constants/style.dart';
import '../helpers/responsive.dart';
import '../routing/routes.dart';
import 'custom_text.dart';
import 'side_menu_item.dart';



class SideMenu extends StatelessWidget {
  const SideMenu({super.key});

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    return Container(
      color: light,
      child: ListView(
        children: [
          if (ResponsiveWidget.isSmallScreen(context))
            Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                SizedBox(height: 40),
                Row(
                  children: [
                    SizedBox(width: width / 48),
                    Padding(
                      padding: const EdgeInsets.only(right: 12.0),
                      child: Image.asset(
                        "assets/icons/logo.png",
                        height: 28,
                      ),
                    ),
                    Flexible(
                        child: CustomText(
                      text: "Smart",
                      size: 20,
                      color: active,
                      weight: FontWeight.bold,
                    )),
                    SizedBox(width: width / 48),
                  ],
                ),
              ],
            ),
          Divider(
            color: lightGrey.withOpacity(.1),
          ),
          Column(
              mainAxisSize: MainAxisSize.min,
              children: sideMenuItemNames
                  .map((item) => SideMenuItem(
                      itemName: item.name == authenticationPageDisplayName
                          ? "Log Out"
                          : item.name,
                      onTap: () {
                        if (item.name == authenticationPageDisplayName) {
                          // TODO log out
                        }

                        if (!menuController.isActive(item.name)) {
                          menuController.changeActiveItemTo(item.name);
                          if (ResponsiveWidget.isSmallScreen(context)) {
                            Get.back();
                          }
                          navigationController.navigateTo(item.route);
                        }
                      }))
                  .toList()),
        ],
      ),
    );
  }
}

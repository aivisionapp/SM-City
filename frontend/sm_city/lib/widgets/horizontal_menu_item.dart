import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../constants/controllers.dart';
import '../constants/style.dart';
import 'custom_text.dart';


class HorizontalMenuItem extends StatelessWidget {
  final String itemName;
  final VoidCallback onTap;

  const HorizontalMenuItem(
      {super.key, required this.itemName, required this.onTap});

  @override
  Widget build(BuildContext context) {
    double width = MediaQuery.of(context).size.width;
    return InkWell(
      onTap: onTap,
      onHover: (value) {
        value
            ? menuController.onHover(itemName)
            : menuController.onHover("not hovering");
      },
      child: Obx(() => Container(
            color: menuController.isHovering(itemName)
                ? Colors.white.withOpacity(0.1)
                : Colors.transparent,
            child: Row(
              children: [
                Visibility(
                  visible: menuController.isHovering(itemName) ||
                      menuController.isActive(itemName),
                  maintainAnimation: true,
                  maintainState: true,
                  maintainSize: true,
                  child: Container(
                    height: 40,
                    width: 6,
                    color: dark,
                  ),
                ),
                SizedBox(
                  width: width / 80,
                ),
                Padding(
                  padding: EdgeInsets.all(16),
                  child: menuController.returnIconFor(itemName),
                ),
                if (!menuController.isActive(itemName))
                  Flexible(
                    child: CustomText(
                      text: itemName,
                      color: menuController.isHovering(itemName)
                          ? dark
                          : lightGrey,
                      size: 20,
                      weight: FontWeight.normal,
                    ),
                  ) else Flexible(
                    child: CustomText(
                      text: itemName,
                      color: dark,
                      size: 18,
                      weight: FontWeight.bold,
                    ),
                  )
              ],
            ),
          )),
    );
  }
}

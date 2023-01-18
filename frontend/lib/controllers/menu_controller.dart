import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../constants/style.dart';
import '../routing/routes.dart';

const Map<String, IconData> itemsIcons = {
    summaryDisplayName: Icons.summarize,
    detectionsDisplayName: Icons.image,
    vehiclesDisplayName: Icons.cases_sharp,
    authenticationPageDisplayName: Icons.exit_to_app,
  };

class MenuController extends GetxController {
  static MenuController instance = Get.find();
  var activeItem = summaryDisplayPageRoute.obs;
  var hoverItem = "".obs;

  changeActiveItemTo(String itemName) {
    activeItem.value = itemName;
  }

  onHover(String itemName) {
    if (!isActive(itemName)) hoverItem.value = itemName;
  }

  isHovering(String itemName) => hoverItem.value == itemName;

  isActive(String itemName) => activeItem.value == itemName;

  Widget returnIconFor(String itemName) {
    return _customIcon(itemsIcons[itemName] ?? Icons.exit_to_app, itemName);
  }

  Widget _customIcon(IconData icon, String itemName) {
    if (isActive(itemName)) return Icon(icon, size: 22, color: dark);

    return Icon(
      icon,
      color: isHovering(itemName) ? dark : lightGrey,
    );
  }
}

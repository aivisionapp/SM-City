import 'package:flutter/material.dart';
import 'package:get/get.dart';

import '../constants/style.dart';
import '../routing/routes.dart';

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
    switch (itemName) {
      case summaryDisplayName:
        return _customIcon(Icons.summarize, itemName);
      case detectionsDisplayName:
        return _customIcon(Icons.image, itemName);
      case vehiclesDisplayName:
        return _customIcon(Icons.cases_sharp, itemName);
      case authenticationPageDisplayName:
        return _customIcon(Icons.exit_to_app, itemName);
      default:
        return _customIcon(Icons.exit_to_app, itemName);
    }
  }

  Widget _customIcon(IconData icon, String itemName) {
    if (isActive(itemName)) return Icon(icon, size: 22, color: dark);

    return Icon(
      icon,
      color: isHovering(itemName) ? dark : lightGrey,
    );
  }
}

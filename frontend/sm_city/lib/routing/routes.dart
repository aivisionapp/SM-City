const rootRoute = "/";

const summaryDisplayName = "Summary";
const summaryDisplayPageRoute = "/summary";

const detectionsDisplayName = "Detections";
const detectionsPageRoute = "/detections";

const vehiclesDisplayName = "Vehicles";
const vehiclesPageRoute = "/vehicles";

const authenticationPageDisplayName = "Log out";
const authenticationPageRoute = "/auth";

class MenuItem {
  final String name;
  final String route;

  MenuItem(this.name, this.route);
}

List<MenuItem> sideMenuItemNames = [
  MenuItem(summaryDisplayName, summaryDisplayPageRoute),
  MenuItem(vehiclesDisplayName, vehiclesPageRoute),
  MenuItem(authenticationPageDisplayName, authenticationPageRoute),
];

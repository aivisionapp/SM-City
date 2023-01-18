import 'package:flutter/widgets.dart';

import '../../presentation/components/events_list.dart';

class SummaryPage extends StatelessWidget {
  const SummaryPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          EventsList(),
        ],
      ),
    );
  }
}

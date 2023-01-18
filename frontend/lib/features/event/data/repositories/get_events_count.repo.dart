import 'dart:convert';

import 'package:get/get.dart';
import 'package:http/http.dart' as http;

import '../../domain/repositories/get_events_count.repo.dart';

class GetEventsCountRepo implements IGetEventsCountRepo {
  @override
  call() async {
    final request = await http.get(Get.find<Uri>(tag: 'API_URI').replace(path: '/event/count'));
    if (request.statusCode != 200) {
      throw Exception(request.reasonPhrase ?? 'Unexpected error');
    }

    final response = json.decode(request.body);

    return response['events_count']!;
  }
}

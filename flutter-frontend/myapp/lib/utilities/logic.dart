import 'dart:async';
import 'dart:collection';
import 'dart:convert';
import 'dart:io';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'package:file_picker/file_picker.dart';

// Constant definitions
const String FLASK_SERVER = "127.0.0.1";
const String FLASK_PORT = "5000";


class InfoSample {
  final int id;
  final String object_hash;
  final String message;


 InfoSample({
  required this.id,
  required this.object_hash,
  required this.message
 });

  factory InfoSample.fromJson(String, dynamic json) {
    return InfoSample(
        id: json['id'],
        object_hash: json['object_hash'],
        message: json['message']
        );
  }
}

Future fetchInfo() async {
  final response = await http.get(Uri.parse('http://$FLASK_SERVER:$FLASK_PORT/api/v1/info'));

  if (response.statusCode == 200) {
    return Text(response.body, textScaleFactor: 0.5);
  } else {
    throw Exception('Failed to load info sample data');
  }
}

Future fetchImage() async {
  final response = await http.get(
      Uri.parse('http://$FLASK_SERVER:$FLASK_PORT/api/v1/image'));

  if (response.statusCode == 200) {
    return Image.memory(response.bodyBytes);
  } else {
    throw Exception('Failed to load image.');
  }
}

Future selectImage() async {
  FilePickerResult? result = await FilePicker.platform.pickFiles();

  String? path = result?.files.single.path;
  if (path != null) {
    return Image.file(File(path));
  } else {
    throw Exception('Failed to load image from file system.');
  }
}
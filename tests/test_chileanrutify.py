import pytest
from chileanrutify import valid_rut_value, valid_rut_values, get_verifier, valid_rut_verifier, normalize_rut, classic_rut, dash_only_rut, format_rut, valid_rut, stringify_rut

def test_valid_rut_value():
  assert valid_rut_value("y") == False
  assert valid_rut_value("/") == False
  assert valid_rut_value([]) == False
  assert valid_rut_value(0) == True
  assert valid_rut_value("9") == True
  assert valid_rut_value("k") == True
  assert valid_rut_value("K") == True

def test_valid_rut_values():
  assert valid_rut_values("ya12") == False
  assert valid_rut_values("/s21") == False
  assert valid_rut_values(["1234"]) == False
  assert valid_rut_values("1234") == True
  assert valid_rut_values(1230) == True
  assert valid_rut_values("4.678-9") == True
  assert valid_rut_values("234k") == True
  assert valid_rut_values("K") == True

def test_get_verifier():
  assert get_verifier("12148514") == "1"
  assert get_verifier("23379716") == "2"
  assert get_verifier("32938250") == "8"
  assert get_verifier("36128619") != "0"
  assert get_verifier("36228719") != "0"
  assert get_verifier("36238719") != "0"

def test_valid_rut_verifier():
  assert valid_rut_verifier("12.148.514-1") == True
  assert valid_rut_verifier("23.379.716-2") == True
  assert valid_rut_verifier("18.486.758-3") == True
  assert valid_rut_verifier("14.001.723-8") == False
  assert valid_rut_verifier("14.175.644-4") == False
  assert valid_rut_verifier("36238719-0") == False

def test_normalize_rut():
  assert normalize_rut("12.148.514-1") == "121485141"
  assert normalize_rut("12.514-1") == "125141"
  assert normalize_rut("128.538-9") == "1285389"
  assert normalize_rut("14.001.723-8") == "140017238"
  assert normalize_rut("14.175.644-4") == "141756444"
  assert normalize_rut("36238719-0") == "362387190"

def test_classic_rut():
  assert classic_rut("12.148.514-1") == "12.148.514-1"
  assert classic_rut("125141") == "12.514-1"
  assert classic_rut("1285389") == "128.538-9"
  assert classic_rut("140017238") == "14.001.723-8"
  assert classic_rut("141756444") == "14.175.644-4"
  assert classic_rut("362387190") == "36.238.719-0"

def test_dash_only_rut():
  assert dash_only_rut("12.148.514-1") == "12148514-1"
  assert dash_only_rut("125141") == "12514-1"
  assert dash_only_rut("1285389") == "128538-9"
  assert dash_only_rut("140017238") == "14001723-8"
  assert dash_only_rut("141756444") == "14175644-4"
  assert dash_only_rut("362387190") == "36238719-0"

def test_format_rut():
  assert format_rut("1285389") == "128.538-9"
  assert format_rut("121485141") == "12.148.514-1"
  assert format_rut("125141") == "12.514-1"
  assert format_rut("1285389", "dash_only") == "128538-9"
  assert format_rut("121485141", "dash_only") == "12148514-1"
  assert format_rut("125141", "dash_only") == "12514-1"
  assert format_rut("1285389", "normalized") == "1285389"
  assert format_rut("121485141", "normalized") == "121485141"
  assert format_rut("12.148.514-1", "normalized") == "121485141"

def test_valid_rut():
  assert valid_rut("12.148.514-1") == True
  assert valid_rut("23.379.7162") == True
  assert valid_rut("18.486758-3") == True
  assert valid_rut("36238719-0") == False
  assert valid_rut("14.001.723-8") == False
  assert valid_rut("14.175.644-4") == False

def test_stringify_rut():
  assert stringify_rut(12148514) == "12148514"
  assert stringify_rut("12.148.514-1") == "12.148.514-1"
  assert stringify_rut(121485141) == "121485141"
  assert stringify_rut([]) == None
  assert stringify_rut(["1234"]) == None
#!/usr/bin/python

import requests
import json

# http://stackoverflow.com/questions/645312/what-is-the-quickest-way-to-http-get-in-python
# http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
# http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python


def get_data():
  url = "http://stats.oecd.org/sdmx-json/data/"
  identifier = "QNA"
  separator = "+"
  locationList = ["AUS"]
  locations = separator.join(locationList)
  subjectList = ["GDP", "B1_GE"]
  subjects = separator.join(subjectList)
  measureList = ["CUR", "VOBARSA"]
  measures = separator.join(measureList)
  frequency = "Q"
  startTime = "2009-Q2"
  endTime = "2010-Q1"
  
  search_url = url + identifier + "/" + locations + "." + subjects + "." + measures + "." + frequency + "/all?startTime=" + startTime + "&endTime=" + endTime
#  print search_url
  response = requests.get(search_url)
  print response



  data=json.loads(response.content)
#  print data
#  print data['header']
  print data['header']['sender']['name']

  printable_data = json.dumps(data, indent=4, separators=(',',':'))
  print printable_data

get_data()
#post_data()

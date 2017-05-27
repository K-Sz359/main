# _*_ coding: utf-8 _*_
# UTF-8　にて記述

import pandas

urlString = "http://www.yahoo.co.jp/"
result = pandas.io.html.read_html(urlString)

print result

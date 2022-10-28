## Test for INFO

### Requirements:
* Install dependencies if neccesary for running scripts
`pip install -r requirements.txt`


# Technical description


In order to finish this task, you need a github account, commit your code after each test case finish. 
Let us know and share the full project with us when you done. 

Other source code management tool is accepted as well.

### Api Automation tasks 


* api-1:
https://ct.pinterest.com/user/?event=search&ed=%7B%22np%22%3A%22gtm%22%7D&tid=2612859132799&cb=1664577078288
1. For parameter tid, please use current time, and cb use the next day any time
2. Validate it returns status code 200,
3. Validate the schema is correct. 
4. Validate isUtilizingAdvertiser1pEnabled is false.

* api-2:
post https://www.google.com/recaptcha/api2/webworker.js?hl=en&v=ovmhLiigaw4D9ujHYlHcKKhP
1. Validate it contains "Sql error"
2. Validate status code is 500

#### If you found bug, please report bug.


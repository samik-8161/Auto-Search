# Auto-Search

Is your college forcing you to give tests online via google/ microsoft forms?
Must be tired of copy-pasting each question and searching it on google.com, right?

This python script fetches questions from the forms and searches for them itself, though it does not returns the correct answer.
It simply searches for each question on google in a new tab. You can go through the results on the tab and discover the right answer yourself.

## Requirements
1). ChromeDriver should be installed and added in your PATH environment variable.

2). Selenium Python bindings to access Selenium Web Driver. `pip install Selenium`

## Steps to run the script

1). Save your google/ microsoft form as <filename>.pdf [You can right click on the page opened in browser, click on **print as pdf**]
  
2). Convert pdf into textfile using command-
  ```
  .\pdftotext.exe <filename>.pdf
  ```
3). Extract questions from .txt file using command-
  ```
  python cleantext.py <fiename>.py [starting] [no_of_Sets]
  ```
  where, starting is the serial number of first question in your pdf. no_of_Sets is total number of sessions into which you would like to divide the task. 
  This will create *no_of_set* number of setx.txt files. Each file contains certain number of questions.
 
4). To search for given set of questions-
  ```
  python search.py <setno>
  ```
 
  To Close the whole browser window, input any key from keyboard.

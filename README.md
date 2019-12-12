# sel

Simple script to open a page with selenium.

Also .spec ready to compile to onefile .exe

pyinstaller ./crackwatch_ez.spec --onefile

Or without .spec

pyinstaller ./crackwatch_ez.py --onefile --noconsole --add-binary "./chromeDriver/chromedriver.exe;./chromeDriver"

with pyinstaller

One thing needed is "chromedriver.exe" like this:

dist/

　└ main/
 
　　　├ chromeDriver/
   
　　　│　└ chromedriver.exe
   
　　　└ crackwatch_ez.exe

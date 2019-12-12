# sel

Simple script to open a page with selenium.

Also .spec ready to compile to onefile .exe

<i>pyinstaller ./crackwatch_ez.spec --onefile</i>

Or without .spec

<i>pyinstaller ./crackwatch_ez.py --onefile --noconsole --add-binary "./chromeDriver/chromedriver.exe;./chromeDriver"</i>



You need "chromedriver.exe" like this:

dist/

　└ main/
 
　　　├ chromeDriver/
   
　　　│　└ chromedriver.exe
   
　　　└ crackwatch_ez.exe

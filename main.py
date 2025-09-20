"""---the main file---"""
import flet as ft #import the librey flet 
from home import * # import the file home.py for the first page
def main(page):
    """---the main function---"""
    #useing the module home(page) in home.py
    home(page)
print("ff")
try:
    #run the app
        
    ft.app(target=main,assets_dir="assets/")
except Exception as e:
    print(e)

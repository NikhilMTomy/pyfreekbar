# PyFreekBar -  freek scented bar with python 

## Dependencies
**[lemonbar-xft](https://github.com/krypt-n/bar "krypt-n/bar")**  
**[arrow](https://pypi.python.org/pypi/arrow "pip install arrow")**  
**[wmctrl](http://tripie.sweb.cz/utils/wmctrl/)**  
**[xdotool](http://www.semicomplete.com/projects/xdotool/)**  
## Customizing  
The base script is `bar.sh`. It contains all the command line arguments given to lemonbar.  

The controller script is `pyfreekbar.py` in the base directory. The modules are in the `modules` direcotry.   

The lemonbar config is done in the indivudual modules  

## Modules  
Modules are kept under `modules` directory.  
### freektime  
_Contains function regarding time display_  
_Requires the dependency arrow_  
#### Methods and variables  
`**formatter()**` : returns the given string with proper lemonbar formatting  
`**getdatetime()**` : returns date and time in specified format (default YYYY-MM-DD HH:mm:ss)  
`**getime()**` : returns only time in specified format(default HH:mm:ss)  
`**getdate()**` : returns only date in specified format(default YYYY-MM-DD)  

### freekcolors  
_Contains color constants_  
_Edit this if you want to change the color scheme_  

### freekbat  
_Contains functions regarding battery display_  
#### Methods and variables  
`**getbat()**` : returns the formatted battery output (icons by FontAwesome)  
`INTERFACE` : It is the battery interface **Must configure this before running**  
`BAT_DIR` : It is the directory where battery details are stored  

=================================
[1] Info
[2] Requirements
[3] Faq
[4] Our Discord
=================================

============== (1) [INFO](1) ============== 

Appname : XGame Launcher
version : 1.1.1
Developer : AmirHossein
CopyRight 2021 / 2022

============== (2) [Requirements] (2) ==============

Python v3.9.2

============== (3) [FAQ] (3) ==============
1- How to add or remove games?
	open 'config.json' file with notpad and add your gamename and gamepath
	like this:

		"GameName":"C:\\Program Files\\GameFolder\\game.exe",

	Tip:Remember that the last game you add should not be placed in front of it. Like :
		
		{
			"Games": {
			        "GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
	        		"GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
		        	"GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
			        "GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
			        "GameName":"C:\\Program Files\\GameFolder\\game.exe"  <---------------
        }
}

----
2- I added the game location correctly but it does not run when I run it.
	In some games there is this problem, you can place the shortcut in the game instead of the main place of the game
	tip: To note that the format of the shortcuts is '.lnk', when you add the location of the game shortcut, '.lnk' should be in front of the gamepath.
	like:
		"GameName": "C:\\Users\\AmirHossein\\Desktop\\gta v.lnk",

----
3- How can I change the theme?
	It's easy, just select the theme change option in the File menu.

----
4- I have a problem, how do I fix it?
	You can join our Discord server using the link below and ask us your question.

============== (4) [OUR DISCORD] (4) ==============
Discord : 
https://discord.gg/aty7pbvzHp
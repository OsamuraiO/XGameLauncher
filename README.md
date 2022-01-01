# XGameLauncher
A simple and small game launcher written with Python | XGameLauncher

## Python version
`3.9.2`

## FAQ's

1- How to add or remove games?

open '`config.json`' file with notpad and add your gamename and gamepath
like this:

  ```
"GameName":"C:\\Program Files\\GameFolder\\game.exe",
  ```
	
  **Tip:** Remember that the last game you add should not be placed in front of it. Like :
```
{
"Games": {
  "GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
  "GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
  "GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
  "GameName":"C:\\Program Files\\GameFolder\\game.exe", <---------------
  "GameName":"C:\\Program Files\\GameFolder\\game.exe"  <---------------
        }
}

```

2- I added the game location correctly but it does not run when I run it.

In some games there is this problem, you can place the shortcut in the game instead of the main place of the game

**tip:** To note that the format of the shortcuts is '`.lnk`', when you add the location of the game shortcut, '`.lnk`' should be in front of the gamepath.
like:
```
"GameName": "C:\\Users\\AmirHossein\\Desktop\\gta v.lnk",
```

Thank you for your attention :-)

[Discord](https://discord.gg/aty7pbvzHp) | [Profile](https://github.com/OsamuraiO)

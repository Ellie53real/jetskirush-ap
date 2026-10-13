# Jetski Rush setup guide
## Prerequisites
* VRChat, owned on Steam: https://store.steampowered.com/app/438100/VRChat/
* Archipelago, version 0.6.7 or above: https://github.com/ArchipelagoMW/Archipelago
* ``jetski_rush.apworld`` from the latest release in this repository: https://github.com/Ellie53real/jetskirush-ap/releases

## Installation
Install ``jetski_rush.apworld`` to the ``custom_worlds`` folder within the Archipelago Launcher's installation folder. This can be done either by directly copying the file to the folder, simply double-clicking the file in File Explorer, or selecting "Install APWorld" in the Archipelago Launcher and locating the file.

...that's it! It really is very simple.

## Configuring a YAML file
### Options Creator
In the Archipelago Launcher, open the ``Options Creator``. Find "Jetski Rush" in the list of games, and configure the settings to your liking!
### Editing a template YAML
In the Archipelago Launcher, use the ``Generate Template Options`` button to generate template YAMLs for all installed APWorlds. If you installed the APWorld correctly, you should be able to find a template YAML for this game at ``[AP install folder]/Players/Templates/Jetski Rush.yaml``.

## Generating a game
If you are running a solo seed, all you need to do is put your edited YAML file in the ``Players`` folder. If playing a seed with multiple slots, put all of the individual YAMLs in the same folder.

Once all of the YAMLs have been put in, run ``ArchipelagoGenerate.exe``; if the generation is successful, a ``.zip`` file containing the output will be present in the ``output`` folder.

## Hosting a game
To host a game on archipelago.gg, simply go to the site, select ``Host Game`` under ``Get Started`` on the top bar, and upload the .zip file from the ``output`` folder.

## Connecting to the multiworld
* Launch VRChat on Steam, and create a new private instance of Jetski Rush.
* Run the Jetski Rush Client from the Archipelago Launcher.
* The client will ask you to locate the log file for your current VRChat session; by default, these logs are located at ``C:/Users/[user]/AppData/LocalLow/VRChat/VRChat``.
* Once the log file is selected, the client will start tracking information from the logs!

GoToSpec
========

This is an early stage RSpec helper plugin for Sublime Text 2.

![GoToSpec Usage Sample](http://fcoury.info/GoToSpec.gif)

Usage
=====

The plugin is triggered by Ctrl+Shift+Alt+S key combo.

It will try to find the RSpec file matching the current open file.

If found, it will split the view (if needed) and open the RSpec file on the left side.

Otherwise, it will prompt the user if he wants to create a new spec for the current file.

![Creating a new spec](https://github.com/webbynode/GoToSpec/raw/master/images/inexistent-spec.png)

![Resulting spec](https://github.com/webbynode/GoToSpec/raw/master/images/resulting-spec.png)


Installation Instructions
=========================

Go to your `Packages` folder and clone the repo, usually:

    cd "$HOME/Library/Application Support/Sublime Text 2/Packages"
    git clone https://github.com/webbynode/GoToSpec.git GoToSpec

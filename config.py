#███    █▄  ███▄▄▄▄      ▄█    █▄     ▄█  ███▄▄▄▄      ▄██████▄     ▄████████ ████████▄  
#███    ███ ███▀▀▀██▄   ███    ███   ███  ███▀▀▀██▄   ███    ███   ███    ███ ███   ▀███ 
#███    ███ ███   ███   ███    ███   ███▌ ███   ███   ███    █▀    ███    █▀  ███    ███ 
#███    ███ ███   ███  ▄███▄▄▄▄███▄▄ ███▌ ███   ███  ▄███         ▄███▄▄▄     ███    ███ 
#███    ███ ███   ███ ▀▀███▀▀▀▀███▀  ███▌ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ 
#███    ███ ███   ███   ███    ███   ███  ███   ███   ███    ███   ███    █▄  ███    ███ 
#███    ███ ███   ███   ███    ███   ███  ███   ███   ███    ███   ███    ███ ███   ▄███ 
#████████▀   ▀█   █▀    ███    █▀    █▀    ▀█   █▀    ████████▀    ██████████ ████████▀  
#                                                                                       
#████████▄       ███      ▄█   ▄█          ▄████████ 
#███    ███  ▀█████████▄ ███  ███         ███    ███ 
#███    ███     ▀███▀▀██ ███▌ ███         ███    █▀  
#███    ███      ███   ▀ ███▌ ███        ▄███▄▄▄     
#███    ███      ███     ███▌ ███       ▀▀███▀▀▀     
#███    ███      ███     ███  ███         ███    █▄  
#███  ▀ ███      ███     ███  ███▌    ▄   ███    ███ 
# ▀██████▀▄█    ▄████▀   █▀   █████▄▄██   ██████████ 
#                             ▀                      
                                                                                       



#IMPORTS

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
#from libqtile.utils import guess_terminal
import subprocess
import os

from libqtile import hook
from theme import tokyonight 


#Variables and Programs
mod = "mod4"
terminal = "alacritty"
home = os.path.expanduser('~')
myAppLauncher = "rofi -show drun" 
#myAppLauncher = "./.config/rofi/launchers/type-1/launcher.sh"
myFileManager = "pcmanfm"
myBrowser = "firefox"
myEditor = "neovim"
myMusic = "Spotify"


keys = [
    
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
   
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"], "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    
    Key([mod], "Return", 
        lazy.spawn(terminal), desc="Launch terminal"),
    
    # Toggle between different layouts as defined below
    Key([mod], "Tab", 
        lazy.next_layout(), desc="Toggle between layouts"),
    
    Key([mod], "q", 
        lazy.window.kill(), desc="Kill focused window"),
    
    Key([mod, "control"], "r", 
        lazy.reload_config(), desc="Reload the config"),
    
    Key([mod, "control"], "q", 
        lazy.shutdown(), desc="Shutdown Qtile"),
    
    Key([mod], "d", lazy.spawn(myAppLauncher), 
        desc="Launch Rofi"),
    
    Key([mod], "b", lazy.spawn(myBrowser),
        desc="Launch Firefox"),

    Key([mod], "f", lazy.spawn(myFileManager),
        desc = "Launch PCMan"),
    
    #Key([mod], "r", lazy.spawncmd(), 
        #desc="Spawn a command using a prompt widget"),

]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.MonadTall(
        border_width = 2,
        border_focus = tokyonight["Sapphire"],
        border_normal = tokyonight["Lavender"],
        margin = 25,
        ),
    layout.MonadWide(
        border_width = 2,
        border_focus = tokyonight["Sapphire"],
        border_normal = tokyonight["Lavender"],
        margin = 10,
        ),
   # layout.Floating(
   #     border_width = 2,
   #     border_focus = catppuccin["Sapphire"],
   #     border_normal = catppuccin["Lavender"],
   #     margin = 10,
   #     ),
    # layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    layout.Tile( 
        border_width = 2,
        border_focus = tokyonight["Sapphire"],
        border_normal = tokyonight["Lavender"],
        margin = 10,
        ),
   # layout.TreeTab(  
   #     font = "FiraCode Nerd Font",
   #     fontsize = 20,
   #     border_width = 4,
   #     sections = [''],
   #     bg_color = catppuccin["Crust"],
   #     active_bg =catppuccin["Surface0"],
   #     active_fg = catppuccin["Text"],
   #     inactive_bg = catppuccin["Crust"],
   #     inactive_fg = catppuccin["Text"],
   #     urgent_bg = catppuccin["Surface2"],
   #     urgent_fg = catppuccin["Red"],
   #     panel_width = 200,
   #    ),
    # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font = "FiraCode Nerd Fonts",
    fontsize = 14,
    padding = 3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
               widget.CurrentLayoutIcon(scale=0.8),
                widget.GroupBox(foreground=tokyonight["White"]),
                widget.WindowName(foreground=tokyonight["White"]),
                widget.Systray(),
                widget.Clock(format="%I:%M||%a||%m/%d",
                             foreground=tokyonight["Sapphire"]),
                widget.CheckUpdates(distro='Debian', no_update_string='N|A',
                                    color_have_updates=tokyonight["Sapphire"],
                                    color_no_updates=tokyonight["White"]),
                widget.QuickExit(default_text='[X]', 
                                 countdown_format='[{}]',
                                 foreground=tokyonight["Red"]),
            ],
            32,
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color=tokyonight["Sapphire"],
            background=tokyonight["BG"],
            opacity= 0.9,
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class='bitwarden'),
        Match(wm_class='confirm'),
        Match(wm_class='dialog'),
        Match(wm_class='download'),
        Match(wm_class='error'),
        Match(wm_class='file_progress'),
        Match(wm_class='notification'),
        Match(wm_class='nm-connection-editor'),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# Java Whitelist
wmname = "LG3D"

#Hooks
#Calls Startup Apps
@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])





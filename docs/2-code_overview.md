# Code Overview

[_Documentation generated by Documatic_](https://www.documatic.com)

<!---Documatic-section-Codebase Structure Python-start--->
## Codebase Structure Python

The codebase has a single-depth folder structure,
                with 42 code files in total.

<!---Documatic-block-system_architecture-start--->
```mermaid
flowchart LR
tox_dns([tox_dns])
util([util])
toxav([toxav])
libtox([libtox])
toxav_enums([toxav_enums])
contact([contact])
history([history])
messages([messages])
avwidgets([avwidgets])
notifications([notifications])
callbacks([callbacks])
settings([settings])
toxcore_enums_and_consts([toxcore_enums_and_consts])
tox([tox])
plugin_support([plugin_support])
file_transfers([file_transfers])
main([main])
loginscreen([loginscreen])
bootstrap([bootstrap])
mainscreen([mainscreen])
passwordscreen([passwordscreen])
updater([updater])
toxes([toxes])
toxencryptsave_enums_and_consts([toxencryptsave_enums_and_consts])
menu([menu])
widgets([widgets])
basecontact([basecontact])
list_items([list_items])
screen_sharing([screen_sharing])
smileys([smileys])
items_factory([items_factory])
toxencryptsave([toxencryptsave])
mainscreen_widgets([mainscreen_widgets])
group_chat([group_chat])
calls([calls])
__init__([__init__])
friend([friend])
profile([profile])
styles
plugins
tox_dns-->util
toxav-->libtox
toxav-->toxav_enums
contact-->history
contact-->messages
avwidgets-->util
notifications-->util
callbacks-->notifications
callbacks-->settings
callbacks-->toxcore_enums_and_consts
callbacks-->toxav_enums
callbacks-->tox
callbacks-->plugin_support
file_transfers-->toxcore_enums_and_consts
file_transfers-->tox
main-->loginscreen
main-->settings
main-->bootstrap
main-->mainscreen
main-->callbacks
main-->util
main-->passwordscreen
main-->plugin_support
bootstrap-->util
history-->toxes
menu-->settings
menu-->util
menu-->widgets
basecontact-->settings
basecontact-->toxcore_enums_and_consts
passwordscreen-->widgets
list_items-->toxcore_enums_and_consts
list_items-->file_transfers
list_items-->util
list_items-->widgets
loginscreen-->widgets
tox-->toxcore_enums_and_consts
tox-->toxav
tox-->libtox
items_factory-->list_items
toxencryptsave-->toxencryptsave_enums_and_consts
mainscreen_widgets-->widgets
settings-->util
settings-->toxes
mainscreen-->menu
mainscreen-->list_items
mainscreen-->widgets
mainscreen-->mainscreen_widgets
calls-->toxav_enums
friend-->messages
profile-->list_items
profile-->friend
profile-->settings
profile-->toxcore_enums_and_consts
profile-->util
profile-->tox_dns
profile-->history
profile-->file_transfers
profile-->group_chat
```
<!---Documatic-block-system_architecture-end--->

# #
<!---Documatic-section-Codebase Structure Python-end--->

<!---Documatic-section-Important Functions-start--->
## Important Functions

<!---Documatic-block-important_funcs-start--->
<!---Documatic-block-most_used_funcs-start--->
### Most Utilised Functions

* [toxygen.util.curr_directory](9-toxygen_util.md#toxygen.util.curr_directory) (8 times)
* [toxygen.util.log](9-toxygen_util.md#toxygen.util.log) (4 times)
* [toxygen.widgets.create_menu](10-toxygen_widgets.md#toxygen.widgets.create_menu) (3 times)
* [toxygen.util.copy](9-toxygen_util.md#toxygen.util.copy) (2 times)
* [toxygen.notifications.sound_notification](4-toxygen_notifications.md#toxygen.notifications.sound_notification) (1 times)
* [toxygen.notifications.tray_notification](4-toxygen_notifications.md#toxygen.notifications.tray_notification) (1 times)
* [toxygen.tox.bin_to_string](8-toxygen_tox.md#toxygen.tox.bin_to_string) (1 times)
* [toxygen.bootstrap.generate_nodes](7-toxygen_bootstrap.md#toxygen.bootstrap.generate_nodes) (1 times)
* [toxygen.bootstrap.download_nodes_list](7-toxygen_bootstrap.md#toxygen.bootstrap.download_nodes_list) (1 times)
* [toxygen.callbacks.init_callbacks](5-toxygen_callbacks.md#toxygen.callbacks.init_callbacks) (1 times)
* [toxygen.callbacks.stop](5-toxygen_callbacks.md#toxygen.callbacks.stop) (1 times)
* [toxygen.callbacks.start](5-toxygen_callbacks.md#toxygen.callbacks.start) (1 times)
* toxygen.util.program_version (1 times)
* [toxygen.util.remove](9-toxygen_util.md#toxygen.util.remove) (1 times)
* [toxygen.util.convert_time](9-toxygen_util.md#toxygen.util.convert_time) (1 times)
* [toxygen.util.curr_time](9-toxygen_util.md#toxygen.util.curr_time) (1 times)
* [toxygen.util.append_slash](9-toxygen_util.md#toxygen.util.append_slash) (1 times)
* [toxygen.tox_dns.tox_dns](8-toxygen_tox.md#toxygen.tox_dns.tox_dns) (1 times)
* toxygen.file_transfers.is_inline (1 times)
<!---Documatic-block-most_used_funcs-end--->
<!---Documatic-block-important_funcs-end--->

# #
<!---Documatic-section-Important Functions-end--->

<!---Documatic-section-File IO-start--->
## File IO

<!---Documatic-block-file_io-start--->
The following files have file read operations

<!---Documatic-block-toxygen-start--->
<details>
	<summary><code>toxygen</code> (Click to Expand!)</summary>

* toxygen.avwidgets
* toxygen.bootstrap
* toxygen.file_transfers
* toxygen.history
* toxygen.main
* toxygen.mainscreen_widgets
* toxygen.menu
* toxygen.notifications
* toxygen.profile
* toxygen.settings
* toxygen.smileys
</details>
<!---Documatic-block-toxygen-end--->

<!---Documatic-block-toxygen.plugins-start--->
<details>
	<summary><code>toxygen.plugins</code> (Click to Expand!)</summary>

* toxygen.plugins.plugin_super_class
</details>
<!---Documatic-block-toxygen.plugins-end--->

The following files have file write operations

<!---Documatic-block-toxygen-start--->
<details>
	<summary><code>toxygen</code> (Click to Expand!)</summary>

* toxygen.basecontact
* toxygen.bootstrap
* toxygen.file_transfers
* toxygen.history
* toxygen.mainscreen
* toxygen.settings
* toxygen.util
</details>
<!---Documatic-block-toxygen-end--->

<!---Documatic-block-toxygen.plugins-start--->
<details>
	<summary><code>toxygen.plugins</code> (Click to Expand!)</summary>

* toxygen.plugins.plugin_super_class
</details>
<!---Documatic-block-toxygen.plugins-end--->
<!---Documatic-block-file_io-end--->

# #
<!---Documatic-section-File IO-end--->

<!---Documatic-section-Class Hierarchy-start--->
## Class Hierarchy

<!---Documatic-block-contact.Contact-start--->
<details>
	<summary><code>contact.Contact</code> (Click to Expand!)</summary>

* toxygen.friend.Friend
* toxygen.group_chat.GroupChat
</details>
<!---Documatic-block-contact.Contact-end--->

<!---Documatic-block-toxygen.basecontact.BaseContact-start--->
<details>
	<summary><code>toxygen.basecontact.BaseContact</code> (Click to Expand!)</summary>

* toxygen.contact.Contact
* toxygen.profile.Profile
</details>
<!---Documatic-block-toxygen.basecontact.BaseContact-end--->

<!---Documatic-block-toxygen.contact.Contact-start--->
<details>
	<summary><code>toxygen.contact.Contact</code> (Click to Expand!)</summary>

* toxygen.friend.Friend
* toxygen.group_chat.GroupChat
</details>
<!---Documatic-block-toxygen.contact.Contact-end--->

<!---Documatic-block-toxygen.file_transfers.FileTransfer-start--->
<details>
	<summary><code>toxygen.file_transfers.FileTransfer</code> (Click to Expand!)</summary>

* toxygen.file_transfers.ReceiveTransfer
* toxygen.file_transfers.SendTransfer
</details>
<!---Documatic-block-toxygen.file_transfers.FileTransfer-end--->

<!---Documatic-block-toxygen.file_transfers.SendTransfer-start--->
<details>
	<summary><code>toxygen.file_transfers.SendTransfer</code> (Click to Expand!)</summary>

* toxygen.file_transfers.SendAvatar
* toxygen.file_transfers.SendFromFileBuffer
</details>
<!---Documatic-block-toxygen.file_transfers.SendTransfer-end--->

<!---Documatic-block-toxygen.passwordscreen.PasswordScreenBase-start--->
<details>
	<summary><code>toxygen.passwordscreen.PasswordScreenBase</code> (Click to Expand!)</summary>

* toxygen.passwordscreen.PasswordScreen
* toxygen.passwordscreen.UnlockAppScreen
</details>
<!---Documatic-block-toxygen.passwordscreen.PasswordScreenBase-end--->

<!---Documatic-block-toxygen.widgets.CenteredWidget-start--->
<details>
	<summary><code>toxygen.widgets.CenteredWidget</code> (Click to Expand!)</summary>

* toxygen.avwidgets.IncomingCallWidget
* toxygen.passwordscreen.PasswordScreenBase
</details>
<!---Documatic-block-toxygen.widgets.CenteredWidget-end--->

# #
<!---Documatic-section-Class Hierarchy-end--->

[_Documentation generated by Documatic_](https://www.documatic.com)
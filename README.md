# dress Symbol Export
Author: **docileninja/scienceman**

_Export Binary Ninja symbols to the dress symbol file format_

## Description:

This exports all global variables and .text functions to a symbol file of the form:

``` javascript
function1() @ *0x400000
function2() @ *0x400010
...
global1 @ *0x600000
global2 @ *0x600004
...
```

## Minimum Version

This plugin requires<sup>*</sup> the following minimum version of Binary Ninja:

 * release - 1.0.318
 * dev - 1.0.dev-654

<sup>*</sup> *This was developed on 1.0.dev-654 but will probably work on much older versions.*

## Required Dependencies

There are no dependencies for this plugin.

## License

This plugin is released under a [MIT](/LICENSE) license.


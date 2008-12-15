*********************************
The :mod:`repoze.what` XML plugin
*********************************

This is an adapters plugin for repoze.what.

Supported source formats
========================

A sample group source may look like this:

    <?xml version="1.0" encoding="UTF-8"?>
    <groups>
        <group name="admins">
            <member name="rms" />
        </group>
        <group name="developers">
            <member name="rms" />
            <member name="linus" />
        </group>
        <group name="trolls">
            <member name="sballmer" />
        </group>
        <group name="python">
            <!-- An empty group -->
        </group>
        <group name="php">
            <!-- An empty group -->
        </group>
    </groups>

A sample permission source may look like this:

    <?xml version="1.0" encoding="UTF-8"?>
    <permissions>
        <permission name="edit-site">
            <group name="admins" />
            <group name="developers" />
        </permission>
        <permission name="commit">
            <group name="developers" />
        </permission>
        <permission name="see-site">
            <group name="trolls" />
        </permission>
    </permissions>

# Sophist's Picard-Plugins

Sophist is a Picard user and amateur developer of Picard enhancements and plugins.

This repo stores copies of Sophist's Picard Plugins which are (mostly) listed on the [Picard Plugins wiki page](http://musicbrainz.org/doc/MusicBrainz_Picard/Plugins) and which are licensed under GPL and are freely available for download by other Picard users.

If you have the skills, please feel free to clone this repo and submit enhancements via the GitHub Pull Request process.

##View Variables plugin
Have you ever struggled to understand what script variables are available for you to put in your tagging or file renaming scripts, or what your use of $set in tagging scripts is actually doing?

Then this plugin is for you. It add's a context (right-click) menu item which shows a dialog listing all the variables available for a file.

Download the [ZIP file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/viewvariables.zip).

Full details in the [MusicBrainz forums](http://forums.musicbrainz.org/viewtopic.php?id=4886).

##Abbreviate artist-sort
Sometimes the album artist tag has a large number of individual names listed, particularly so for classical albums.

This plugin replaces the artists forenames with their initials i.e. `Bach, Johann Sebastian` with `Bach, J. S.` and so both shortens the string and makes it more readable.

This plugin operates only on the albumartistsort and artistsort tags.

Download the [abbreviate_artistsort.py file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/abbreviate_artistsort.py).

Full details in the [MusicBrainz forums](http://forums.musicbrainz.org/viewtopic.php?id=4893).

##Copy to Comment
Some music players are unable to display the standard tags produced by Picard for Composer, Performers etc.
This plugin copies this data to the default Comment so that these players can (hopefully) display this information.

Download the [copy_to_comment.py file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/copy_to_comment.py).

Full details in the [MusicBrainz forums](http://forums.musicbrainz.org/viewtopic.php?id=4895).

##Album Artist Website
Unfortunately, MusicBrainz does not supply the Artists Official Homepage url when Picard requests details for an album, and so the 'website variable and id3 WOAR tag cannot be populated.

This plugin makes an additional request to MusicBrainz to get this information and loads it into the 'website' variable.

Download the [albumartist_website.py file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/albumartist_website.py).

Full details in the [MusicBrainz forums](http://forums.musicbrainz.org/viewtopic.php?id=4906).

##Sort Multi-Value tags
This plugin sorts multi-value tags (like Performer, Composer etc.).

Download the [sort_multivalue_tags.py file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/sort_multivalue_tags.py).

##MusicBee compatibility
This plugin sets some tags to maximise the compatibility of mp3 files tagged by Picard with the MusicBee player.

Download the [musicbee_compatibility.py file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/musicbee_compatibility.py).

Full details in the [MusicBrainz forums](http://forums.musicbrainz.org/viewtopic.php?id=4903).

##Standardise Performers
This plugin splits multi-instrument performer tags into single instruments and combines names so that e.g. (from 10cc by 10cc track 1):
```
Performer [acoustic guitar, bass, dobro, electric guitar and tambourine]: Graham Gouldman
Performer [acoustic guitar, electric guitar, grand piano and synthesizer]: Lol Creme
Performer [electric guitar, moog and slide guitar]: Eric Stewart
```
becomes:
```
Performer [acoustic guitar]: Graham Gouldman; Lol Creme
Performer [bass]: Graham Gouldman
Performer [dobro]: Graham Gouldman
Performer [electric guitar]: Eric Stewart; Graham Gouldman; Lol Creme
Performer [grand piano]: Lol Creme
Performer [moog]: Eric Stewart
Performer [slide guitar]: Eric Stewart
Performer [synthesizer]: Lol Creme
Performer [tambourine]: Graham Gouldman
```

Download the [standardise_performers.py file here](https://github.com/Sophist-UK/Picard-Plugins/raw/master/standardise_performers.py).

Full details in the [MusicBrainz forums](http://forums.musicbrainz.org/viewtopic.php?id=4941).

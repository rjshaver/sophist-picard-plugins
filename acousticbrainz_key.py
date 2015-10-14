# -*- coding: utf-8 -*-

PLUGIN_NAME = _(u'AcousticBrainz Key')
PLUGIN_AUTHOR = u'Sophist'
PLUGIN_DESCRIPTION = u'''Add's the track's Key if:
<ol type="a">
<li>the musicbrainz_recordingid is in the track's metadata; and</li>
<li>if the key is in the AcousticBrainz database.</li>
</ol>'''
PLUGIN_VERSION = '0.1'
PLUGIN_API_VERSIONS = ["1.4.0"] # Requires support for TKEY which is in 1.4

import json
from picard import config, log
from picard.util import LockableObject
from picard.metadata import register_track_metadata_processor
from functools import partial
from picard.webservice import REQUEST_DELAY

ACOUSTICBRAINZ_HOST = "acousticbrainz.org"
ACOUSTICBRAINZ_PORT = 80
REQUEST_DELAY[(ACOUSTICBRAINZ_HOST, ACOUSTICBRAINZ_PORT)] = 50

class AcousticBrainz_Key:

    def get_key(self, album, track_metadata, trackXmlNode, releaseXmlNode):
        recordingId = track_metadata['musicbrainz_recordingid']
        if recordingId:
            log.debug("%s: Add AcusticBrainz request for %s(%s)", PLUGIN_NAME, track_metadata['title'], recordingId)
            self.album_add_request(album)
            path = "/%s/low-level" % recordingId
            return album.tagger.xmlws.get(
                        ACOUSTICBRAINZ_HOST,
                        ACOUSTICBRAINZ_PORT,
                        path,
                        partial(self.process_key, album, track_metadata),
                        xml=False, priority=True, important=False)
        return

    def process_key(self, album, track_metadata, response, reply, error):
        self.album_remove_request(album)
        if error:
            log.error("%s: Network error retrieving acousticBrainz data for recordingId %s",
                PLUGIN_NAME, track_metadata['musicbrainz_recordingid'])
            return
        data = json.loads(response)
        if "tonal" in data:
            if "key_key" in data["tonal"]:
                key = data["tonal"]["key_key"]
                if "key_scale" in data["tonal"]:
                    scale = data["tonal"]["key_scale"]
                    if scale == "minor":
                        key += "m"
                track_metadata["key"] = key
                log.debug("%s: Track '%s' is in key %s", PLUGIN_NAME, track_metadata["title"], key)
        if "rhythm" in data:
            if "bpm" in data["rhythm"]:
                bpm = int(data["rhythm"]["bpm"] + 0.5)
                track_metadata["bpm"] = bpm
                log.debug("%s: Track '%s' has %s bpm", PLUGIN_NAME, track_metadata["title"], bpm)

    def album_add_request(self, album):
        album._requests += 1

    def album_remove_request(self, album):
        album._requests -= 1
        if album._requests == 0:
            album._finalize_loading(None)

register_track_metadata_processor(AcousticBrainz_Key().get_key)

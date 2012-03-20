#############################################################################
#
# VoiceID, Copyright (C) 2011, Sardegna Ricerche.
# Email: labcontdigit@sardegnaricerche.it, michela.fancello@crs4.it, 
#        mauro.mereu@crs4.it
# Web: http://code.google.com/p/voiceid
# Authors: Michela Fancello, Mauro Mereu
#
# This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#############################################################################
"""
VoiceID is a speaker recognition/identification system written in Python,
based on the `LIUM Speaker Diarization <http://lium3.univ-lemans.fr/diarization/doku.php>`_ framework.

VoiceID can process video or audio files to identify in which slices of 
time there is a person speaking (diarization); then it examines all those
segments to identify who is speaking. To do so uses a voice models
database. 

To create the database you have to do a "train phase", in
interactive mode, by assigning a label to the "unknown" speakers.
You can also build yourself manually the speaker models and put in the db
using the scripts to create the gmm files.

"""
import os
import sys

#-------------------------------------
# initializations and global variables
#-------------------------------------

lium_jar = os.path.join(sys.prefix,'local/share/voiceid/LIUM_SpkDiarization-4.7.jar')  
ubm_path  = os.path.join(sys.prefix,'local/share/voiceid/ubm.gmm')
test_path  = os.path.expanduser('~/.voiceid/test')
db_dir = os.path.expanduser('~/.voiceid/gmm_db')
gender_gmms = os.path.join(sys.prefix,'local/share/voiceid/gender.gmms')
sms_gmms = os.path.join(sys.prefix,'local/share/voiceid/sms.gmms')
output_format = 'srt' #default output format
quiet_mode = False
verbose = False
keep_intermediate_files = False

output_redirect = open('/dev/null','w')
if verbose:
    output_redirect = open('/dev/stdout','w')

#!/usr/bin/env python

# From
# http://users.ohiohills.com/fmacall/YTCRACK.TXT

#itag=  video  resolution/bitrate
#value  type	:	'( w x h )  flags
#=====  =====  ==================

itag_dict = {
	5		:	'FLV 320 x 240',
	17		:	'3GP 176 x 144',
	18		:	'MP4 480 x 360',
	22		:	'MP4 1280 x 720',
	34		:	'FLV 480 x 360',
	35		:	'FLV 640 x 480 ',
	36		:	'3GP 320 x 240',
	37		:	'MP4 1920 x 1080',
	38		:	'MP4 2048 x 1080',
	43		:	'WEB 480 x 360',
	44		:	'WEB 640 x 480',
	45		:	'WEB 1280 x 720',
	46		:	'WEB 1920 x 1080',
	82		:	'MP4 480 x 360 3D',
	83		:	'MP4 640 x 480 3D',
	84		:	'MP4 1280 x 720 3D',
	85		:	'MP4 1920 x 1080 3D',
	100	:	'WEB 480 x 360 3D',
	101	:	'WEB 640 x 480 3D',
	102	:	'WEB 1280 x 720 3D',
	133	:	'MP4 320 x 240 VO',
	134	:	'MP4 480 x 360 VO',
	135	:	'MP4 640 x 480 VO',
	136	:	'MP4 1280 x 720 VO',
	137	:	'MP4 1920 x 1080 VO',
	139	:	'MP4 Low bitrate AO',
	140	:	'MP4 Med bitrate AO',
	141	:	'MP4 Hi  bitrate AO',
	160	:	'MP4 256 x 144 VO',
	171	:	'WEB Med bitrate AO',
	172	:	'WEB Hi  bitrate AO',
	242	:	'WEB 320 x 240 VOX',
	243	:	'WEB 480 x 360 VOX',
	244	:	'WEB 640 x 480 VOX',
	245	:	'WEB 640 x 480 VOX',
	246	:	'WEB 640 x 480 VOX',
	247	:	'WEB 1280 x 720 VOX',
	248	:	'WEB 1920 x 1080 VOX',
	264	:	'MP4 1920 x 1080 VO',
}

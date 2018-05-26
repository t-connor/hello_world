## coding : utf-8

import ConfigParser
import sys, getopt
import os

def main(filename):
	cf = ConfigParser.ConfigParser()
	cf.read(filename)
	secs = cf.sections()
	#print secs, type(secs)

	#GSM900_options = cf.options('GSM900 Sub band, RX loss')
	#print GSM900_band_RX, type(GSM900_band_RX)   #get the tab

	#GSM900_MAX_ARFCN = cf.items('GSM900 Sub band, RX loss')
	#print GSM900_MAX_ARFCN 					#get the tab and data

	## GSM900
	GSM900_MAX_ARFCN = cf.get('GSM900 Sub band, RX loss', 'Max ARFCN')
	GSM900_arfcn = GSM900_MAX_ARFCN.split(',')

	GSM900_RX_LOSS = cf.get('GSM900 Sub band, RX loss', 'RX loss')
	GSM900_loss = GSM900_RX_LOSS.split(',')

	GSM900_items = cf.items('GSM900 level, ramp')

	##print GSM900_items[4][1]
	
	GSM900_ARFCN = cf.get('GSM900 level, ramp', 'Subband max arfcn')
	GSM900_arfcn2 = GSM900_ARFCN.split(',')
	GSM900_LEVEL = cf.get('GSM900 level, ramp', 'Subband mid level')
	GSM900_level = GSM900_LEVEL.split(',')
	GSM900_HIGH_WEIGHT = cf.get('GSM900 level, ramp', 'Subband high weight')
	GSM900_high = GSM900_HIGH_WEIGHT.split(',')
	GSM900_LOW_WEIGHT = cf.get('GSM900 level, ramp', 'Subband low weight')
	GSM900_low = GSM900_LOW_WEIGHT.split(',')


	## DCS1800
	DCS1800_MAX_ARFCN = cf.get('DCS1800 Sub band, RX loss', 'Max ARFCN')
	DCS1800_arfcn = DCS1800_MAX_ARFCN.split(',')

	DCS1800_RX_LOSS = cf.get('DCS1800 Sub band, RX loss', 'RX loss')
	DCS1800_loss = DCS1800_RX_LOSS.split(',')

	DCS1800_items = cf.items('DCS1800 level, ramp')

	DCS1800_ARFCN = cf.get('DCS1800 level, ramp', 'Subband max arfcn')
	DCS1800_arfcn2 = DCS1800_ARFCN.split(',')
	DCS1800_LEVEL = cf.get('DCS1800 level, ramp', 'Subband mid level')
	DCS1800_level = DCS1800_LEVEL.split(',')
	DCS1800_HIGH_WEIGHT = cf.get('DCS1800 level, ramp', 'Subband high weight')
	DCS1800_high = DCS1800_HIGH_WEIGHT.split(',')
	DCS1800_LOW_WEIGHT = cf.get('DCS1800 level, ramp', 'Subband low weight')
	DCS1800_low = DCS1800_LOW_WEIGHT.split(',')

	## PCS1900
	PCS1900_MAX_ARFCN = cf.get('PCS1900 Sub band, RX loss', 'Max ARFCN')
	PCS1900_arfcn = PCS1900_MAX_ARFCN.split(',')

	PCS1900_RX_LOSS = cf.get('PCS1900 Sub band, RX loss', 'RX loss')
	PCS1900_loss = PCS1900_RX_LOSS.split(',')

	PCS1900_items = cf.items('PCS1900 level, ramp')

	PCS1900_ARFCN = cf.get('PCS1900 level, ramp', 'Subband max arfcn')
	PCS1900_arfcn2 = PCS1900_ARFCN.split(',')
	PCS1900_LEVEL = cf.get('PCS1900 level, ramp', 'Subband mid level')
	PCS1900_level = PCS1900_LEVEL.split(',')
	PCS1900_HIGH_WEIGHT = cf.get('PCS1900 level, ramp', 'Subband high weight')
	PCS1900_high = PCS1900_HIGH_WEIGHT.split(',')
	PCS1900_LOW_WEIGHT = cf.get('PCS1900 level, ramp', 'Subband low weight')
	PCS1900_low = PCS1900_LOW_WEIGHT.split(',')

	## GSM850
	GSM850_MAX_ARFCN = cf.get('GSM850 Sub band, RX loss', 'Max ARFCN')
	GSM850_arfcn = GSM850_MAX_ARFCN.split(',')

	GSM850_RX_LOSS = cf.get('GSM850 Sub band, RX loss', 'RX loss')
	GSM850_loss = GSM850_RX_LOSS.split(',')

	GSM850_items = cf.items('GSM850 level, ramp')

	##print GSM900_items[4][1]
	
	GSM850_ARFCN = cf.get('GSM850 level, ramp', 'Subband max arfcn')
	GSM850_arfcn2 = GSM850_ARFCN.split(',')
	GSM850_LEVEL = cf.get('GSM850 level, ramp', 'Subband mid level')
	GSM850_level = GSM850_LEVEL.split(',')
	GSM850_HIGH_WEIGHT = cf.get('GSM850 level, ramp', 'Subband high weight')
	GSM850_high = GSM850_HIGH_WEIGHT.split(',')
	GSM850_LOW_WEIGHT = cf.get('GSM850 level, ramp', 'Subband low weight')
	GSM850_low = GSM850_LOW_WEIGHT.split(',')

	name = filename.split('.')
	f = open(name[0] + '.txt', 'w')
	a = ""

	a += '\t/* GSM850....................................................................*/\n\n\n'
	a += '\tsAGCGAINOFFSET  AGC_PATHLOSS_GSM850[ PLTABLE_SIZE ] =\n\t{\n\n'
	for i in range(len(GSM850_arfcn)):
		a += '\t\t{   %s,  GAINLOSS( %s ) },\n' %(GSM850_arfcn[i], GSM850_loss[i])
	a += '\t\t/*-------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\n\t};\n\n'

	a += '\t/* GSM900....................................................................*/\n\n\n'
	a += '\tsAGCGAINOFFSET  AGC_PATHLOSS_GSM900[ PLTABLE_SIZE ] =\n\t{\n\n'
	for i in range(len(GSM900_arfcn)):
		a += '\t\t{   %s,  GAINLOSS( %s ) },\n' %(GSM900_arfcn[i], GSM900_loss[i])
	a += '\t\t/*-------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\n\t};\n\n'

	a += '\t/* DCS1800....................................................................*/\n\n\n'
	a += '\tsAGCGAINOFFSET  AGC_PATHLOSS_DCS1800[ PLTABLE_SIZE ] =\n\t{\n'
	for i in range(len(DCS1800_arfcn)):
		a += '\t\t{   %s,  GAINLOSS( %s ) },\n' %(DCS1800_arfcn[i], DCS1800_loss[i])
	a += '\t\t/*-------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\n\t};\n\n'

	a += '\t/* PCS1900....................................................................*/\n\n'
	a += '\tsAGCGAINOFFSET  AGC_PATHLOSS_PCS1900[ PLTABLE_SIZE ] =\n\t{\n'
	for i in range(len(PCS1900_arfcn)):
		a += '\t\t{   %s,  GAINLOSS( %s ) },\n' %(PCS1900_arfcn[i], PCS1900_loss[i])
	a += '\t\t/*-------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\n\t};\n\n'

	a += '\t/*...........................................................................*/\n'
	a += '\tsAGCGAINOFFSET*  AGC_PATHLOSS_TABLE[] =\n'
	a += '\t{  0,                                 /* FrequencyBand400  */\n'
	a += '\t   AGC_PATHLOSS_GSM850,               /* FrequencyBand850  */\n'
	a += '\t   AGC_PATHLOSS_GSM900,               /* FrequencyBand900  */\n'
	a += '\t   AGC_PATHLOSS_DCS1800,               /* FrequencyBand1800 */\n'
	a += '\t   AGC_PATHLOSS_PCS1900,               /* FrequencyBand1900 */\n'
	a += '\t};\n\n'

	a += '\t/*----------------------------------------*/\n'
	a += '\t/* Calibration data for power ramp        */\n'
	a += '\t/*----------------------------------------*/\n\n\n'

	a += '\t#define  APC_DC_OFFSET   0//hulin modify 20140912    //70\n\n'

	a += '\t/* GSM850....................................................................*/\n\n'

	a += '\tsRAMPDATA  GSM850_RampData =\n\t{\n\n'
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* lowest power */\n'
	a += '\t((APC_DC_OFFSET)<<8) | %s,\n'  %(GSM850_items[3][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* power level  */\n'
	a += '\t/*  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35 dBm                        */\n'
	a += '\t/* JP {  62, 72, 85, 100, 117,135,160,190,227,270,333,405,495,610,700,700 }, */\n'
	a += '\t\t{%s},\n'  %(GSM850_items[4][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t{\n'
	a += '\t  /* profile  0 :  5 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[5][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[6][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  1 :  7 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[7][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[8][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  2 :  9 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[9][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[10][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  3 : 11 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[11][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[12][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  4 : 13 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[13][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[14][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  5 : 15 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[15][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[16][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  6 : 17 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[17][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[18][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  7 : 19 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[19][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[20][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  8 : 21 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[21][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[22][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  9 : 23 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[23][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[24][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 10 : 25 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[25][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[26][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 11 : 27 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[27][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[28][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 12 : 29 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[29][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[30][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 13 : 31 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[31][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[32][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 14 : 33 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[33][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[34][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 15 : 35 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM850_items[35][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM850_items[36][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t},\n'
	a += '\t/* ARFCN WEIGHT */\n'
	a += '\t{  /* max arfcn , mid_level ,  hi_weight   ,  lo_weight   */\n'
	for i in range(len(GSM850_arfcn2)):
		a += '\t\t{         %s,       %s , WEIGHT(%s), WEIGHT(%s) },\n'  % (GSM850_arfcn2[i], GSM850_level[i], GSM850_high[i], GSM850_low[i])
	a += '\t\t/*------------------------------------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\t},\n'
	a += '\t/* Battery WEIGHT */\n'
	a += '\t{  /*      low temp,       mid temp,        hi temp */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* low volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* mid volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /*  hi volt */\n'
	a += '\t},\n'
	a += '\t};\n\n\n\n\n\n'

	a += '\t/* GSM900....................................................................*/\n\n'

	a += '\tsRAMPDATA  GSM_RampData =\n\t{\n\n'
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* lowest power */\n'
	a += '\t((APC_DC_OFFSET)<<8) | %s,\n'  %(GSM900_items[3][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* power level  */\n'
	a += '\t/*  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35 dBm                        */\n'
	a += '\t/* JP {  62, 72, 85, 100, 117,135,160,190,227,270,333,405,495,610,700,700 }, */\n'
	a += '\t\t{%s},\n'  %(GSM900_items[4][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t{\n'
	a += '\t  /* profile  0 :  5 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[5][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[6][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  1 :  7 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[7][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[8][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  2 :  9 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[9][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[10][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  3 : 11 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[11][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[12][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  4 : 13 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[13][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[14][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  5 : 15 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[15][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[16][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  6 : 17 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[17][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[18][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  7 : 19 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[19][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[20][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  8 : 21 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[21][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[22][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  9 : 23 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[23][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[24][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 10 : 25 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[25][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[26][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 11 : 27 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[27][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[28][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 12 : 29 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[29][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[30][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 13 : 31 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[31][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[32][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 14 : 33 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[33][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[34][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 15 : 35 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(GSM900_items[35][1])
	a += '\t     /* ramp down */    {%s} }\n' %(GSM900_items[36][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t},\n'
	a += '\t/* ARFCN WEIGHT */\n'
	a += '\t{  /* max arfcn , mid_level ,  hi_weight   ,  lo_weight   */\n'
	for i in range(len(GSM900_arfcn2)):
		a += '\t\t{         %s,       %s , WEIGHT(%s), WEIGHT(%s) },\n'  % (GSM900_arfcn2[i], GSM900_level[i], GSM900_high[i], GSM900_low[i])
	a += '\t\t/*------------------------------------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\t},\n'
	a += '\t/* Battery WEIGHT */\n'
	a += '\t{  /*      low temp,       mid temp,        hi temp */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* low volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* mid volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /*  hi volt */\n'
	a += '\t},\n'
	a += '\t};\n\n\n\n\n\n'

	a += '\t/* DCS1800....................................................................*/\n\n'

	a += '\tsRAMPDATA  DCS_RampData =\n\t{\n\n'
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* lowest power */\n'
	a += '\t((APC_DC_OFFSET)<<8) | %s,\n'  %(DCS1800_items[3][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* power level  */\n'
	a += '\t	   /*    0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30 dBm                      */\n'
	a += '\t\t{%s},\n'  %(DCS1800_items[4][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t{\n'
	a += '\t  /* profile  0 :  0 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[5][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[6][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  1 :  2 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[7][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[8][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  2 :  4 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[9][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[10][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  3 :  6 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[11][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[12][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  4 :  8 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[13][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[14][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  5 : 10 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[15][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[16][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  6 : 12 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[17][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[18][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  7 : 14 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[19][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[20][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  8 : 16 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[21][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[22][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  9 : 18 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[23][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[24][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 10 : 20 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[25][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[26][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 11 : 22 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[27][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[28][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 12 : 24 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[29][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[30][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 13 : 26 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[31][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[32][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 14 : 28 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[33][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[34][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 15 : 30 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(DCS1800_items[35][1])
	a += '\t     /* ramp down */    {%s} }\n' %(DCS1800_items[36][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t},\n'
	a += '\t/* ARFCN WEIGHT */\n'
	a += '\t{  /* max arfcn , mid_level ,  hi_weight   ,  lo_weight   */\n'
	for i in range(len(DCS1800_arfcn2)):
		a += '\t\t{         %s,       %s , WEIGHT(%s), WEIGHT(%s) },\n'  % (DCS1800_arfcn2[i], DCS1800_level[i], DCS1800_high[i], DCS1800_low[i])
	a += '\t\t/*------------------------------------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\t},\n'
	a += '\t/* Battery WEIGHT */\n'
	a += '\t{  /*      low temp,       mid temp,        hi temp */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* low volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* mid volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /*  hi volt */\n'
	a += '\t},\n'
	a += '\t};\n\n\n\n\n\n'

	a += '\t/* PCS1900....................................................................*/\n\n'

	a += '\tsRAMPDATA  PCS_RampData =\n\t{\n\n'
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* lowest power */\n'
	a += '\t((APC_DC_OFFSET)<<8) | %s,\n'  %(PCS1900_items[3][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t/* power level  */\n'
	a += '\t/*  0,  2,   4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30 dBm                        */\n'
	a += '\t\t{%s},\n'  %(PCS1900_items[4][1])
	a += '\t/*-------------------------------------------------------------------------------------------*/\n'
	a += '\t{\n'
	a += '\t  /* profile  0 :  0 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[5][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[6][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  1 :  2 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[7][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[8][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  2 :  4 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[9][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[10][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  3 :  6 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[11][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[12][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  4 :  8 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[13][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[14][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  5 : 10 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[15][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[16][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  6 : 12 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[17][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[18][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  7 : 14 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[19][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[20][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  8 : 16 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[21][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[22][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile  9 : 18 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[23][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[24][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 10 : 20 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[25][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[26][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 11 : 22 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[27][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[28][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 12 : 24 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[29][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[30][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 13 : 26 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[31][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[32][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 14 : 28 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[33][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[34][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t  /* profile 15 : 30 dBm | p00,p01,p02,p03,p04,p05,p06,p07,p08,p09,p10,p11,p12,p13,p14,p15  */\n'
	a += '\t  {  /* ramp up   */ {  {%s},\n'  %(PCS1900_items[35][1])
	a += '\t     /* ramp down */    {%s} }\n' %(PCS1900_items[36][1])
	a += '\t  }, /*-------------------------------------------------------------------------------------*/\n'
	a += '\t},\n'
	a += '\t/* ARFCN WEIGHT */\n'
	a += '\t{  /* max arfcn , mid_level ,  hi_weight   ,  lo_weight   */\n'
	for i in range(len(PCS1900_arfcn2)):
		a += '\t\t{         %s,       %s , WEIGHT(%s), WEIGHT(%s) },\n'  % (PCS1900_arfcn2[i], PCS1900_level[i], PCS1900_high[i], PCS1900_low[i])
	a += '\t\t/*------------------------------------------------------*/\n'
	a += '\t\t{ TABLE_END }\n'
	a += '\t},\n'
	a += '\t/* Battery WEIGHT */\n'
	a += '\t{  /*      low temp,       mid temp,        hi temp */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* low volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /* mid volt */\n'
	a += '\t\t{  WEIGHT(1.000),  WEIGHT(1.000),  WEIGHT(1.000)  },  /*  hi volt */\n'
	a += '\t},\n'
	a += '\t};\n\n\n'

	f.write(a)
	f.close()

	print 'Generate %s.txt, Completed!' %(name[0])


if __name__ == '__main__':
        #print 'please input the filename:'
        #filename = sys.argv[1]
	#main(filename)

        items = os.listdir('.')
        filename = []
        for names in items:
                name = names.split('.')
                if name[1] == 'ini':
                        filename.append(name[0])
        #print filename

        for i in range(len(filename)):
                main(filename[i]+'.ini')        

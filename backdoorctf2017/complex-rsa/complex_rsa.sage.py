# This file was *autogenerated* from the file complex_rsa.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_37507589401 = Integer(37507589401); _sage_const_554264859105764813308660999731057971935100899008191382001838196926947542874512190874402841957978974562758951331436856029517893995971179950228409634742368823490858553015862605452077729540463185207987338059905256552215054036643656077780363670065154151957507791559734841291875379738678210733333998195096643491711 = Integer(554264859105764813308660999731057971935100899008191382001838196926947542874512190874402841957978974562758951331436856029517893995971179950228409634742368823490858553015862605452077729540463185207987338059905256552215054036643656077780363670065154151957507791559734841291875379738678210733333998195096643491711); _sage_const_4268405784672563577566143285906824408738650526784746749170468318123056940297449811287105187623419766934370809781249030117023876215912795037797160740003478418767197450012472858547143622542113157392499087427939336504102036205305906052998841826136038160560099357503377453502865716581429205507834478651 = Integer(4268405784672563577566143285906824408738650526784746749170468318123056940297449811287105187623419766934370809781249030117023876215912795037797160740003478418767197450012472858547143622542113157392499087427939336504102036205305906052998841826136038160560099357503377453502865716581429205507834478651); _sage_const_0x02acd7d7f075333f571c1e342ccfdee05d9262beef9398e54d25f0c3a72d4817ce61971e546923bf5726299be22fd8a74fba6e39ca6b4c2cac7d88480a10f32c26ab5f84bc772c763094e7d4ad81a4d8b8c03bf19045303713ef53cf162fce89ca73ca6376bd73d808d9e9818a160c6be205591583032871127cbb363946812527 = Integer(0x02acd7d7f075333f571c1e342ccfdee05d9262beef9398e54d25f0c3a72d4817ce61971e546923bf5726299be22fd8a74fba6e39ca6b4c2cac7d88480a10f32c26ab5f84bc772c763094e7d4ad81a4d8b8c03bf19045303713ef53cf162fce89ca73ca6376bd73d808d9e9818a160c6be205591583032871127cbb363946812527)
n = _sage_const_554264859105764813308660999731057971935100899008191382001838196926947542874512190874402841957978974562758951331436856029517893995971179950228409634742368823490858553015862605452077729540463185207987338059905256552215054036643656077780363670065154151957507791559734841291875379738678210733333998195096643491711 
e1 = _sage_const_37507589401 
e2 = _sage_const_4268405784672563577566143285906824408738650526784746749170468318123056940297449811287105187623419766934370809781249030117023876215912795037797160740003478418767197450012472858547143622542113157392499087427939336504102036205305906052998841826136038160560099357503377453502865716581429205507834478651 
c = _sage_const_0x02acd7d7f075333f571c1e342ccfdee05d9262beef9398e54d25f0c3a72d4817ce61971e546923bf5726299be22fd8a74fba6e39ca6b4c2cac7d88480a10f32c26ab5f84bc772c763094e7d4ad81a4d8b8c03bf19045303713ef53cf162fce89ca73ca6376bd73d808d9e9818a160c6be205591583032871127cbb363946812527 

e = e1 * e2

lst = continued_fraction(e/n)
conv = lst.convergents()
for i in conv:

	k = i.numerator()
	d = i.denominator()

	try:
		m = hex(int(pow(c,d,n)))[_sage_const_2 :-_sage_const_1 ].decode("hex")
		if "CTF" in m:
			print m
	except:
		continue
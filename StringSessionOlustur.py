from pyrogram import Client
print("""  
   +--------------+ 
   |.------------.| 
   ||Thor UserBot|| 
   ||            || 
   ||   String   || 
   ||   Alıcı    || 
   |+------------+| 
   +-..--------..-+ 
   .--------------. 
  / /============\ \  
 / /==============\ \ 
/____________________\   
\____________________/  
""")
phone = input("Lütfen numaranızı ülke kodu ile beraber yazınız\n ➜")

app = Client(':memory:',api_id="4150176",api_hash="cc60c01e601ee9cd77fe5ec6a6129882",app_version='ThorUserBot',device_model='Thor',system_version='1.0',lang_code='tr',phone_number=phone)
with app:
    self = app.get_me()
    session = app.export_session_string()
    out = f'''<b>SESSION:</b> <code>{session}</code>\n<b>NOT: Bu bilgiyi kurulum dışında hiçbir yere/kimseye vermeyiniz!</b>'''
    print(f"\n\n{session}\nNOT: Bu bilgiyi kurulum dışında hiçbir yere/kimseye vermeyiniz!\n")
    app.send_message('me', out, parse_mode="html")
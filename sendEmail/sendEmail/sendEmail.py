import smtplib

fromaddr = 'keith.h.hill.85@gmail.com'
toaddrs  = 'diknak@gmail.com'
msg = "\r\n".join([
  "From: user_me@gmail.com",
  "To: user_you@gmail.com",
  "Subject: Just a message",
  "",
  "Why, oh why"
  ])
username = 'keith.h.hill.85@gmail.com'
password = 'eajvuqtyskigalff'
server = smtplib.SMTP('smtp.live.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

import smtplib as s
smtpobj = s.SMTP("smtp.gmail.com", 587)
smtpobj.starttls()
smtpobj.login("gurjeetpalbawa1990@gmail.com", "password")

subject = "Email send through script ... "
body = "This email is generated using script. No need to respond..."

message = "Mail:{}\n\n\n{}".format(subject, body)

smtpobj.sendmail("gurjeetpalbawa1990@gmail.com", ["gurjeetpalbawa1990@gmail.com", "harishk@pu.ac.in", "akashdeep@pu.ac.in", "sakshi@pu.ac.in"], message)

print("Mail sended successfully...")
smtpobj.close()
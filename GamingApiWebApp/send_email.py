import smtplib, ssl

def sendEmail(toAddress, msg):
  host = "smtp.gmail.com"
  port = 465

  username = "YOUR EMAIL USERNAME"
  password = "YOUR PASSWORD" # Enviroment Variable

  sent_from = "jhornjr@gmail.com"
  context = ssl.create_default_context()

  result = ""

  try:

    with smtplib.SMTP_SSL(host, port, context=context) as server:
      server.login(username, password)
      server.sendmail(from_addr=sent_from, to_addrs=toAddress, msg=msg)
      result = "Message sent. Thank you."
      return result

  except:
    result = "Error: Message could not be sent. Try again."
    return result

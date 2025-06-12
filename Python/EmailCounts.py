def organize_inbox(inbox_string):
    emails = inbox_string.split(';')
    senders = {}
    senders_tuple  = []

    for email in emails:
        address = email.split(',')[0].strip()
        if address in senders:
            senders[address] += 1
        else:
            senders[address] = 1

    for address, count in senders.items():
        senders_tuple.append((address, count))

    senders_tuple = sorted(senders_tuple, key=lambda x:(-x[1], x[0]))
    
    return(senders_tuple) #pass


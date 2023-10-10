phase1 = extract(url)
    ext = parse_data(phase1)
    print(ext)
    if not os.path.exists("data.txt"):
         create_file()
         pass
    file = read_file()
    if ext != "No upcoming tours":
        if ext not in file:
            write_msg(ext)
            send_email("Hello!")
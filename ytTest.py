import webbrowser

search = input('enter the topic and thing you want to search on YT: ')

if len(search) > 0:
    search_query = search
    youtube_search_url = f"https://www.youtube.com/results?search_query={search_query}"
    webbrowser.open(youtube_search_url)

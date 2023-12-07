import speedtest


def int_spd():
    # Speed test
    st = speedtest.Speedtest()

    # Download speed
    ds = st.download()
    # Upload speed
    us = st.upload()

    # Human size
    def humansize(nbytes):
        suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
        i = 0
        while nbytes >= 1024 and i < len(suffixes)-1:
            nbytes /= 1024.
            i += 1
        f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
        return '%s %s' % (f, suffixes[i])

    download = humansize(ds)
    upload = humansize(us)

    return f'''Prędkość pobierania: {download}'
    Prędkość publikowania: {upload}'''

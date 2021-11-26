def test(value):
    print(repr(value), 'to', end=' ')
    try:
        value + 0
    except TypeError:
        try:
            value + ''
        except TypeError:
            print('ani liczba, ani tekst')
        else:
            print('jakiś tekst')
    else:
        print('jakaś liczba')


test(None)

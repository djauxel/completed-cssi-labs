def pluralizer(singular):
    if singular[-3:] == "ife":
        plural = singular[:-3] + 'ives'
    elif singular[-2:] == 'sh':
        plural = singular + 'es'
    elif singular[-2:] == 'ch':
        plural = singular + 'es'
    elif singular[-2:] == 'us':
        plural = singular[:-2] + 'i'
    elif singular[-2:] in ['ay', 'oy', 'ey', 'uy']:
        plural = singular + 's'
    elif singular[-1:] == 'y':
        plural = singular[:-1] + 'ies'
    else:
        plural = singular + 's'
    return plural

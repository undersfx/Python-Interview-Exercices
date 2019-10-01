from functools import wraps

STDFMT = '{dia}/{mes}/{ano}'

def format_date(date_format=STDFMT):
    
    def decorator(func):
        
        @wraps(func)
        def inner(dia, mes, ano):
            result = date_format.format(**locals())
            print(result)

        return inner

    return decorator

# Normal Call
def show_date(dia, mes, ano):
    print(f'{dia}/{mes}/{ano}')

show_date('11', '07', '1991')

# Formated Call
@format_date('{ano}-{mes}-{dia}')
def show_fdate(dia, mes, ano):
    print(f'{dia}/{mes}/{ano}')

show_fdate('11', '07', '1991')
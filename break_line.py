"""
 Breaks a line longer than 40 characters on the next word.
"""

texto = '''
Lorem ipsum aliquet taciti donec habitant lobortis gravida mi iaculis 
ad tempor urna sociosqu, et consectetur donec vel quisque rutrum torquent 
faucibus aenean eros pharetra imperdiet. tortor ad hendrerit mattis purus 
id porttitor sollicitudin est nisl, habitasse sit felis hac placerat nisl 
venenatis metus dictum, euismod aenean sagittis eros enim felis aptent potenti. 
luctus aliquet sapien aenean ac elementum vivamus bibendum aliquet, quisque 
scelerisque semper feugiat tincidunt quisque suspendisse a, mauris maecenas 
orci lobortis placerat tempor litora. tortor class elementum arcu leo ipsum 
turpis aenean velit mollis, sodales taciti viverra praesent pretium pellentesque 
suscipit metus aliquam libero, per faucibus consequat volutpat nisl nibh neque vel.
'''

def quebra_linha(texto, n=39):
    resto = texto[n:].split()
    linha = texto[:n] + resto[0]
    resto = ' '.join(resto[1:])

    return linha, resto

while len(texto) > 40:
    linha, resto = quebra_linha(texto)
    print(linha)
    texto = resto

print(resto)
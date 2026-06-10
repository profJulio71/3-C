"""
Dada a tupla frutas = ('maçã', 'banana', 'laranja', 'uva'), crie uma nova
tupla chamada frutas_selcontendo apenas as frutas que começam com a letra ‘l’.
Pesquise sobre o método startswithde strings.
"""

frutas = ('maçã', 'banana', 'laranja', 'uva')
frutas_sel = tuple(fruta for fruta in frutas if fruta.startswith('l'))

print(frutas_sel)
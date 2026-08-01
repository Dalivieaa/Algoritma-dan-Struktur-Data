# 7. SET
basket = {'apple', 'orange', 'apple','pear','orange','banana'}
print("isi basket:", basket)

#mengecek keanggotaan
print('orange' in basket)     # mengecek apakah 'orange' ada di bsaket?
print('crabgrass' in basket)  # mengecek apakah 'crabgrass' ada di basket?

#set dari dua kata huruf (huruf unik)
a = set('abracadabra')
b = set('alacazam')

print("set a:", a)
print("set b:", b)

#operasi set
print(a-b)    # huruf di a tapi tidak di b (a-b)
print(a|b)    # gabungan (a|b)
print(a & b)  # irisan (a & b)
print(a ^ b)  # selisih simetris (a^b)
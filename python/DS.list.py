#!/usr/bin/python

shoplist= ['apple', 'mango', 'carrot', 'banana']
print 'I hava', len(shoplist), 'items to buy.'

print 'These items are:',
for item in shoplist:
	print item,

print '\nI aslo have to buy rice.'
shoplist.append('rice')
print 'My shopping list is now', shoplist

print 'I will sort my list now'
shoplist.sort()
print 'Sorted shopping list is', shoplist

print 'The first item i will buy is', shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print 'I bought the', olditem
print 'My shopping list is now', shoplist
